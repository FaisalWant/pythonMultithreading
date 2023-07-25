# pgm which creates 2 threads which does the following without conflict: 
# 1. Acquire the lock, increment the counter value and release the lock 

import threading 
import logging 
import time
logging.basicConfig(level= logging.DEBUG, format= '(%(threadName)-10s) %(message)s')


class Counter(object): 
    def __init__(self, start=0): 
        self.lock= threading.Lock()
        self.value= start 
    
    def increment(self): 
        logging.debug('Waiting for lock') 
        self.lock.acquire()
        try: 
            logging.debug('Acquired lock')
            self.value= self.value+1 
        
        finally: 
            self.lock.release() 



def userFunction(c):
    logging.debug('Starting') 
    time.sleep(3) 
    c.increment()
    logging.debug('Exiting') 


counter= Counter() 
for i in range(2): 
    t= threading.Thread(target=userFunction, args=(counter,))
    t.start() 


logging.debug('Waiting for userfunction threads') 

main_thread= threading.current_thread() 
for t in threading.enumerate():
    if t is not main_thread: 
        t.join() 

logging.debug('Counter: %d', counter.value) 
