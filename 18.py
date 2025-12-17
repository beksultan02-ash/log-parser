class Transport:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name
    
    def move(self):
        print("Transport is moving")
        

class Car(Transport):
    def move(self):
        print("Car is driving")


class Plane(Transport):
    def move(self):
        print("Plane is flying")


toyota = Car(200, "toyota")
airastana = Plane(1000, "Air Astana")

toyota.move()
airastana.move()
