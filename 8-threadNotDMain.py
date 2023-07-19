# pgm - create a thread which is not dependent on the main thread - (daemon thread) 

import logging 
import threading 
import time
import Queue
logging.basicConfig(level=logging.DEBUG, 
					format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
				


def uf(): 
	logging.debug('Starting') 
	time.sleep(4) 
	logging.debug('Exiting') 




##--------------------------------- why Threading?

def basic_worker(queue):
    while True:
        item = queue.get()
        # do_work(item)
        print(item)
        queue.task_done()


def basic():
    # http://docs.python.org/library/queue.html
    queue = Queue.Queue()
    for i in range(3):
         t = threading.Thread(target=basic_worker,args=(queue,))
         t.daemon = True
         t.start()
    for item in range(4):
        queue.put(item)
    queue.join()       # block until all tasks are done
    print('got here')

basic()



if __name__ == '__main__':

	w= threading.Thread(name='daemonThread', target=uf)
	w.daemon=True  # will now have independent flow of execution ... 
	w.start()