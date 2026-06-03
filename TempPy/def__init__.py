class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        #Initiates the dog instance with name and age
        self.name = name  # Assigns the name argument to the object's name attribute
        self.age = age    # Assigns the age argument to the object's age attribute

    def bark(self):
        """
        An instance method that uses the object's attributes.
        """
        print(f"{self.name} says Woof!")

# Creating a new object automatically calls __init__
my_dog = Dog("Buddy", 3)

print(f"{my_dog.name} is {my_dog.age} years old.") # Output: Buddy is 3 years old.
my_dog.bark()
print(my_dog.species)

