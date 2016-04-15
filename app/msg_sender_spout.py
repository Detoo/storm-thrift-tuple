from time import sleep
from pyleus.storm import Spout

from message_services.ttypes import MsgType, Message


class MsgSenderSpout(Spout):
    OUTPUT_FIELDS = ['message']

    def initialize(self):
        self.msg_bodies = iter([
            'this is a test message.',
            'this is the second test message.'
        ])

    def next_tuple(self):
        try:
            msg_body = next(self.msg_bodies)
            msg = Message(type=MsgType.TYPE_A, body=msg_body)
            self.log('emitting message: {}'.format(msg))
            self.emit([msg.__dict__], tup_id=hash(msg))
        except StopIteration:
            sleep(10)
            pass


if __name__ == '__main__':
    MsgSenderSpout().run()
