from pyleus.storm import Bolt

from message_services.ttypes import Message


class MsgLoggerBolt(Bolt):
    def process_tuple(self, tup):
        msg_dict = tup.values[0]
        msg = Message(**msg_dict)

        self.log('received message: {}'.format(msg))
        self.ack(tup)


if __name__ == '__main__':
    MsgLoggerBolt().run()
