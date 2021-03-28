## Queue-based architecture

Looking at basic architecture, it is composed of two elements: a queue that stores jobs and workers that consume the jobs from a queue, process them and send the result to another destination.

Some tools to implement this is RQ and Celery
