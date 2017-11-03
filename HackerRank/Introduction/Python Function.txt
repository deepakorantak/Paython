import math
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year in range(1900,int(math.pow(10,5))+1):
        if (year % 4 == 0):
            if ( year % 100 == 0 ):
                if (year %  400 == 0):
                    leap = True 
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
            
    
    return leap
    
    
year = int(input())
print(is_leap(year))