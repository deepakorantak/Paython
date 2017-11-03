add = lambda x,y:x+y

def calculate(function,x,y):
	return function(x,y)

def print_result(item):
    for i in item:      
        yield i

res = 1
list_res = []
for i in range(1,6):
    list_res.append(res)   
    res = calculate(add,res,i)



    







