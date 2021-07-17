class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

p1 = Person("John", 36, "Male")
p2 = Person("Kumar", 34, "Male")

print(p1.name)
print(p1.age)
print(p1.gender)

print(p2.name)
print(p2.age)
print(p2.gender)
