#We want to wait for both threads to finish before executing
#the next part of the code to calculate the time right

import time
import threading

start = time.perf_counter()

def do_something():
    print("sleep for 1s\n")
    time.sleep(1)
    print("DONE SLEEPING\n")
#this function makes the cpu just wait for 1 sec
#IO binding: cpu waits for io operatino to finish

#create a thread Object
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

#start the threads
t1.start()
t2.start()

#now add the join method
t1.join()
t2.join()

#means do not jump to next line until the threads exit

#it takes 1s to finish both threads
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} sec")