import data_acquisition.scrapping as scrap
import threading
import time
import json

def write_values_json (input_file) :
    with (open("./data_acquisition/data_test.json", "a")) as outpout_file :
        outpout_file.write(json.dumps(scrap.immoweb_scrapping(input_file.readline())))
    pass

threads = list()
maxthreads = 3
smphr = threading.Semaphore(value=maxthreads)

def task(SomeInput):
    smphr.acquire()
    write_values_json(SomeInput)
    time.sleep(2)
    smphr.release()

filename = "./links_acquisition/list_of_results.txt"
with (open(filename, "r")) as input_file :
    threads = [threading.Thread(name="worker/task", target=task, args=(input_file,)) for i in range(0,20)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
pass

'''links = [
    'https://www.immoweb.be/en/classified/penthouse/for-rent/ixelles/1050/10306706',
    'https://www.immoweb.be/en/classified/apartment/for-rent/willebroek/2830/10309521',
    'https://www.immoweb.be/en/classified/house/for-sale/oupeye/4680/10302566',
    'https://www.immoweb.be/en/classified/house/for-sale/antwerpen/2140/10258718'
]

my_list = list()

for link in links :
    my_list.append(scrap.immoweb_scrapping(link))

print(my_list)'''