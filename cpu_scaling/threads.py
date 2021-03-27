import threading
import random

"""
Threads

If your system does not support multiple processors, the threads will be executed one after another as
scheduled by the operating system. However, if multiple CPUs are available, threads could be scheduled
on multiple processing units, once again as determined by the operating system
"""

"""
def print_something(something):
    print(something)


t = threading.Thread(target=print_something, args=("hello",))
# you can avoid using join by setting the below property
t.daemon = True
t.start()

print("thread started")
# join is needed to ensure no thread is left behind
# t.join()
"""

# below program sums one million random integers eight times, spread across eight threads at the same time
# running it with `time` shows that CPU usage is just above 100% which is not that good
# reason being is that the GIL limits the performance of CPython when executing multiple threads
results = []


def compute():
    results.append(sum(
        [random.randint(1, 100) for i in range(1000000)]))


workers = [threading.Thread(target=compute) for x in range(8)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print("Results: %s" % results)
