
import time
import threading

start = time.perf_counter()

def do_something():
    print("sleep")
    time.sleep(1)
    print("DONE SLEEPING")
#this function makes the cpu just wait for 1 sec
#IO binding: cpu waits for io operatino to finish

do_something()
do_something()      #sitting around waiting
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} sec")