#program to illustrate the concept of threading
import threading
import os

def print_cube(number):
    print("Cube: {}".format(number * number * number))

def print_square(number):
    print("Square: {}".format(number * number))

def task1():
    print("Task 1 assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running task 1 : {}".format(os.getppid()))

def task2():
    print("Task2 assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running task 2 : {}".format(os.getpid()))

if __name__ == "__main__":

    print("ID of process running main program {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))
    #create thread
    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")
    # t1 = threading.Thread(target=print_square, args=(10,))
    # t2 = threading.Thread(target=print_cube, args=(10,))

    #start thread1
    t1.start()
    #start thread2
    t2.start()
    #wait until thread1 is finished
    t1.join()
    t2.join()
    print("Done!")