#try 10 threads
#and add args
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f"sleep for {seconds}s\n")
    time.sleep(seconds)
    print("DONE SLEEPING\n")

#we cannot use join inside the loop
#so we create a list of threads

threads=[]
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)
#we will loop on all threads and make sure they are finished
for thread in threads:
    thread.join()

#it takes one function time to finish all threads
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} sec")