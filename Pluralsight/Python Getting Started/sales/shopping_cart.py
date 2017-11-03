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

    def process_order(self,order):
        if (order.option == "a"):
            self.add_cart(order)
        elif (order.option == "d"):
            self.delete_cart(order)  
        else:
             return (False,"Invalid option")
        return (True,"Order processed")

