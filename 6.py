import threading
import time

def print_hello(name):
    for _ in range(5):
        print(f"Hello, {name}")
        time.sleep(1)

def print_hi(name):
    for _ in range(5):
        print(f"Hi, {name}")
        time.sleep(1)

# Get user input for names
name_hello = input("Enter a name for 'Hello' thread: ")
name_hi = input("Enter a name for 'Hi' thread: ")

# Create two threads with user input
thread_hello = threading.Thread(target=print_hello, args=(name_hello,))
thread_hi = threading.Thread(target=print_hi, args=(name_hi,))

# Start the threads
thread_hello.start()
thread_hi.start()

# Wait for both threads to finish
thread_hello.join()
thread_hi.join()
