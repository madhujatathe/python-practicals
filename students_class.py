class student:
    school = "abc school"   # class variable

    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private variable
        print(f"Constructor called for {self.name}")

    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)
        print("School:", student.school)

    def __del__(self):
        print(f"Destructor called for {self.name}")


# Creating objects
s1 = student("raghav", 19)
s2 = student("prachi", 18)

# Access and display
print(s1.name)
s1.show()

# Changing class variable
student.school = "pqr school"

s2.show()

# Deleting objects
del s1
