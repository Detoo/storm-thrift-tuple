from time import sleep
from pyleus.storm import Spout


class MsgSenderSpout(Spout):
    OUTPUT_FIELDS = ['message']

    def initialize(self):
        self.messages = iter([
            'this is a test message.',
            'this is the second test message.'
        ])

    def next_tuple(self):
        try:
            message = next(self.messages)
            self.log('emitting message: {}'.format(message))
            self.emit([message], tup_id=hash(str(message)))
        except StopIteration:
            sleep(10)
            pass


if __name__ == '__main__':
    MsgSenderSpout().run()
