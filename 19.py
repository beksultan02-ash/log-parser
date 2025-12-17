class Dog:
    def __init__(self,name):
        self.name = name
    def sound(self):
        return "Bark bark"

class Cat:
    def __init__(self,name):
        self.name = name
    def sound(self):
        return "Meow meow"
    
def animal_sound(animal):
    if hasattr(animal, 'sound'):
        print(animal.sound())
    else:
        print("poshel nahui zaebal rabotai bolshe ne zhalei sebya ne lenis suka")


cat = Cat("Lucky")
dog = Dog("Kira")

animal_sound(cat)
animal_sound(dog)