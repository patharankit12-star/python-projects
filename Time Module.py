# Example
import time
def usingwhile():
    i = 0
    while i<20:
        i = i + 1
        print(i)

def usingfor():
    for i in range(21):
        print(i)

init = time.time()
usingwhile()
print(time.time() - init)
init = time.time()
usingfor()
print(time.time() - init)
# return time in second form

print(4)
time.sleep(3)
print("This is printed after 3 seconds")

t=time.localtime()
nowtime=time.strftime("%Y-%m-%d %H:%M:%S" ,t)
print(nowtime)