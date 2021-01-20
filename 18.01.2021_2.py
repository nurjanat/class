class Planet:

    def __init__(self,name,size,color):
        self.name = name
        self.size = size # big middle small
        self.color = color
        self.humanity = True
        self.oxygen = True
        self.water = False
        self.population = True
        self.temp = 0

    def set_humanity(self):
        if self.humanity:
            self.humanity = False
            self.oxygen = False
        else:
            self.humanity = True

    def set_population(self,quantity):
        if self.population:
            self.humanity = True
            self.population = True
            self.population += quantity
        else:
            self.humanity = False


    def set_water(self):
        if self.size == 'middle' or self.size == 'great':
            self.water = True
        else:
            self.water = False
        if self.water:
            self.burger = True
        else:
            self.burger = False

planet = Planet('Maxim','middle','black')
print(planet.name,planet.color)
planet.set_humanity()
print(planet.humanity)
planet.set_humanity()
print(planet.humanity)
planet.set_water()
print(planet.water)
planet.set_population(50)
print(planet.population)