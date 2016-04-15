from pyleus.storm import Bolt


class MsgLoggerBolt(Bolt):
    def process_tuple(self, tup):
        message = tup.values[0]
        self.log('received message: {}'.format(message))
        self.ack(tup)


if __name__ == '__main__':
    MsgLoggerBolt().run()
