# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/protos/platform.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmodel/protos/platform.proto\x12\x0cmodel.protos\"i\n\nEnergyItem\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x17\n\nwatth_type\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\r\n\x05watth\x18\x03 \x03(\rB\x0c\n\n_timestampB\r\n\x0b_watth_type\"{\n\x11\x45nergyTotalReport\x12\x16\n\twatth_seq\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x31\n\nwatth_item\x18\x02 \x01(\x0b\x32\x18.model.protos.EnergyItemH\x01\x88\x01\x01\x42\x0c\n\n_watth_seqB\r\n\x0b_watth_item\"l\n\x16\x42\x61tchEnergyTotalReport\x12\x16\n\twatth_seq\x18\x01 \x01(\rH\x00\x88\x01\x01\x12,\n\nwatth_item\x18\x02 \x03(\x0b\x32\x18.model.protos.EnergyItemB\x0c\n\n_watth_seq\"\x84\x01\n\x14\x45nergyTotalReportAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\twatth_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x17\n\nwatth_type\x18\x03 \x01(\rH\x02\x88\x01\x01\x42\t\n\x07_resultB\x0c\n\n_watth_seqB\r\n\x0b_watth_type\"\xa7\x01\n\x0f\x45ventRecordItem\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x13\n\x06sys_ms\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x15\n\x08\x65vent_no\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x19\n\x0c\x65vent_detail\x18\x04 \x01(\x02H\x03\x88\x01\x01\x42\x0c\n\n_timestampB\t\n\x07_sys_msB\x0b\n\t_event_noB\x0f\n\r_event_detail\"\x92\x01\n\x11\x45ventRecordReport\x12\x16\n\tevent_ver\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\tevent_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x31\n\nevent_item\x18\x03 \x03(\x0b\x32\x1d.model.protos.EventRecordItemB\x0c\n\n_event_verB\x0c\n\n_event_seq\"\x8a\x01\n\x12\x45ventInfoReportAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\tevent_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x1b\n\x0e\x65vent_item_num\x18\x03 \x01(\rH\x02\x88\x01\x01\x42\t\n\x07_resultB\x0c\n\n_event_seqB\x11\n\x0f_event_item_num\",\n\x0eProductNameSet\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"3\n\x11ProductNameSetAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x42\t\n\x07_result\"\x10\n\x0eProductNameGet\"/\n\x11ProductNameGetAck\x12\x11\n\x04name\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x0c\n\nRTCTimeGet\"Y\n\rRTCTimeGetAck\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x15\n\x08timezone\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_timestampB\x0b\n\t_timezone\"V\n\nRTCTimeSet\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x15\n\x08timezone\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_timestampB\x0b\n\t_timezone\"/\n\rRTCTimeSetAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x42\t\n\x07_result\"T\n\x14\x63ountry_town_message\x12\x14\n\x07\x63ountry\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04town\x18\x02 \x01(\rH\x01\x88\x01\x01\x42\n\n\x08_countryB\x07\n\x05_town*N\n\tPlCmdSets\x12\x14\n\x10PL_NONE_CMD_SETS\x10\x00\x12\x15\n\x11PL_BASIC_CMD_SETS\x10\x01\x12\x14\n\x0fPL_EXT_CMD_SETS\x10\xfe\x01*F\n\x07PlCmdId\x12\x12\n\x0ePL_CMD_ID_NONE\x10\x00\x12\x12\n\x0ePL_CMD_ID_XLOG\x10\x10\x12\x13\n\x0fPL_CMD_ID_WATTH\x10 b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.protos.platform_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLCMDSETS._serialized_start=1476
  _PLCMDSETS._serialized_end=1554
  _PLCMDID._serialized_start=1556
  _PLCMDID._serialized_end=1626
  _ENERGYITEM._serialized_start=45
  _ENERGYITEM._serialized_end=150
  _ENERGYTOTALREPORT._serialized_start=152
  _ENERGYTOTALREPORT._serialized_end=275
  _BATCHENERGYTOTALREPORT._serialized_start=277
  _BATCHENERGYTOTALREPORT._serialized_end=385
  _ENERGYTOTALREPORTACK._serialized_start=388
  _ENERGYTOTALREPORTACK._serialized_end=520
  _EVENTRECORDITEM._serialized_start=523
  _EVENTRECORDITEM._serialized_end=690
  _EVENTRECORDREPORT._serialized_start=693
  _EVENTRECORDREPORT._serialized_end=839
  _EVENTINFOREPORTACK._serialized_start=842
  _EVENTINFOREPORTACK._serialized_end=980
  _PRODUCTNAMESET._serialized_start=982
  _PRODUCTNAMESET._serialized_end=1026
  _PRODUCTNAMESETACK._serialized_start=1028
  _PRODUCTNAMESETACK._serialized_end=1079
  _PRODUCTNAMEGET._serialized_start=1081
  _PRODUCTNAMEGET._serialized_end=1097
  _PRODUCTNAMEGETACK._serialized_start=1099
  _PRODUCTNAMEGETACK._serialized_end=1146
  _RTCTIMEGET._serialized_start=1148
  _RTCTIMEGET._serialized_end=1160
  _RTCTIMEGETACK._serialized_start=1162
  _RTCTIMEGETACK._serialized_end=1251
  _RTCTIMESET._serialized_start=1253
  _RTCTIMESET._serialized_end=1339
  _RTCTIMESETACK._serialized_start=1341
  _RTCTIMESETACK._serialized_end=1388
  _COUNTRY_TOWN_MESSAGE._serialized_start=1390
  _COUNTRY_TOWN_MESSAGE._serialized_end=1474
# @@protoc_insertion_point(module_scope)
