## Timer Decorator:
# Write a decorator function called timer that calculates the time taken 
# for a function to execute and prints the duration. It should be able to 
# decorate any function and print the time taken for execution.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Program took {end - start:0.4f} seconds to execute.")
        print("")
    return wrapper

@timer
def say_hello():
    print("Hello!")

@timer
def loopCount(n):
    for i in range(n):
        print(i, end=" ")
    print("")

say_hello()
loopCount(100)