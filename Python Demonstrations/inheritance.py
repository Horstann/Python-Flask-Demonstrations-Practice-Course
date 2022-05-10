class Bird:
    def __init__(self):
        print("Bird class constructor is executing...")

    def whatType(self):
        print("I am a bird.")
    def canWalk(self):
        print("I can walk.")

""" Inheritance """
# Penguin class inherits attributes from Bird class
class Penguin(Bird):
    def __init__(self):
        super().__init__() # Bird class will be constructed here, within Penguin Class
        print("Penguin class constuctor is executing...")
    
    def whoisThis(self):
        print("I am a penguin.")
    def canFly(self):
        print("I can't fly.")
    def canSwim(self):
        print("I can swim.")

""" Polymorphism """
# methods in the child classes Penguin & Parrot have same names
class Parrot(Bird):
    def __init__(self):
        super().__init__()
        print("Parrot class constructor is executing...")
    
    def whoisThis(self):
        print("I am a parrot.")
    def canFly(self):
        print("I can fly.")
    def canSwim(self):
        print("I can't swim.")

def bird_test(bird):
    bird.canFly()
    bird.canSwim()

penguin = Penguin()
penguin.whatType()
penguin.canWalk()
penguin.whoisThis()
penguin.canSwim()

print()
parrot = Parrot()

bird_test(parrot)
bird_test(penguin)

print()

""" Multiple Inheritance """
# Base classes
class Base1:
    def func1(self):
        print("func1() is executing...")

class Base2:
    def func2(self):
        print("func2() is executing...")

class Base3:
    def func3(self):
        print("func3() is executing...")

# Derived class
class Derived(Base1, Base2, Base3):
    def funcDerived(self):
        print("funcDerived() is executing...")

d = Derived()
d.func1()
d.func2()
d.func3()
d.funcDerived()