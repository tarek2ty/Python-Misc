## Threading can run different tasks concurrently
## Multi-threading does not run operations concurrently
## instead, it runs another part of the code until an io operation finishes


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

#this will start the threads and realize that they are io operations
#so instead of waiting, it jumps to next part in the code
#and come back to them once they exit
#we notice it will print the next line before the threads
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} sec")