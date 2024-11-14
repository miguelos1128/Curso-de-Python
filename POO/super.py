class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello! I am a person. My name is {self.name}")

class Student(Person):
    def __init__(self, name , age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my students ID is {self.student_id}")
student = Student("Ana", 20, "S123")
student.greet()