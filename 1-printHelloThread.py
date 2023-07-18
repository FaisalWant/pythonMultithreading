# A pgm to create a thread which will print "hello world" on the screen 

import threading 

def uf():
	""" thread uf function """ 
	print ("hello World") 
	return 



if __name__ == "__main__":
	threads=[] 
	t= threading.Thread(target=uf)  # creates the thread 
	threads.append(t) 
	t.start() 
