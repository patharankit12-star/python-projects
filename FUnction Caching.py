# function caching save time that second time run this output 
#use for similar task more time 

# Example 
from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5
# take time all list for 5 seconds
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(3))
print("done for 3")
print(fx(5))
print("done for 5")

# don't take time beacause function caching use thatr remember this
print("second time dont take time deriact excuted ")
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(3))
print("done for 3")
print(fx(5))
print("done for 5")
