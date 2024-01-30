from Item import Item
from Phone import Phone

# item1 = Item("phone",1000,5)
# item2 = Item("laptob",2000,5)
# item3 = Item("cable",10,5)
# item4 = Item("Mouse",50,5)
# item5 = Item("Keyboard",75,5)
# print(item1.price)
# # here you can see the diffrence between class attribute and instance attribute
# item1.apply_discount()
# #print(item1.price)
#
# item2.pay_rate = 0.7
# item2.apply_discount()
# #print(item2.price)
##################################
# Item.instnciate_from_csv()
#
# print(Item.isInteger(2))

phone1 = Phone("nokia",500,5,0)
phone1.name = "samsung"
phone1.quantity = -5
print(phone1.quantity)



