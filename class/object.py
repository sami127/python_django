# oops
# 1.encapsulation
# 2.inheriatabce
# 3.polymoriphism
# 4.objects


class Vehicle:
    name = ""
    kind = "car"
    color = ""

    def __init__(self):
        self.__price = 100
        print("I am inside init method")

    def description(self):
        desc_str = "%s is a %s %s worth $%d" % (self.name,self.color,self.kind,self.__price)
        return desc_str
    
    def setPrice(self,price):
        self.__price = price

car1 = Vehicle()
car1.name = "Ferrari"
car1.color = "red"
car1.kind = "sports"
car1.__price = 1000000
car1.setPrice(1000000)
print(car1.description())
