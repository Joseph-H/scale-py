import multiprocessing
import time
import cotyledon

"""
A widespread use case is to run long-running, background processes (often called daemons) that
are responsible for scheduling some tasks regularly or processing jobs from a queue.
Cotyledon comes in handy for that, it's designed to run long running processes

This is the basic pattern that is used to implement the Go routines and their channels
"""
# The following example shows an implementation of the common producer/consumer pattern.
# In this pattern, a service fills a queue (the producer), and other services
# (the consumers) consume the jobs to execute them.


class Manager(cotyledon.ServiceManager):
    """
    is in charge of creating the queue object. This queue object is passed to all the services
    """

    def __init__(self):
        super.__init__()
        queue = multiprocessing.Manager().Queue()
        self.add(ProducerService, args=(queue,))
        self.printer = self.add(PrinterService, args=(queue,), workers=2)
        self.register_hooks(on_reload=self.reload)

    def reload(self):
        print("Reloading")
        self.reconfigure(self.printer, 5)


class ProducerService(cotyledon.Service):
    """
    uses the queue and fills it with an incremented integer every second
    """

    def __init__(self, worker_id, queue):
        super.__init__(worker_id)
        self.queue = queue

    def run(self):
        i = 0
        while True:
            self.queue.put(i)
            i += 1
            time.sleep(1)


class PrinterService(cotyledon.Service):
    """
    consume from the queue and print its content
    """
    name = "printer"

    def __init__(self, worker_id, queue):
        super.__init__(worker_id)
        self.queue = queue

    def run(self):
        while True:
            job = self.queue.get(block=True)
            print("I am Worker: %d PID: %d and I print %s"
                  % (self.worker_id, self.pid, job))


Manager().run()
