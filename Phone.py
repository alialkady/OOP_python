from Item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, brokenPhone = 0):
        super().__init__(name,price,quantity)
        #restriction
        assert brokenPhone >=0 ,f"broken_phone can't be negative"
        ######
        self.brokenPhone = brokenPhone