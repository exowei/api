# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bitcoin/v1alpha1/bitcoin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bitcoin/v1alpha1/bitcoin.proto',
  package='exowei.bitcoin.v1alpha1',
  syntax='proto3',
  serialized_options=_b('Z\036exowei.io/api/bitcoin/v1alpha1\200\001\001\370\001\001\310\341\036\000\250\342\036\000\360\341\036\000'),
  serialized_pb=_b('\n\x1e\x62itcoin/v1alpha1/bitcoin.proto\x12\x17\x65xowei.bitcoin.v1alpha1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"y\n\x05\x42lock\x12\x34\n\x06header\x18\x01 \x01(\x0b\x32$.exowei.bitcoin.v1alpha1.BlockHeader\x12:\n\x0ctransactions\x18\x02 \x03(\x0b\x32$.exowei.bitcoin.v1alpha1.Transaction\"\x93\x01\n\x0b\x42lockHeader\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x12\n\nprev_block\x18\x02 \x01(\t\x12\x13\n\x0bmerkle_root\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x62its\x18\x05 \x01(\r\x12\r\n\x05nonce\x18\x06 \x01(\r\"\'\n\x08OutPoint\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\"\x82\x01\n\x04TxIn\x12=\n\x12previous_out_point\x18\x01 \x01(\x0b\x32!.exowei.bitcoin.v1alpha1.OutPoint\x12\x18\n\x10signature_script\x18\x02 \x01(\t\x12\x0f\n\x07witness\x18\x03 \x03(\t\x12\x10\n\x08sequence\x18\x04 \x01(\r\")\n\x05TxOut\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x11\n\tpk_script\x18\x02 \x01(\t\"\x8f\x01\n\x0bTransaction\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12,\n\x05tx_in\x18\x02 \x03(\x0b\x32\x1d.exowei.bitcoin.v1alpha1.TxIn\x12.\n\x06tx_out\x18\x03 \x03(\x0b\x32\x1e.exowei.bitcoin.v1alpha1.TxOut\x12\x11\n\tlock_time\x18\x04 \x01(\r\"+\n\x15GetBlockByHashRequest\x12\x12\n\nblock_hash\x18\x01 \x01(\t\"/\n\x17GetBlockByNumberRequest\x12\x14\n\x0c\x62lock_number\x18\x01 \x01(\r\"Q\n\x17ListTransactionsRequest\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12\x12\n\npage_token\x18\x03 \x01(\t\"V\n\x18ListTransactionsResponse\x12:\n\x0ctransactions\x18\x01 \x03(\x0b\x32$.exowei.bitcoin.v1alpha1.Transaction\"7\n\x1bGetTransactionByHashRequest\x12\x18\n\x10transaction_hash\x18\x01 \x01(\t2\xc6\x03\n\x07\x42itcoin\x12\x62\n\x0eGetBlockByHash\x12..exowei.bitcoin.v1alpha1.GetBlockByHashRequest\x1a\x1e.exowei.bitcoin.v1alpha1.Block\"\x00\x12\x66\n\x10GetBlockByNumber\x12\x30.exowei.bitcoin.v1alpha1.GetBlockByNumberRequest\x1a\x1e.exowei.bitcoin.v1alpha1.Block\"\x00\x12y\n\x10ListTransactions\x12\x30.exowei.bitcoin.v1alpha1.ListTransactionsRequest\x1a\x31.exowei.bitcoin.v1alpha1.ListTransactionsResponse\"\x00\x12t\n\x14GetTransactionByHash\x12\x34.exowei.bitcoin.v1alpha1.GetTransactionByHashRequest\x1a$.exowei.bitcoin.v1alpha1.Transaction\"\x00\x42\x32Z\x1e\x65xowei.io/api/bitcoin/v1alpha1\x80\x01\x01\xf8\x01\x01\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='exowei.bitcoin.v1alpha1.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='exowei.bitcoin.v1alpha1.Block.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='exowei.bitcoin.v1alpha1.Block.transactions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=235,
)


