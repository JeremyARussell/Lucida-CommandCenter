#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic,slots
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.protocol.TBase import TBase, TExceptionBase, TTransport


class Iface(object):
  def blahBlah(self):
    pass

  def secondtestString(self, thing):
    """
    Prints 'testString("%s")' with thing as '%s'
    @param string thing - the string to print
    @return string - returns the string 'thing'

    Parameters:
     - thing
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def blahBlah(self):
    self.send_blahBlah()
    self.recv_blahBlah()

  def send_blahBlah(self):
    self._oprot.writeMessageBegin('blahBlah', TMessageType.CALL, self._seqid)
    args = blahBlah_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_blahBlah(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = blahBlah_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def secondtestString(self, thing):
    """
    Prints 'testString("%s")' with thing as '%s'
    @param string thing - the string to print
    @return string - returns the string 'thing'

    Parameters:
     - thing
    """
    self.send_secondtestString(thing)
    return self.recv_secondtestString()

  def send_secondtestString(self, thing):
    self._oprot.writeMessageBegin('secondtestString', TMessageType.CALL, self._seqid)
    args = secondtestString_args()
    args.thing = thing
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_secondtestString(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = secondtestString_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "secondtestString failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["blahBlah"] = Processor.process_blahBlah
    self._processMap["secondtestString"] = Processor.process_secondtestString

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

  def process_blahBlah(self, seqid, iprot, oprot):
    args = blahBlah_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = blahBlah_result()
    try:
      self._handler.blahBlah()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("blahBlah", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_secondtestString(self, seqid, iprot, oprot):
    args = secondtestString_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = secondtestString_result()
    try:
      result.success = self._handler.secondtestString(args.thing)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("secondtestString", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class blahBlah_args(TBase):

  __slots__ = [ 
   ]

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value


class blahBlah_result(TBase):

  __slots__ = [ 
   ]

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value


class secondtestString_args(TBase):
  """
  Attributes:
   - thing
  """

  __slots__ = [ 
    'thing',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'thing', None, None, ), # 1
  )

  def __init__(self, thing=None,):
    self.thing = thing

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.thing)
    return value


class secondtestString_result(TBase):
  """
  Attributes:
   - success
  """

  __slots__ = [ 
    'success',
   ]

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

