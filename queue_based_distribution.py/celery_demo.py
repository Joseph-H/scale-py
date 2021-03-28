import celery
import requests
import tenacity

# celery queue is created that has redis as backend and broker
app = celery.Celery('celery-proj',
                    broker='redis://localhost',
                    backend='redis://localhost')


def do_something(url_to_crawl):
    dic = {}
    r = requests.get(url=url_to_crawl)
    if r.status_code != 200:
        raise RuntimeError
    text = r.text
    dic['data'] = text
    dic['status_code'] = r.status_code
    return dic


@app.task()
def getURL(url_to_crawl):
    # celery task
    @tenacity.retry(wait=tenacity.wait_fixed(5), stop=tenacity.stop_after_attempt(3))
    def do_something_and_retry(url_to_crawl):
        return do_something(url_to_crawl)
    return do_something_and_retry(url_to_crawl)


if __name__ == '__main__':
    urls = ["http://educative.io",
            "http://example.org/", "http://example2ed3d.com"]

    results = []
    for url in urls:
        results.append(getURL.delay(url))

    for result in results:
        print("Task state: %s" % result.state)
        print("Result: %s" % result.get())
        print("Task state: %s" % result.state)
