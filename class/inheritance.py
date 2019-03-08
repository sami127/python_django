class Bird:
    #parant class
    #base class
    def __init__(self):
        print("this is bird")
    
    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    # Child class
    #derived claas
    def __init__(self):
        print("this is Penguin")
    
    def whoisThis(self):
        print("Bird")
    
    def run(self):
        print("run faster")

p = Penguin()
p.whoisThis()
p.swim()
p.run()

