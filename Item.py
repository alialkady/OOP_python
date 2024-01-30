import csv
class Item:
    #class attribute
    pay_rate = 0.8

    def __init__(self,name: str,price: float,quantity =0):
       #some restrictions
       assert price >=0, f"price can't be negative"
       assert quantity >=0, f"quantity can't be negative"

       #assign parameters
       self.__name = name # here's this attribute became private and couldn't change from outside
       self.__price =price
       self.quantity = quantity

    #that's read only method to access  attribute ###getter
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
    #setter
    @name.setter
    def name(self,value):
        print("your are setting \n")
        self.__name = value
    @price.setter
    def price(self,value):
        print("your are setting \n")
        self.__price=value

    def calculate_total_price(self):
        return self.__price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    @classmethod
    def instnciate_from_csv(cls):
        with open("text.csv")as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(name=item.get("name"),
                 price = float(item.get("price")),
                 quantity= int(item.get("quantity")))

    @staticmethod
    def isInteger(num):
        if isinstance(num,float):
            return  num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False