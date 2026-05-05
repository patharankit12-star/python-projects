
# Download from internet ,all file downloading same time
import threading
import time
from concurrent.futures import ThreadPoolExecutor
#Indicates some task being done 

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2 - time1 )


time3 = time.perf_counter()
t1 = threading.Thread(target = func,args=[4])
t2 = threading.Thread(target = func,args=[2])
t3 = threading.Thread(target = func,args=[1])
# start in background and work all parameter after all compalte all excuted 
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time4 = time.perf_counter()
print(time4 - time3)


def poolingdemo():
 with ThreadPoolExecutor(max_workers=1) as executor:
    future1= executor.submit(func ,4)
    future2= executor.submit(func ,2)
    future3= executor.submit(func ,1)
    print(future1.result())
    print(future2.result())
    print(future3.result())
    l = [ 3, 5,1,4]
    results = executor.map(func , l)
    for result in results:
       print(result)



poolingdemo()