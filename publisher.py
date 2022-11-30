
import string
import random
import os
import time

# initializing size of string
def get_jobId_and_taskId():
    k = 8
    l = 4
    m = 4
    n = 12

    kth = ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))
    lth = ''.join(random.choices(string.ascii_lowercase + string.digits, k=l))
    mth = ''.join(random.choices(string.ascii_lowercase + string.digits, k=m))
    nth = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))
    res = str(kth + '-' + lth + '-' + mth + '-' + nth)

    return res
from kubemq.queue.message_queue import MessageQueue

from kubemq.queue.message import Message


if __name__ == "__main__":
    while True:
        queue = MessageQueue("lambda-test", "test-queue-client-id2", "host.docker.internal:50000")
        message = Message()
        message.metadata = 'metadata'
        message.attributes = None
        try:
            for i in range(2):
                order = 0
                payload={}
                job_id = get_jobId_and_taskId()
                payload["job_id"]=job_id
                payload["chunk"]=""
                payload["podname"] = str(os.getenv("MY_POD_NAME"))

                for j in range(5):
                    payload["order"] = 0
                    task_id = get_jobId_and_taskId()
                    payload["task_id"] = task_id
                    payload["status"] = "In Progress"

                    for k in range(7):
                        payload["chunk"]=f"chunk{random.randint(0,6)}.log"
                        message.body = f"{payload}".encode('UTF-8')
                        sent = queue.send_queue_message(message)
                        payload["order"] += 1
                        if k == 8:
                            payload["status"] = "Completed"
                        time.sleep(0.25)
            if sent.error:
                print('message enqueue error, error:' + sent.error)
            else:
                print('message sent at: %d ; message Id: %s' % (
                    sent.sent_at,
                    sent.message_id
                            ))
        except Exception as err:
            print('message enqueue error, error:%s'  % (
                    err
                            ))
