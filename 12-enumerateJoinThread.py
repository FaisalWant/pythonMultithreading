# pgm for using enumerate and join for thread 

import threading 
import time 
import logging 


logging.basicConfig(level= logging.DEBUG,  
                    format='(%(threadName)-10s) %(message)s')



def uf():
    logging.debug('Starting') 
    time.sleep(10)
    logging.debug('Exiting') 


t= threading.Thread(target=uf)
t.daemon= True 
t.start()

main_thread= threading.current_thread()

for t in threading.enumerate():   # gives the list of threads which are running... 
    if t is main_thread:
        continue 
    logging.debug('joining %s', t.name)
    t.join()