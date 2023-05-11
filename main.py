import requests
import os

FILE = "lectures.txt"
DIR = "lectures"

def lectures_downloader(name, url):
    ext = url.strip()[::-1].split('.', 1)[0][::-1]
    
    r = requests.get(url, allow_redirects=True)
    if 'video' not in r.headers.get('content-type'): 
        print("Not video type")
        
    if ext != r.headers.get('content-type').replace('video/', ''):
        print("Extension error")

    path = os.path.join(DIR, f"{name}.{ext}")
    open(path, 'wb').write(r.content)
    print(f"Downloaded {name}.{ext}")
    pass



def main():

    if not os.path.exists(DIR):
        os.makedirs(DIR)

    index = 1
    with open(FILE, 'r') as f:
        for line in f:
            name = f"OOP - #" + format(index, '02d')
            url = line
            lectures_downloader(name, url)
            index += 1
    

if __name__ == "__main__":
    main()