class ShoppingCart:
    def __init__(self):
        self._list = dict()

    def add_cart(self,order):
        if (order.item in self._list):
            self._list[order.item] += order.qty
        else:
            self._list[order.item] = order.qty
        return (True,"Order processed")

    def delete_cart(self,order):
        if ((order.item in self._list) and (self._list[order.item] > order.qty)):
            self._list[order.item] -= order.qty
        elif ((order.item in self._list) and (self._list[order.item] <= order.qty)):
            del self._list[order.item]
        else:
            return (False,"Item not present")       
        return (True,"Order processed")

    def __repr__(self):
        return " The cart contents: {0}".format(self.__dict__["_list"])

    def __str__(self):
        return " Str The cart contents: {0}".format(self.__dict__["_list"])

class Order:
    def __init__(self,option,item,qty):
        self.option = option
        self.item = item
        self.qty = qty

    def process_order(self):
        if (self.option == "a"):
            cart.add_cart(self)
        elif (self.option == "d"):
            cart.delete_cart(self)  
        else:
             return (False,"Invalid option")
        return (True,"Order processed")

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
     
    return Order(option,item,qty)

   
exit_shopping = False
cart = ShoppingCart()

while not exit_shopping:
    o1 = get_order()    
    if o1.option == "q":
        exit_shopping = True
        break
    result = o1.process_order()
    print(result)    
print(cart)
    

    

