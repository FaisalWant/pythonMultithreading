import threading 

def uf():
	""" thread uf function """ 
	print ("hello World") 
	return 



if __name__ == "__main__":
	threads=[] 
	t= threading.Thread(target=uf) 
	threads.append(t) 
	t.start() 
