# pgm to check if the thread is still active and is daemon..

import threading 
import time 
import logging 


logging.basicConfig(level= logging.DEBUG,  
                    format='(%(threadName)-10s) %(message)s')



def uf():
    logging.debug('Starting') 
    time.sleep(10)
    logging.debug('Exiting') 



t= threading.Thread(name='demonThread', target=uf)
t.daemon= True 
t.start()
t.join(2) 
print('t.isAlive()', t.is_alive()) 
print('t.isDaemon()', t.isDaemon())