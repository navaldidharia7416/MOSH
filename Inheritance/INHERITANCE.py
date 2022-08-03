class Mammal:
    def talk(self):
        print("Talk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def kitty(slef):
        print("I am kitty")


dog1=Dog()
dog1.talk()
mammal=Mammal()
mammal.talk()
cat1=Cat()
cat1.kitty()
