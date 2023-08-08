# pgm where two consumer threads wait on the producer thread to notify them abt the availability 
# of the resources 

import logging 
import threading 
import time 
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


class availPool(object): 
    def __init__(self): 
        super(availPool, self).__init__()
        self.active=[]
        self.lock= threading.Lock() 
    

    def makeActive(self, name):
        with self.lock: 
            self.active.append(name) 
            logging.debug('Running :%s', self.active) 
    

    def makeInactive(self, name): 
        with self.lock: 
            self.active.remove(name)
            logging.debug('Running : %s', self.active) 


def thread_function(s, pool): 
    logging.debug('Waiting to join the pool') 
    with s: 
        name= threading.current_thread().name
        pool.makeActive(name) 
        time.sleep(1) 
        pool.makeInactive(name) 


pool= availPool() 
s= threading.Semaphore(1) 
for i in range(2): 
    t= threading.Thread(target= thread_function, name= str(i), args=(s, pool))
    t.start() 