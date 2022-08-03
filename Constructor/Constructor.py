class Person:
    def __init__(self, aname):
        self.name=aname

    def talk(self):
        print(f"Hi I am {self.name}")


john = Person("john smith")
print(john.name)
john.talk()
carl=Person("Carl smith")
print(carl.name)
carl.talk()

