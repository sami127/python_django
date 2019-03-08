class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can not swim")

class Penguin:
    def fly(self):
        print("Penguin can not fly")
    
    def swim(self):
        print("Penguin can swim")
    
#common interface
def flying_test(obj):
    obj.fly()

p = Parrot()
pen = Penguin()


flying_test(p)
flying_test(pen)

