import random
import multiprocessing

"""
Since multithreading is not a perfect scalability solution because of GIL,
processes offer a better alternative.
"""

# the example below shares no global state and uses multiprocessing to
# fork all the processes over the CPUs
"""
def compute(results):
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))


with multiprocessing.Manager() as manager:
    results = manager.list()
    workers = [multiprocessing.Process(target=compute, args=(results,))
               for x in range(8)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print("Results: %s" % results)
"""
# Pool offers a mechanism to express the above code in a functional manner
# The pool starts processes on-demand and takes care of reaping them when done.
# They are also reusable, reducing the usage of the fork system call, which is quite costly.


def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


# Start 8 workers
pool = multiprocessing.Pool(processes=8)
print("Results: %s" % pool.map(compute, range(8)))
