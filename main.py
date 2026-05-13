class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


p1 = Phone('iPhone', 1200)

print(p1.brand)
print(p1.get_price())

p1.set_price(1500)

print(p1.get_price())
