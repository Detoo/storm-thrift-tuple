from thrift.TSerialization import deserialize
from pyleus.storm import Bolt

from message_services.ttypes import Message


class MsgLoggerBolt(Bolt):
    def process_tuple(self, tup):
        ser_msg = tup.values[0]
        msg = Message()
        deserialize(msg, ser_msg)

        self.log('received message: {}'.format(msg))
        self.ack(tup)


if __name__ == '__main__':
    MsgLoggerBolt().run()
