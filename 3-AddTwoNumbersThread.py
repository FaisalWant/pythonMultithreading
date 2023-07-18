# pgm to create a thread which adds 2 numbers and prints the result

import threading 

def uf(num1, num2): 
    """ thread uf function """ 
    print(f'numbers: {num1},{num2}')
    print('result =%d' %(int(num1) + int(num2)))

    return 





if __name__ == "__main__":
    t= threading.Thread(target=uf, args=(2,3))
    t.start()