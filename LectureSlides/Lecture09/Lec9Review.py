# # Example 1. 
# class salary(object):
#     def __init__(self, month_salary, interest_rate, increase):
#         self.ms = month_salary
#         self.interest_rate = interest_rate
#         self.increase = increase 

#     def get_money(self):
#         return self.ms * 12 * (1 + self.interest_rate) + self.increase

# my_salary = salary(10000, 0.1, 2000)

# my_salary.get_money()
# # my_salary.money


# # Example 2. 
# # Default argument 
# def add(x=2, y=3):
#     return x + y 

# print(add(1, 2))


# Example 3. 
# Animal
class Animal(object):
    def __init__(self, age, name):
        self.age = age 
        self.name = name 

    def get_age(self):
        return self.age
    def get_name(self):
        return self.name 
    def set_age(self, newage):
        self.age = newage 
    def set_name(self, newname = ""):
        self.name = newname

    def __str__(self):
        return "Animal: " + str(self.name) + ":" + str(self.age)

animal1 = Animal(2, "Alice")
print(animal1.get_age())
print(animal1)

class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "Cat: " + str(self.name) + ":" + str(self.age)

cat1 = Cat(3, "Bob")
print(cat1.get_age())
print(cat1.speak())
print(cat1)


class Person(Animal):
    ... 

class Student(Person):
    ...