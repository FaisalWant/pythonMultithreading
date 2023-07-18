# pgm creating a thread, officially names it and tries to print the official name of the thread 
import threading 
import time 

def ug(): 
    print(threading.current_thread().name, 'Starting') 
    time.sleep(3) 
    print(threading.current_thread().name, "Exiting") 


def serviceFunction():
    print(threading.current_thread().name, 'Starting') 
    time.sleep(3) 
    print(threading.current_thread().name, 'Exiting') 


if __name__ == "__main__": 
    t= threading.Thread(name= 'serviceFunction', target= serviceFunction)
    w= threading.Thread(name='ug', target=ug) 
    w2= threading.Thread(target=ug) 
    w.start()
    w2.start()
    t.start() 