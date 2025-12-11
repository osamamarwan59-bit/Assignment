import threading   # importing the threading module
import time        # importing the time module

# function to run for the first thread
def print_1():
    # print starting of the current Thread name
    print("Starting of a thread:", threading.current_thread().name)

    # suspends execution of the current thread for 0.02 seconds
    time.sleep(0.02)

    print("Finishing of a thread:", threading.current_thread().name)

# function to run for the second thread
def print_2():
    # print starting of the current Thread name
    print("Starting of a thread:", threading.current_thread().name)

    # print finishing of the current Thread name
    print("Finishing of a thread:", threading.current_thread().name)

# creating threads
a = threading.Thread(target=print_1, name="Thread-1")
b = threading.Thread(target=print_2, name="Thread-2")

# starting the threads
a.start()  
b.start()
