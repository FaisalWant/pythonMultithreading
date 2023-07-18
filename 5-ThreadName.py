# a pgm to print the default thread name while the thread is executing 
import threading 
import time 

def ug(): 
    print(threading.current_thread().name, 'Starting') 
    time.sleep(2) 
    print(threading.current_thread().name, 'Exiting') 






if __name__ == "__main__":

    w= threading.Thread(target=ug)  # use default name 
    w.start() 