import pickle
from pyleus.storm import Bolt

from message_services.ttypes import Message


class MsgLoggerBolt(Bolt):
    def process_tuple(self, tup):
        ser_msg = tup.values[0]
        msg = pickle.loads(ser_msg)

        self.log('received message: {}'.format(msg))
        self.ack(tup)


if __name__ == '__main__':
    MsgLoggerBolt().run()