_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='exowei.bitcoin.v1alpha1.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='exowei.bitcoin.v1alpha1.BlockHeader.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_block', full_name='exowei.bitcoin.v1alpha1.BlockHeader.prev_block', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merkle_root', full_name='exowei.bitcoin.v1alpha1.BlockHeader.merkle_root', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='exowei.bitcoin.v1alpha1.BlockHeader.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bits', full_name='exowei.bitcoin.v1alpha1.BlockHeader.bits', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='exowei.bitcoin.v1alpha1.BlockHeader.nonce', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=385,
)


_OUTPOINT = _descriptor.Descriptor(
  name='OutPoint',
  full_name='exowei.bitcoin.v1alpha1.OutPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='exowei.bitcoin.v1alpha1.OutPoint.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='exowei.bitcoin.v1alpha1.OutPoint.index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=426,
)


_TXIN = _descriptor.Descriptor(
  name='TxIn',
  full_name='exowei.bitcoin.v1alpha1.TxIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_out_point', full_name='exowei.bitcoin.v1alpha1.TxIn.previous_out_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_script', full_name='exowei.bitcoin.v1alpha1.TxIn.signature_script', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witness', full_name='exowei.bitcoin.v1alpha1.TxIn.witness', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='exowei.bitcoin.v1alpha1.TxIn.sequence', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=559,
)


_TXOUT = _descriptor.Descriptor(
  name='TxOut',
  full_name='exowei.bitcoin.v1alpha1.TxOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='exowei.bitcoin.v1alpha1.TxOut.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pk_script', full_name='exowei.bitcoin.v1alpha1.TxOut.pk_script', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=602,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='exowei.bitcoin.v1alpha1.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='exowei.bitcoin.v1alpha1.Transaction.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_in', full_name='exowei.bitcoin.v1alpha1.Transaction.tx_in', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_out', full_name='exowei.bitcoin.v1alpha1.Transaction.tx_out', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock_time', full_name='exowei.bitcoin.v1alpha1.Transaction.lock_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=748,
)


_GETBLOCKBYHASHREQUEST = _descriptor.Descriptor(
  name='GetBlockByHashRequest',
  full_name='exowei.bitcoin.v1alpha1.GetBlockByHashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='exowei.bitcoin.v1alpha1.GetBlockByHashRequest.block_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=793,
)


_GETBLOCKBYNUMBERREQUEST = _descriptor.Descriptor(
  name='GetBlockByNumberRequest',
  full_name='exowei.bitcoin.v1alpha1.GetBlockByNumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_number', full_name='exowei.bitcoin.v1alpha1.GetBlockByNumberRequest.block_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=842,
)


_LISTTRANSACTIONSREQUEST = _descriptor.Descriptor(
  name='ListTransactionsRequest',
  full_name='exowei.bitcoin.v1alpha1.ListTransactionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='exowei.bitcoin.v1alpha1.ListTransactionsRequest.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='exowei.bitcoin.v1alpha1.ListTransactionsRequest.page_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='exowei.bitcoin.v1alpha1.ListTransactionsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=925,
)


_LISTTRANSACTIONSRESPONSE = _descriptor.Descriptor(
  name='ListTransactionsResponse',
  full_name='exowei.bitcoin.v1alpha1.ListTransactionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='exowei.bitcoin.v1alpha1.ListTransactionsResponse.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=927,
  serialized_end=1013,
)


_GETTRANSACTIONBYHASHREQUEST = _descriptor.Descriptor(
  name='GetTransactionByHashRequest',
  full_name='exowei.bitcoin.v1alpha1.GetTransactionByHashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_hash', full_name='exowei.bitcoin.v1alpha1.GetTransactionByHashRequest.transaction_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1015,
  serialized_end=1070,
)

_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['transactions'].message_type = _TRANSACTION
_BLOCKHEADER.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TXIN.fields_by_name['previous_out_point'].message_type = _OUTPOINT
_TRANSACTION.fields_by_name['tx_in'].message_type = _TXIN
_TRANSACTION.fields_by_name['tx_out'].message_type = _TXOUT
_LISTTRANSACTIONSRESPONSE.fields_by_name['transactions'].message_type = _TRANSACTION
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['OutPoint'] = _OUTPOINT
DESCRIPTOR.message_types_by_name['TxIn'] = _TXIN
DESCRIPTOR.message_types_by_name['TxOut'] = _TXOUT
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['GetBlockByHashRequest'] = _GETBLOCKBYHASHREQUEST
DESCRIPTOR.message_types_by_name['GetBlockByNumberRequest'] = _GETBLOCKBYNUMBERREQUEST
DESCRIPTOR.message_types_by_name['ListTransactionsRequest'] = _LISTTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name['ListTransactionsResponse'] = _LISTTRANSACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetTransactionByHashRequest'] = _GETTRANSACTIONBYHASHREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.Block)
  })
