class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)


class DogOne:

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog2 = DogOne("test", 9)

print(dog2.name)
