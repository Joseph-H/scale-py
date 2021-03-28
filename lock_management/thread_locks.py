import threading

stdout_lock = threading.Lock()


def print_something(something):
    with stdout_lock:
        print(something)


t = threading.Thread(target=print_something, args=("hello",))
t.daemon = True
t.start()
print_something("thread started")

# can also use reentrant locks too
# In the case that one of your threads might need to acquire a lock multiple times (e.g. a recursive function)
rlock = threading.RLock()

with rlock:
    with rlock:
        print("Double acquired")
