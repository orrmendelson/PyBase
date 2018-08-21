class Farm:
    animals = []

    def __init__(self, in_animals):
        self.animals = in_animals

    def get_oldest_animal(self):
        max_age = 0
        for animal in self.animals:
            if animal.age > max_age:
                max_age = animal.age
        return max_age

    def hungry_status(self):
        hungry_num = 0
        for animal in self.animals:
            if animal.is_hungry:
                hungry_num += 1
        return hungry_num == len(self.animals)

    def speak(self, sound):
        for animal in self.animals:
            print("  ",animal.speak(sound))


class Dog:
    species = 'mammal'
    is_hungry = True

    # def __init__(self):
    #     self.age = 0
    #     self.name = "Bark"

    def __init__(self, name="Bark", age=2):
        self.age = age
        self.name = name

    def __str__(self):
        return "Dog: age is "+str(self.age)+", name is "+self.name

    def eat(self):
        self.is_hungry = False

    # instance method
    def description(self):
        return "{} age is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# ######## Inheritance of Dog: ##################
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# ######## Inheritance of Dog: ##################
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# ######## Inheritance of Dog: ##################
class OtherBreed(Dog):
    species = 'reptile'


# #################################
# TESTS
# #######################
print("\nObjects tests:")
dog1 = Dog("Jake", 7)
dog2 = Dog("Doug", 4)
dog3 = Dog("William", 5)
dog4 = Dog()
print(dog1)
print(dog2)

# Access the instance attributes
print("{} is {} and {} is {}.".format(dog1.name, dog1.age, dog2.name, dog2.age))

# Is Philo a mammal?
if dog1.species == "mammal":
    print("{0} is a {1}!".format(dog1.name, dog1.species))

print(dog1.speak("Hauuu!"))
print(dog1.description())
# #################################
dogs = [dog1, dog2, dog3, dog4]
farm = Farm(dogs)
print("\nFarm:")
print("Max animals age:", farm.get_oldest_animal())
print("All farm animals are hungry?", farm.hungry_status())
print("dog1 eats...", dog1.eat())
print("All farm animals are hungry?", farm.hungry_status())
print("Farm speak:")
farm.speak("Miau")

# #################################
print("\nInheritance:")
# create inheriting class
russelDog = RussellTerrier()
print(russelDog.run(34))

# ####################################################
# Child classes inherit attributes and behaviors from the parent class
child1 = Bulldog("Jim", 12)
print(child1.description())

# Child classes have specific attributes and behaviors as well
print(child1.run("slowly"))

# child is an instance of Dog()? Yes
print("instance of child is an instance of parent: ", isinstance(child1, Dog))

parent1 = Dog("Julie", 100)
print("instance of class is instance of class: ", isinstance(parent1, Dog))

child2 = RussellTerrier("Johnny Walker", 4)
print("instance of sibling 1 Class is instance of 2nd sibling Class? : ", isinstance(child2, Bulldog))

# print("instance of parent is instance of child? : ", isinstance(parent1, child1))
# -->    TypeError: isinstance() arg 2 must be a type or tuple of types

otherBreed = OtherBreed()
print("otherBreed: override parent member value to:", otherBreed.species)

