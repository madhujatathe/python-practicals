class student:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def accept(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display(self):
        print("Student name:", self.name)
        print("Student age:", self.age)


# Creating objects
s1 = student()
s2 = student()

print("Enter details for student 1:")
s1.accept()

print("\nEnter details for student 2:")
s2.accept()

print("\nStudent details:")
s1.display()
s2.display()
