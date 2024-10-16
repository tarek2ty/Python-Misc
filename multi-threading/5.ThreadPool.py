## Threadpool is an easier way to execute the multi-processing

import concurrent.futures
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f"sleep for {seconds}s\n")
    time.sleep(seconds)
    return f"DONE SLEEPING {seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    resutls = [executor.submit(do_something,2) for _ in range(10)]
    #the submit method returns a futures object
    
    #as_completed will yield the threads as they finish
    for f in concurrent.futures.as_completed(resutls):
        print(f.result())
    #result method is like join(), wait for comletion

        
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} sec")