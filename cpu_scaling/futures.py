from concurrent import futures
import random

"""
Futures module provides an easy way to schedule asynchronous tasks

The module currently provides two kinds of executors:
concurrent.futures.ThreadPoolExecutor and concurrent.futures.ProcessPoolExecutor
first one based of threading and second one based of multiprocessing

As expected the ThreadPoolExecutor suffers from the same GIL issues as the threading module
"""


def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)])


# suboptimal ThreadPoolExecutor
# with futures.ThreadPoolExecutor(max_workers=8) as executor:
with futures.ProcessPoolExecutor() as executor:
    futs = [executor.submit(compute) for _ in range(8)]

results = [f.result() for f in futs]

print("Results: %s" % results)
