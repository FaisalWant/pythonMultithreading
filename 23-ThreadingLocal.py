import logging 
import threading 
import time 
import random
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def display_value(data): 
    try: 
        val= data.value 
    
    except AttributeError: 
        logging.debug('No value yet') 
    
    else: 
        logging.debug('value=%s', val) 



def thread_function(data): 
    display_value(data) 
    data.value= random.randint(1, 100) 
    display_value(data) 

local_data= threading.local()   # local to each thread 

for i in range(2): 
    t= threading.Thread(target=thread_function, args=(local_data,))
    t.start() 
