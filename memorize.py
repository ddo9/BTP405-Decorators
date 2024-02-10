## Memoization using Closures: 
# Implement a memoization decorator using closures. 
# The decorator should cache the results of a function for particular 
# arguments and return the cached result when the function is called 
# with those arguments again, instead of recomputing it.

import time

def memorization(func):
    results = {}
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        checkResult = results.get((*args, *kwargs))
        if(checkResult == None):
            currResult = func(*args,**kwargs)
            results[(*args, *kwargs)] = currResult
            end = time.perf_counter()
            print(f"Program took {end - start:0.4f} seconds to execute.")
            return currResult
        else:
            end = time.perf_counter()
            print(f"Program took {end - start:0.4f} seconds to execute.")
            return checkResult

            
    return wrapper

@memorization
def say_hello():
    return "Hello!"

@memorization
def loopCount(n):
    countList = []
    for i in range(n):
        countList.append(i)
    return countList

print(say_hello())
loopCount(10000)
loopCount(10000)
loopCount(100000)
loopCount(100000)
