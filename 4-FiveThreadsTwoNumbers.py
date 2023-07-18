# a pgm to create 5 threads wich executed in parallel, each will add 2 numbers and print the result 
# each thread will have its own copy of user function.

import threading 

def uf(num1, num2):
    """ thread uf function""" 
    print (f'numbers {num1}-{num2}')
    print ('result = %d' %(int(num1) +int(num2)))
    return 




if __name__ == "__main__":
    threads=[]
    for i in range(5): 
        t= threading.Thread(target= uf, args=(2,1)) 
        threads.append(t) 
        t.start() 