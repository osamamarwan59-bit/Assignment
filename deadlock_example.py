import threading   # importing the threading module
import time        # importing the time module

# Two shared resources (locks)
resource_a = threading.Lock()
resource_b = threading.Lock()

def thread_function_1():
    # Thread 1 locks resource A first
    with resource_a:
        print("Thread 1 acquired resource A")

        # Simulate work
        time.sleep(1)

        print("Thread 1 waiting for resource B")

        # Now tries to lock resource B
        with resource_b:
            print("Thread 1 acquired resource B")

def thread_function_2():
    # Thread 2 locks resource B first
    with resource_b:
        print("Thread 2 acquired resource B")

        # Simulate work
        time.sleep(1)

        print("Thread 2 waiting for resource A")

        # Now tries to lock resource A
        with resource_a:
            print("Thread 2 acquired resource A")

# Create two threads
thread1 = threading.Thread(target=thread_function_1)
thread2 = threading.Thread(target=thread_function_2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
