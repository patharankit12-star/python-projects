''''import multiprocessing
import requests

def DOwnloadfile(url ,name):
    print(f"Starting Downloading{name}")
    response = requests.get(url)
    open(f"file12{name}.jpg",
"wb").write(response.content)
    print(f"Finishing  Downloading{name}")


url = "https://picsum.photos/200/300"
pros = []

for i in range(5):
   DOwnloadfile(url , i)'''
   #p=multiprocessing.Process(target=DOwnloadfile,args=(url , i))
   #p.start()
   #pros.append(p)

#for p in pros:
 #  p.join()




# wondefull spped for download file 
import threading
import requests
import time

def download_file(url, name):
    print(f"Starting Download {name}")
    response = requests.get(url)
    with open(f"File{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Download {name}")

def main():
    url = "https://picsum.photos/200/300"
    threads = []
    start_time = time.time()

    
    for i in range(20):
        t = threading.Thread(target=download_file, args=(url, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"All downloads finished in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()