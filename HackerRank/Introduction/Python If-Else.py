if __name__ == '__main__':
    n = int(input())
    
    if n in range(1,101):
        res = n % 2
        if res == 0:
            if n in range(1,6):
                print("Not Weird")
            if n in range(6,21):
                print("Weird") 
            if n > 20:
                print("Not Weird")
        else:
            print("Weird")
            
            
    	