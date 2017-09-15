#! python3

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print('running task', self.name)
        time.sleep(3)


t1 = MyThread('t1')
t2 = MyThread('t2')

t1.start()
t2.start()
