import data_acquisition.scrapping as scrap
import threading
import time
import json

def write_values_json (input_file) :
    with (open("./data_acquisition/data_test.json", "a")) as outpout_file :
        start_thread = time.perf_counter() 
        outpout_file.write(json.dumps(scrap.immoweb_scrapping(input_file.readline())))
        print(f"task finished in {time.perf_counter() - start_thread}")
    pass

start_process = time.perf_counter() 
threads = list()
maxthreads = 5
smphr = threading.Semaphore(value=maxthreads)

def task(SomeInput):
    with smphr:
        write_values_json(SomeInput)
        time.sleep(2)

filename = "./links_acquisition/list_of_results.txt"
with (open(filename, "r")) as input_file :
    threads = [threading.Thread(name="worker/task", target=task, args=(input_file,)) for i in range(0,100)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
pass

print(time.perf_counter() - start_process)
