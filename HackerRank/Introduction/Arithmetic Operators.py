import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a in range(1,int(math.pow(10,10))+1)  and   b in range(1,int(math.pow(10,10))+1)  :
        #print(str(a+b))
        #print(str(a-b))
        #print(str(a*b))
        print(a+b,a-b,a*b,sep='\n')
    	
    	
    
