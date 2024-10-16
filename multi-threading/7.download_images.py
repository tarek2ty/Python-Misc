import requests
import time


urls=[
    "https://images.unsplash.com/photo-1526779259212-939e64788e3c",
    "https://images.unsplash.com/photo-1505968409348-bd000797c92e",
    "https://images.unsplash.com/photo-1570051008600-b34baa49e751",
    "https://images.unsplash.com/photo-1561816544-21ecbffa09a3",
    "https://images.unsplash.com/photo-1502236876560-243e78f715f7",
]

start = time.perf_counter()
for url in urls:
    img_byte = requests.get(url).content
    name = url.split('/')[3] + ".jpg"
    with open(name,'wb') as f:
        f.write(img_byte)
    print(f"{name} was downloaded")

#sequential execution will finish in 16 sec

finish = time.perf_counter()
print(f"finished in {finish-start}s\n")






