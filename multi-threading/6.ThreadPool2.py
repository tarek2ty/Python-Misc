## add different times to see who finished first

import concurrent.futures
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f"sleep for {seconds}s\n")
    time.sleep(seconds)
    return f"DONE SLEEPING {seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    # resutls = [executor.submit(do_something,sec) for sec in secs]
    # for f in concurrent.futures.as_completed(resutls):
    #     print(f.result())
    #this should return only 5 seconds
    results=executor.map(do_something,secs)
    #map returns the threads in the order by which they were started
    for res in results:
        print(res)
    #if one of the functions raised an exception, we would handle it in this iterator
        

        
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} sec")