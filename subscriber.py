import time

from kubemq.queue.message_queue import MessageQueue
if __name__ == "__main__":
    while True:
        queue = MessageQueue("hello-world-queue", "test-queue-client-id2", "localhost:50000", 1, 1)
        try:
            res = queue.receive_queue_messages()
            if res.error:
                print(
                    "'Received:'%s'" % (
                        res.error
                    )
                )
            else:
                for message in res.messages:
                    print(message.Body)
                    time.sleep(0.25)
        except Exception as err:
            print(
                "'error sending:'%s'" % (
                    err
                )
            )


