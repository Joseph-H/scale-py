import futurist
from futurist import waiters
from futurist import periodics
import random
"""
Futurist is an abstraction over futures that offers fine-grained control over
the execution of your threads and processes

Some things that you can do:
- manage queue size
- schedule functions to run periodically
"""


def compute():
    return sum(
        [random.randint(1, 100) for i in range(10000)])


with futurist.ThreadPoolExecutor(max_workers=8) as executor:
    futs = [executor.submit(compute) for _ in range(8)]
    print(executor.statistics)

results = waiters.wait_for_all(futs)
print(executor.statistics)

print("Results: %s" % [r.result() for r in results.done])

# periodically run functions


@periodics.periodic(1)
def every_one(started_at):
    print("1: %s" % (time.time() - started_at))


w = periodics.PeriodicWorker([
    (every_one, (time.time(),), {}),
])


@periodics.periodic(4)
def print_stats():
    print("stats: %s" % list(w.iter_watchers()))


w.add(print_stats)
w.start()
