import requests
import os

FILE = "links.txt"
DIR = "download"
PREFIX = "material"

def lectures_downloader(name, url):
    # ext = url.strip()[::-1].split('.', 1)[0][::-1]

    r = requests.get(url, allow_redirects=True)

    content_type, ext = r.headers.get('content-type').strip().split('/')
    print(f"content_type: {content_type}; extension : {ext}")

    path = os.path.join(DIR, f"{name}.{ext}")
    open(path, 'wb').write(r.content)
    print(f"Downloaded {name}.{ext}")
    pass



def main():

    if not os.path.exists(FILE):
        open(FILE, 'w').close()
        print(f"Created {FILE} file")
        print(f"Please fill {FILE} file with links")
        exit(0)


    if not os.path.exists(DIR):
        os.makedirs(DIR)

    index = 1
    with open(FILE, 'r') as f:
        for line in f:
            name = f"{PREFIX} - #" + format(index, '02d')
            url = line
            lectures_downloader(name, url)
            index += 1
    

if __name__ == "__main__":
    main()