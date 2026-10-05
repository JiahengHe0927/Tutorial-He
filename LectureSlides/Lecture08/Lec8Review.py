# # Example 1. 
# Ana = {
#     "Age": 18,
#     "College": "Imperial",
#     "Subject": "Computer Science"
# }

# Bob = {
#     "Age": 20,
#     "College": "Oxford",
#     "Subject": "Mathematics"
# }

# # 1. Construction
# # 2. Change attribute
# # 3. Delete
# def people():
#     ... 

# def change_age(people):
#     ...

# def salary(people):
#     ...

# # Same object, different instances
# Ana = people(18, "Imperial", "Computer Science")
# Bob = people(20, "Oxford", "Mathematics")

# Ana.change_age(20)
# Bob.change_age(22)

# # Object (called student)
# class Student(object):
    
#     def __init__(self, name, age, college, subject):
#         self.name = name
#         self.age = age 
#         self.college = college
#         self.subject = subject

#     def __str__(self):
#         return "Name:" + str(self.name) + "\nAge:" + str(self.name) + "\nCollege:" + str(self.college) + "\nSubject:" + str(self.subject)

#     def compare_age(self, other_student):
#         if self.age > other_student.age:
#             print(self.name, "is older than", other_student.name)
#         elif self.age < other_student.age:
#             print(other_student.name, "is older than", self.name)
#         else:
#             print("They are the same age")

# # Instance (called Ana and Bob)
# Ana = Student('Ana', 18, "Imperial", "Computer Science")
# Bob = Student('Bob', 20, "Oxford", "Mathematics")
# Chelsea = Student('Chelsea', 16, "Cambridge", "Biology")

# Ana.compare_age(Bob)

# print(Ana)

# Example 2. 
# Create a new type
class Coordinate(object):
    
    # define attributes and construction
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        if self.x < other.x:
            return True 
        elif self.x > other.x:
            return False 
        else: 
            return self.y < other.y 

    # Creating a method
    def distance(self, other_point):
        x_diff = (self.x - other_point.x)**2
        y_diff = (self.y - other_point.y)**2
        return (x_diff + y_diff)**0.5

# Create an instance
c = Coordinate(3.0, 4.0)
d = Coordinate(0, 0)
e = Coordinate(1, 2)

# # Wrong example (the method must be used with the class instance)
# length = distance(c, d)
# length = c.distance(d)
# print(length)

# length = Coordinate.distance(c, d)

# print(c, d)

# c.__add__(e)
# print(c + e)

# c2 = Coordinate(3, 4)
# print(c == c2)
# print(c == c)

# e2 = Coordinate(1, 1)
# print(e < c)
# print(e < e2)
