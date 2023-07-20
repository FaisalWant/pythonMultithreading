#pgm to create 3 daemon threads, and using the enumerate and join function, wait for the daemon threads to complete execution 


import threading 
import time 
import logging 


logging.basicConfig(level= logging.DEBUG,  
                    format='(%(threadName)-10s) %(message)s')



def uf():
    logging.debug('Starting') 
    time.sleep(10)
    logging.debug('Exiting') 

for i in range(3):
    t= threading.Thread(target=uf)
    t.daemon= True 
    t.start()

main_thread= threading.current_thread()

for t in threading.enumerate():   # gives the list of threads which are running... 
    if t is main_thread:
        continue 
    logging.debug('joining %s', t.name)
    t.join()