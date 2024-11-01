class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} y tengo {self.age}")

Person1 = Person("Ana", 30)
Person2 = Person("Mike", 26)

Person1.greet()
Person2.greet()