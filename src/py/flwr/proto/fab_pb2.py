# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/fab.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x66lwr/proto/fab.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\"(\n\x03\x46\x61\x62\x12\x10\n\x08hash_str\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"Q\n\rGetFabRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08hash_str\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\x04\".\n\x0eGetFabResponse\x12\x1c\n\x03\x66\x61\x62\x18\x01 \x01(\x0b\x32\x0f.flwr.proto.Fabb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.fab_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FAB']._serialized_start=59
  _globals['_FAB']._serialized_end=99
  _globals['_GETFABREQUEST']._serialized_start=101
  _globals['_GETFABREQUEST']._serialized_end=182
  _globals['_GETFABRESPONSE']._serialized_start=184
  _globals['_GETFABRESPONSE']._serialized_end=230
# @@protoc_insertion_point(module_scope)
