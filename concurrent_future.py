#The concurrent.future module is part of standard library which provides a high level api
#for lauching async tasks
#Executor: Executor has two useful concrete subclassesL ThreadPollExecutor and ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from time import sleep

import urllib.request

#first construct a ThreadPoolExecutor with the number of threads we want in the pool
pool = ThreadPoolExecutor(3)

#Then we submitted a task to the thread pool executor
def return_after_5_sec(message):
    sleep(5)
    return message
future = pool.submit(return_after_5_sec, ("hello"))
#future has a method called done which tells us of the future has been resolved
print(future.done())
sleep(5)
print(future.done())

#Both executors have a common method map(), the map method allows multiple calls to a provided function
#passing each item in the iterable to the function
URLS = [
    'http://www.foxnews.com/',
    'http://www.cnn.com/',
    'http://europe.wsj.com/',
    'http://www.bbc.co.uk/'
]
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print("%r page is %d bytes"%(url, len(data)))  