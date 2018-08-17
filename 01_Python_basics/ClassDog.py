class Farm:
    animals = []

    def __init__(self, inAnimals):
        self.animals = inAnimals

    def get_biggest_number(self):
        max_age = 0
        for animal in self.animals:
            if animal.age > max_age:
                max_age = animal.age
        return max_age


class Dog:
    species = 'mammal'

    # def __init__(self):
    #     self.age = 0
    #     self.name = "Bark"

    def __init__(self, age=2, name="Bark"):
        self.age = age
        self.name = name

    def __str__(self):
        return "Dog: age is "+str(self.age)+", name is "+self.name

    # instance method
    def description(self):
        return "{} age is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


##################################
# TESTS
########################
philo = Dog(6, "Birk")
mikey = Dog()
print(philo)
print(mikey)

# Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

print(philo.speak("Hauuu!"))
print(philo.description())

dogs = [philo, mikey]
farm = Farm(dogs)
print("Max animals age:", farm.get_biggest_number())





