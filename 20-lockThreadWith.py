import logging 
import threading 


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def thread_using_with(lock): 
    with lock: 
        logging.debug('lock acquired via with') 
    

def thread_not_using_with(lock): 
    lock.acquire() 
    try:
        logging.debug('Lock acquired directly')
    
    finally: 
        lock.release() 


lock= threading.Lock() 
w= threading.Thread(target= thread_using_with, args=(lock,)) 
nw= threading.Thread(target= thread_not_using_with, args=(lock,)) 

w.start() 
nw.start() 