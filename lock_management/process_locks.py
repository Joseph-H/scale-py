import multiprocessing
import time

stdout_lock = multiprocessing.Lock()


def print_cat():
    # Add some randomness by waiting a bit
    time.sleep(0.1)
    # without this, the cats would be jumbled up sometimes
    with stdout_lock:
        print(" /\\_/\\")
        print("( o.o )")
        print(" > ^ <")


with multiprocessing.Pool(processes=3) as pool:
    jobs = []
    for _ in range(5):
        jobs.append(pool.apply_async(print_cat))
    for job in jobs:
        job.wait()
