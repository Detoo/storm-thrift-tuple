from time import sleep
from binascii import b2a_base64

from pyleus.storm import Spout
from thrift.TSerialization import serialize

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
            msg = Message(type=MsgType.TYPE_A, body=msg_body, score=98.7654321)
            ser_msg = b2a_base64(serialize(msg))
            self.log('emitting message: {}'.format(msg))
            self.log('serialized message: {}'.format(ser_msg))
            self.emit([ser_msg], tup_id=hash(msg))
        except StopIteration:
            sleep(10)
            pass


if __name__ == '__main__':
    MsgSenderSpout().run()
