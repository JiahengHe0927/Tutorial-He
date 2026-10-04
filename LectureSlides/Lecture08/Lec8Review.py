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

# Object (called student)
class Student(object):
    
    def __init__(self, name, age, college, subject):
        self.name = name
        self.age = age 
        self.college = college
        self.subject = subject

    def compare_age(self, other_student):
        if self.age > other_student.age:
            print(self.name, "is older than", other_student.name)
        elif self.age < other_student.age:
            print(other_student.name, "is older than", self.name)
        else:
            print("They are the same age")

# Instance (called Ana and Bob)
Ana = Student('Ana', 18, "Imperial", "Computer Science")
Bob = Student('Bob', 20, "Oxford", "Mathematics")
Chelsea = Student('Chelsea', 16, "Cambridge", "Biology")

Ana.compare_age(Bob)


# Example 2. 
# Create a new type
class Coordinate(object):
    
    # define attributes and construction
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    # Creating a method
    def distance(self, other_point):
        x_diff = (self.x - other_point.x)**2
        y_diff = (self.y - other_point.y)**2
        return (x_diff + y_diff)**0.5

# Create an instance
c = Coordinate(3, 4)
d = Coordinate(0, 0)

# # Wrong example (the method must be used with the class instance)
# length = distance(c, d)
length = c.distance(d)
print(length)

length = Coordinate.distance(c, d)