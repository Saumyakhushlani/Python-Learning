# What is a thread?
# We can imagine thread as a light-weight process.
# So big tasks can be broken down into multiple small threads.

# Why do we need thread?
# We have so many things happening at the same time.
# So we break down each thing to an individual thread.
# And all these threads are executed on different CPU cores (if available).

# ------------------------------
# Import everything from threading module
from threading import *
from time import sleep

# ------------------------------
# Create a class 'hello' which is a subclass of Thread
class hello(Thread):
    # The run() method will be executed when thread is started
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)  # sleep to simulate delay and observe interleaving

# ------------------------------
# Create a class 'hi' which is also a subclass of Thread
class hi(Thread):
    # The run() method will be executed when thread is started
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)  # sleep to simulate delay and observe interleaving

# ------------------------------
# Create objects of both threads
t1 = hello()
t2 = hi()

# -----------------------------------
# Is it possible to run the code of hello and hi simultaneously?
# By default every execution has one thread.
# And that one thread is known as main thread.
# To run them simultaneously, we need to create two different threads.

# How to create two different threads?
# 1. Make your class a subclass of Thread (done above)
# 2. Call start() instead of run()

# -----------------------------------
# Starting both threads
t1.start()   # this will internally call t1.run() in a new thread
t2.start()   # this will internally call t2.run() in another thread

# If we call run() directly, it runs sequentially in main thread.
# But start() will create new threads and run them simultaneously.

# -----------------------------------
# If we want main thread to wait until both threads finish:
t1.join()    # main thread will wait for t1 to complete
t2.join()    # main thread will wait for t2 to complete

# After both threads finish, we can print something:
print("Bye")  # This will print only after both threads are done
