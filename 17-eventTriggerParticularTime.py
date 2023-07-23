# pgm where in a thread waits for a particular event for a particular period of time, once 
# the event is set by the main thread, the thread stops waiting and resumes the execution.. 

import threading 
import time 
import logging 

logging.basicConfig(level= logging.DEBUG, format= '(%(threadName)-10s) %(message)s')


def user_function_waiting_for_event_timeout(e,t): 
    """wait for the event to be set befor doing anything""" 
    logging.debug('user function waiting for event timeout starting...') 
    event_is_set= e.wait(t)
    logging.debug('event set: %s', event_is_set) # will get executed after the event is set ...
    if event_is_set: 
        logging.debug('processing event') 
    else: 
        logging.debug('doing other work')




e= threading.Event()
t1= threading.Thread(name='non block wait for event', target= user_function_waiting_for_event_timeout, args=(e,2)) 
t1.start() 

logging.debug('Waiting before calling Event.set()') 
time.sleep(5)
e.set() # once the even is set all the threads waiting on it will get notified ... 
logging.debug('Event is set')