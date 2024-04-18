# 2.1 Intermediate Python Object-Oriented Programming (OOP):

# Classes and Objects:

# In Python, everything is an object. You can define your own classes to create objects with attributes and methods.

# Example: Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# Create an object of the Person class
person1 = Person("John", 30)
person1.greet() # Output: Hello, my name is John and I am 30 years old.


# Inheritance:

# You can create a new class that inherits attributes and methods from another class.

# Example: Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(self.name, "is studying.")

# Create an object of the Student class
student1 = Student("Alice", 25, "S12345")
student1.greet() # Output: Hello, my name is Alice and I am 25 years old.
student1.study() # Output: Alice is studying.



# Encapsulation and Polymorphism:

# Encapsulation refers to the bundling of data and methods that operate on the data into a single unit (i.e., a class). Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Example: Encapsulation and Polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Polymorphism
def make_animal_sound(animal):
    animal.make_sound()

# Create objects of different classes
dog = Dog()
cat = Cat()

# Call the same method on different objects
make_animal_sound(dog) # Output: Woof!
make_animal_sound(cat) # Output: Meow!



