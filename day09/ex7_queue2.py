#! python3

import threading
import queue
import operator


class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('current job is %s, priority is %s' % (self.description, self.priority))

    # 对当前对象进行比较排序
    def __cmp__(self, other):
        return 1


q = queue.PriorityQueue(maxsize=3)

q.put(Job(3, 'Job_2'))
q.put(Job(1, 'Job_1'))
q.put(Job(10, 'Job_3'))


def process_jobs(q):
    while not q.empty():
        n_job = q.get()
        print('while:', n_job[0], n_job[1])
        q.task_done()


workers = []


def append_threads():
    for i in range(2):
        t = threading.Thread(target=process_jobs, args=(q,))
        workers.append(t)


def run_workers():
    for t in workers:
        t.start()


if __name__ == '__main__':
    q.join()
    append_threads()
    run_workers()
