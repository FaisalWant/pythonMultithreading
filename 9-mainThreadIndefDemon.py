# pgm Create a daemon thread.. From the main thread function, wait indefinitely for the daemon thread to complete execution.
import threading 
import time 
import logging 


logging.basicConfig(level= logging.DEBUG,  
                    format='(%(threadName)-10s) %(message)s')



def uf():
    logging.debug('Starting') 
    time.sleep(2)
    logging.debug('Exiting') 



t= threading.Thread(name='demonThread', target=uf)
t.daemon= True 
t.start()
t.join()  # main was blocked indefinitely for the thread to get over
