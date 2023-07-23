# pgm to override the constructor and run() functions of thread 

import threading 
import logging 

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

class SubThreadWithArgs(threading.Thread):

    def __init__(self, group= None, target=None, name=None, args=(), kwargs= None): 

        threading.Thread.__init__(self, group= group, target= target, name=name)
        self.args= args 
        self.kwargs= kwargs 
        return 
    
    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs) 
        return 


t= SubThreadWithArgs(args=(1,), kwargs= {'a':'A', 'b':'B'})
t.start() 
