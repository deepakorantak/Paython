cart = dict()

def get_order():
    print("Enter your choice : ")
    print("Enter a <item> <qty>: to add to shopping list")
    print("Enter d <item> <qty>: to delete from shopping list")
    print("Enter q: to quit shopping")
    print("")
    user_input = input()
    option = user_input[:1]
    if option == "q":
        item = ""
        qty = ""
    else:
        option,item,qty = user_input.split(" ")
        qty = int(qty)

    print(option,item,qty)  
    return (option,item,qty)

def process_order(order):
     option,item,qty = order
     if (option == "a"):
         if (item in cart):
             cart[item] += qty
         else:
             cart[item] = qty
     elif (option == "d"):
         if ((item in cart) and (cart[item] > qty)):             
             cart[item] -= qty
         elif ((item in cart) and (cart[item] <= qty)):
             del cart[item]
         else:
             return (False,"Item not present")
     else:
         return (False,"Invalid option")

     return (True,"Order processed")
    
def main():
    exit_shopping = False
    while not exit_shopping:
        option,item,qty = get_order()    
        if option == "q":
            exit_shopping = True
            break
        result = process_order((option,item,qty))
        print(result)
        print(cart)

if __name__ == '__main__':
    main()
  
     
