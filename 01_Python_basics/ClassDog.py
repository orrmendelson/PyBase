class Dog:
    species = 'mammal'

    def __init__(self):
        self.age = 0
        self.sound = "Bark"

    def __init__(self, age=1, sound="Bark"):
        self.age = age
        self.sound = sound

    def __str__(self):
        return "Dog: age is "+str(self.age)+", sound is "+self.sound


dog1 = Dog(6, "Birk")
dog2 = Dog()
print(dog1)
print(dog2)
