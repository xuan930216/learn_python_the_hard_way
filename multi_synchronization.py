import threading

x = 0

def increament():
    global x
    x += 1

def thread_task(lock):
    
    for _ in range(1000):
        lock.acquire()
        increament()
        lock.release()

def main_task():

    lock = threading.Lock()
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print(x)