#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from lucidaservice.ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def create(self, LUCID, spec):
    """
    Parameters:
     - LUCID
     - spec
    """
    pass

  def learn(self, LUCID, knowledge):
    """
    Parameters:
     - LUCID
     - knowledge
    """
    pass

  def infer(self, LUCID, query):
    """
    Parameters:
     - LUCID
     - query
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def create(self, LUCID, spec):
    """
    Parameters:
     - LUCID
     - spec
    """
    self.send_create(LUCID, spec)
    self.recv_create()

  def send_create(self, LUCID, spec):
    self._oprot.writeMessageBegin('create', TMessageType.CALL, self._seqid)
    args = create_args()
    args.LUCID = LUCID
    args.spec = spec
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_create(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = create_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def learn(self, LUCID, knowledge):
    """
    Parameters:
     - LUCID
     - knowledge
    """
    self.send_learn(LUCID, knowledge)
    self.recv_learn()

  def send_learn(self, LUCID, knowledge):
    self._oprot.writeMessageBegin('learn', TMessageType.CALL, self._seqid)
    args = learn_args()
    args.LUCID = LUCID
    args.knowledge = knowledge
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_learn(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = learn_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def infer(self, LUCID, query):
    """
    Parameters:
     - LUCID
     - query
    """
    self.send_infer(LUCID, query)
    return self.recv_infer()

  def send_infer(self, LUCID, query):
    self._oprot.writeMessageBegin('infer', TMessageType.CALL, self._seqid)
    args = infer_args()
    args.LUCID = LUCID
    args.query = query
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_infer(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = infer_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "infer failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["create"] = Processor.process_create
    self._processMap["learn"] = Processor.process_learn
    self._processMap["infer"] = Processor.process_infer

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_create(self, seqid, iprot, oprot):
    args = create_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = create_result()
    try:
      self._handler.create(args.LUCID, args.spec)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("create", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_learn(self, seqid, iprot, oprot):
    args = learn_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = learn_result()
    try:
      self._handler.learn(args.LUCID, args.knowledge)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("learn", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_infer(self, seqid, iprot, oprot):
    args = infer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = infer_result()
    try:
      result.success = self._handler.infer(args.LUCID, args.query)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("infer", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class create_args:
  """
  Attributes:
   - LUCID
   - spec
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'LUCID', None, None, ), # 1
    (2, TType.STRUCT, 'spec', (lucidatypes.ttypes.QuerySpec, lucidatypes.ttypes.QuerySpec.thrift_spec), None, ), # 2
  )

  def __init__(self, LUCID=None, spec=None,):
    self.LUCID = LUCID
    self.spec = spec

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.LUCID = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.spec = lucidatypes.ttypes.QuerySpec()
          self.spec.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('create_args')
    if self.LUCID is not None:
      oprot.writeFieldBegin('LUCID', TType.STRING, 1)
      oprot.writeString(self.LUCID)
      oprot.writeFieldEnd()
    if self.spec is not None:
      oprot.writeFieldBegin('spec', TType.STRUCT, 2)
      self.spec.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.LUCID)
    value = (value * 31) ^ hash(self.spec)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class create_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('create_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class learn_args:
  """
  Attributes:
   - LUCID
   - knowledge
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'LUCID', None, None, ), # 1
    (2, TType.STRUCT, 'knowledge', (lucidatypes.ttypes.QuerySpec, lucidatypes.ttypes.QuerySpec.thrift_spec), None, ), # 2
  )

  def __init__(self, LUCID=None, knowledge=None,):
    self.LUCID = LUCID
    self.knowledge = knowledge

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.LUCID = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.knowledge = lucidatypes.ttypes.QuerySpec()
          self.knowledge.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('learn_args')
    if self.LUCID is not None:
      oprot.writeFieldBegin('LUCID', TType.STRING, 1)
      oprot.writeString(self.LUCID)
      oprot.writeFieldEnd()
    if self.knowledge is not None:
      oprot.writeFieldBegin('knowledge', TType.STRUCT, 2)
      self.knowledge.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.LUCID)
    value = (value * 31) ^ hash(self.knowledge)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class learn_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('learn_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class infer_args:
  """
  Attributes:
   - LUCID
   - query
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'LUCID', None, None, ), # 1
    (2, TType.STRUCT, 'query', (lucidatypes.ttypes.QuerySpec, lucidatypes.ttypes.QuerySpec.thrift_spec), None, ), # 2
  )

  def __init__(self, LUCID=None, query=None,):
    self.LUCID = LUCID
    self.query = query

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.LUCID = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.query = lucidatypes.ttypes.QuerySpec()
          self.query.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('infer_args')
    if self.LUCID is not None:
      oprot.writeFieldBegin('LUCID', TType.STRING, 1)
      oprot.writeString(self.LUCID)
      oprot.writeFieldEnd()
    if self.query is not None:
      oprot.writeFieldBegin('query', TType.STRUCT, 2)
      self.query.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.LUCID)
    value = (value * 31) ^ hash(self.query)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class infer_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('infer_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
