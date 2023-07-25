#Pgm where the main thread tries to acquire the lock twice in a sequential Fashion 

import threading 

# lock = threading.Lock() 

# print('FirstTry', lock.acquire())   # will be waiting idefinitely 
# print('secondTry', lock.acquire(0))  #  0 for making it non-blocking



# for sequential locking is to use RLock .

lock = threading.RLock() 

print('FirstTry', lock.acquire())   # will be waiting idefinitely 
print('secondTry', lock.acquire(0))  #  0 for making it non-blocking