_sym_db.RegisterMessage(Block)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADER,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.BlockHeader)
  })
_sym_db.RegisterMessage(BlockHeader)

OutPoint = _reflection.GeneratedProtocolMessageType('OutPoint', (_message.Message,), {
  'DESCRIPTOR' : _OUTPOINT,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.OutPoint)
  })
_sym_db.RegisterMessage(OutPoint)

TxIn = _reflection.GeneratedProtocolMessageType('TxIn', (_message.Message,), {
  'DESCRIPTOR' : _TXIN,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.TxIn)
  })
_sym_db.RegisterMessage(TxIn)

TxOut = _reflection.GeneratedProtocolMessageType('TxOut', (_message.Message,), {
  'DESCRIPTOR' : _TXOUT,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.TxOut)
  })
_sym_db.RegisterMessage(TxOut)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

GetBlockByHashRequest = _reflection.GeneratedProtocolMessageType('GetBlockByHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKBYHASHREQUEST,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.GetBlockByHashRequest)
  })
_sym_db.RegisterMessage(GetBlockByHashRequest)

GetBlockByNumberRequest = _reflection.GeneratedProtocolMessageType('GetBlockByNumberRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKBYNUMBERREQUEST,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.GetBlockByNumberRequest)
  })
_sym_db.RegisterMessage(GetBlockByNumberRequest)

ListTransactionsRequest = _reflection.GeneratedProtocolMessageType('ListTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSACTIONSREQUEST,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.ListTransactionsRequest)
  })
_sym_db.RegisterMessage(ListTransactionsRequest)

ListTransactionsResponse = _reflection.GeneratedProtocolMessageType('ListTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSACTIONSRESPONSE,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.ListTransactionsResponse)
  })
_sym_db.RegisterMessage(ListTransactionsResponse)

GetTransactionByHashRequest = _reflection.GeneratedProtocolMessageType('GetTransactionByHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONBYHASHREQUEST,
  '__module__' : 'bitcoin.v1alpha1.bitcoin_pb2'
  # @@protoc_insertion_point(class_scope:exowei.bitcoin.v1alpha1.GetTransactionByHashRequest)
  })
_sym_db.RegisterMessage(GetTransactionByHashRequest)


DESCRIPTOR._options = None

_BITCOIN = _descriptor.ServiceDescriptor(
  name='Bitcoin',
  full_name='exowei.bitcoin.v1alpha1.Bitcoin',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1073,
  serialized_end=1527,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBlockByHash',
    full_name='exowei.bitcoin.v1alpha1.Bitcoin.GetBlockByHash',
    index=0,
    containing_service=None,
    input_type=_GETBLOCKBYHASHREQUEST,
    output_type=_BLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockByNumber',
    full_name='exowei.bitcoin.v1alpha1.Bitcoin.GetBlockByNumber',
    index=1,
    containing_service=None,
    input_type=_GETBLOCKBYNUMBERREQUEST,
    output_type=_BLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTransactions',
    full_name='exowei.bitcoin.v1alpha1.Bitcoin.ListTransactions',
    index=2,
    containing_service=None,
    input_type=_LISTTRANSACTIONSREQUEST,
    output_type=_LISTTRANSACTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionByHash',
    full_name='exowei.bitcoin.v1alpha1.Bitcoin.GetTransactionByHash',
    index=3,
    containing_service=None,
    input_type=_GETTRANSACTIONBYHASHREQUEST,
    output_type=_TRANSACTION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BITCOIN)

DESCRIPTOR.services_by_name['Bitcoin'] = _BITCOIN

# @@protoc_insertion_point(module_scope)
