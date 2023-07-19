import logging 
import threading 
import time

logging.basicConfig(level=logging.DEBUG, 
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
                


def uf(): 
    logging.debug('Starting') 
    time.sleep(4) 
    logging.debug('Exiting') 



w= threading.Thread(name='uf', target=uf)
w.start()