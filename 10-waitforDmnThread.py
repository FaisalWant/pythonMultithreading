# pgm to create a daemon thread and from main function, wait for stipulated period to the daemon thread for its completion. 
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