class Person():
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

person1 = Person("Michael", 3.8, "CS")
print(person1.name)
print(person1.gpa)
print(person1.major)

print(person1.on_honor_roll())
