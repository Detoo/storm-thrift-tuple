from binascii import a2b_base64

from thrift.TSerialization import deserialize
from pyleus.storm import Bolt

from message_services.ttypes import Message


class MsgLoggerBolt(Bolt):
    def process_tuple(self, tup):
        buf = a2b_base64(tup.values[0])
        msg = Message()
        deserialize(msg, buf)

        self.log('received message: {}'.format(msg))
        self.ack(tup)


if __name__ == '__main__':
    MsgLoggerBolt().run()
