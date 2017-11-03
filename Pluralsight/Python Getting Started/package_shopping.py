import sales.shopping_cart,sales.shopping_order
   
exit_shopping = False
cart = sales.shopping_cart.ShoppingCart()

while not exit_shopping:
    o1 = sales.shopping_order.Order()
    o1.get_order()
    if o1.option == "q":
        exit_shopping = True
        break
    result = cart.process_order(o1)
    print(result)    
print(cart)
    

    

