# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/protos/options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1amodel/protos/options.proto\x12\x0cmodel.protos\x1a google/protobuf/descriptor.proto\"f\n\tHomieNode\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\tno_retain\x18\x04 \x01(\x08\x12\x1e\n\x03qos\x18\x05 \x01(\x0e\x32\x11.model.protos.Qos\"\x9c\x01\n\x0c\x44\x65rivedField\x12(\n\x08operator\x18\x01 \x01(\x0e\x32\x16.model.protos.Operator\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x0c\n\x04node\x18\x04 \x01(\t\x12\x0e\n\x06\x66ields\x18\x06 \x03(\t\x12\x11\n\x04unit\x18\x07 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_unit\"\xd4\x01\n\x0eMappingOptions\x12\x14\n\x07\x64ivisor\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04unit\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tconverter\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x0f\n\x02id\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x11\n\x04node\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0c\x64isplay_name\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\n\n\x08_divisorB\x07\n\x05_unitB\x0c\n\n_converterB\x05\n\x03_idB\x07\n\x05_nodeB\x0f\n\r_display_name*G\n\x03Qos\x12\t\n\x05UNSET\x10\x00\x12\x10\n\x0c\x41T_MOST_ONCE\x10\x01\x12\x11\n\rAT_LEAST_ONCE\x10\x02\x12\x10\n\x0c\x45XACTLY_ONCE\x10\x03*\x1c\n\x08Operator\x12\x07\n\x03SUM\x10\x00\x12\x07\n\x03\x41VG\x10\x01:N\n\nhomie_node\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x03(\x0b\x32\x17.model.protos.HomieNode:T\n\rderived_field\x12\x1f.google.protobuf.MessageOptions\x18\xd2\x86\x03 \x03(\x0b\x32\x1a.model.protos.DerivedField:Y\n\x0fmapping_options\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\x0b\x32\x1c.model.protos.MappingOptions\x88\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.protos.options_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(homie_node)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(derived_field)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(mapping_options)

  DESCRIPTOR._options = None
  _QOS._serialized_start=556
  _QOS._serialized_end=627
  _OPERATOR._serialized_start=629
  _OPERATOR._serialized_end=657
  _HOMIENODE._serialized_start=78
  _HOMIENODE._serialized_end=180
  _DERIVEDFIELD._serialized_start=183
  _DERIVEDFIELD._serialized_end=339
  _MAPPINGOPTIONS._serialized_start=342
  _MAPPINGOPTIONS._serialized_end=554
# @@protoc_insertion_point(module_scope)
