#downloading files from an online server is a great candidate for threading
#because the cpu waits for each io operation to finish to start the other
#but threading will make multiple requests

import requests
import concurrent.futures
import time

def download_image(url):
    img_byte = requests.get(url).content
    name = url.split('/')[3] + ".jpg"
    with open(name,'wb') as f:
        f.write(img_byte)
    print(f"{name} was downloaded")


urls=[
    "https://images.unsplash.com/photo-1526779259212-939e64788e3c",
    "https://images.unsplash.com/photo-1505968409348-bd000797c92e",
    "https://images.unsplash.com/photo-1570051008600-b34baa49e751",
    "https://images.unsplash.com/photo-1561816544-21ecbffa09a3",
    "https://images.unsplash.com/photo-1502236876560-243e78f715f7",
]

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image,urls)

#concurrent execution will finish in 11 sec

finish = time.perf_counter()
print(f"finished in {finish-start}s\n")


## Threads is ideal for downloading or waiting in general
## on the other hand, threads is not good if we do computation
## because the cpu will do something actually not just wait

## ALSO, threads can slow down the script because the overhead
## of creating and destroying them.