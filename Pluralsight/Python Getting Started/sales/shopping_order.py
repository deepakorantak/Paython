class Order:
    def __init__(self):
        self.option = None
        self.item = None
        self.qty = None

    def get_order(self):
        print("Enter your choice : ")
        print("Enter a <item> <qty>: to add to shopping list")
        print("Enter d <item> <qty>: to delete from shopping list")
        print("Enter q: to quit shopping")
        print("")
        user_input = input()
        self.option = user_input[:1]
        if self.option == "q":
            self.item = ""
            self.qty = ""
        else:
            self.option,self.item,self.qty = user_input.split(" ")
            self.qty = int(self.qty)
         
        



