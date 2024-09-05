class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"My name is {self.name}, I am a {self.gender} aged {self.age} ")

p1 = Person("Kevien", 22, "male")
p1.introduce()