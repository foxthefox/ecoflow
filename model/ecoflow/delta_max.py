from model.ecoflow.base_device import EcoflowDevice
from model.connector import Connector
import logging
import re
import math

_LOGGER = logging.getLogger(__name__)

class Ecoflow_DeltaMax(EcoflowDevice):
    def __init__(self, serial: str, user_id: str, stdscr=None):
        super().__init__(serial, user_id, stdscr)
        self.uses_protobuf = False
        self.screen_initialized = False

        self.connector = Connector(self.device_sn, "delta-max", name="Delta Max", screen=stdscr)
        self.connector.col_width = 38
        self.connector.show_filter = lambda name : name[0:3] in ["bms", "ems", "pd."] and name[0:7] != "pd.icon"

        self.add_cmd_id_handler(self.handle_heartbeat, [0, "latestQuotas", "params"])

    def init_subscriptions(self):        
        super().init_subscriptions()
        self.request_data()       
        self.client.subscribe(self._set_topic, self)
        self.client.subscribe(self._get_topic, self) 

    def handle_heartbeat(self, message: dict):
        data_map = None

        if "params" in message:
            data_map = message["params"]
        elif "data" in message:
            data_map = message["data"]["quotaMap"]
            if not self.screen_initialized:
                self.connector.init_screen(list(data_map.keys()), prefixes={
                    "bmsMaster.": 1,
                    "bmsSlave1.": 2,
                    "ems.": 3,
                    "pd.": 4
                })
                self.screen_initialized = True

                # dump config
                # config = {}
                # names = list(data_map.keys())
                # names.sort()
                # for name in names:
                #     [unit, divisor, special_handler] = self.get_param_settings(name).values()
                #     [node, property_name] = name.split(".")
                #     config[name] = {
                #         "divisor": divisor, 
                #         "unit": unit, 
                #         "node": node,
                #         "name": property_name
                #     }
                #     if special_handler is not None:
                #         config[name]["converter"] = special_handler
                # with open('delta-max.json', 'w') as f:
                #     import json
                #     f.write(json.dumps(config, indent=2))

        
        if data_map is not None:
            for name, val in data_map.items():
                if val is not None:
                    [unit, divisor, special_handler] = self.get_param_settings(name).values()
                    if special_handler == "time":
                        # time in minutes
                        h = math.floor(val/60)
                        m = val % 60
                        val = "%02d:%02d" % (h, m)                   
                    if divisor != 1:
                        val = val / divisor
                    self.connector.update(name, val, unit)
                    _LOGGER.debug(f"update received {name}: {val} {unit}")
            self.connector.end_update()

    def detect_param_settings(self, name) -> dict:
        sub_device, param_name = name.split(".") if "." in name else [None, name]
        name_parts = [x.lower() for x in re.sub(r"([A-Z])", r" \1", param_name).split()]
        unit = ""
        divisor = 1
        special_handler = None
        if "watts" in name_parts or "power" in name_parts:
            divisor = 10 if name not in ["inv.outputWatts"] else 1
            unit = "W"
        elif "cur" in name_parts or "amp" in name_parts:
            #divisor = 10
            unit = "A"
        elif "temp" in name_parts:
            #divisor = 10
            unit = "°C"
        elif "volt" in name_parts:
            #divisor = 10 # ???
            unit = "V"
        elif "voltage" in name_parts:
            divisor = 1000
            unit = "V"
        elif "brightness" in name_parts:
            #divisor = 10
            unit = "%"
        elif "cap" in name_parts:
            divisor = 10
            unit = "Wh"
        elif "soc" in name_parts or "soh" in name_parts:
            unit = "%"
        elif "time" in name_parts:
            special_handler = "minutes"
        return {
            "unit": unit,
            "divisor": divisor,
            "special_handler": special_handler
        }
