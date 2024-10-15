import base64
import os
import csv

def convert(path):
    try:
        with open(path,'rb') as img:
            encoded = base64.b64encode(img.read()).decode('utf-8')
        return encoded
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as e:
        print(f"an error {e} has occured")
        return None
    
dir = 'images'
with open("images_converted.csv", 'w') as file:
        pass
for img in os.listdir(dir):
    con = convert(f'{dir}/{img}')
    html_xpath = [(img, f"<img src='data:image/png;base64, {con}' />")]
    with open("images_converted.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerows(html_xpath)
