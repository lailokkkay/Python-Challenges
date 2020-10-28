import math

class Planet:
    gravitationalConstant = 6.6743 * 10 **(-11)
    def __init__(instance, mass, radius):
        instance.mass = float(mass)
        instance.radius = float(radius)
    def EscapeVelocity(instance):
        return math.sqrt((float(2) * Planet.gravitationalConstant * instance.mass) / instance.radius)

newPlanet = Planet(input("Mass : "),input("Radius : "))
print(newPlanet.EscapeVelocity())
