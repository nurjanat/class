class Car:
    wheels = 4
    def __init__(self,name,year,color,model,is_crashed):
        self.name = name
        self.year = year
        self.color = color
        self.model = model
        self.is_crashed = is_crashed
        self.fuel = 100
        self.run = 0
        self.V = 20
        self.speed = 0
        self.position = 0
        print(f"{self.name} created!")



    def drive_to(self,city,km):
        result = self.V / 100
        result = result * km
        if result < self.fuel:
            self.fuel -= result
            if self.fuel >= 0:
                print(f"{self.name} drive to {city}")
        else:
            print('road so far.')

    def charge(self):
        if self.fuel < 20:
            self.fuel = 100


    def crash(self,another_car):
        if another_car.position == self.position:
            self.is_crashed = True
            another_car.is_crashed= True
            print(f"{self.name} crashed")


class Human:

    def __init__(self,full_name,age,height,weight,nation):
        self.full_name = full_name
        self.age = age
        self.height = height
        self.weight = weight
        self.nation = nation
        self.position = 0
        self.health = 100
        self.is_alive = True

    def move(self):
        self.position += 1

    def accident(self,car,trafficlight):
        if car.position == self.position and trafficlight.green:
            if self.health > 40:
                if 5 <car.speed < 20:
                    self.health -= 20
                elif car.speed > 20:
                    self.health -= 40
            else:
                self.health = 0
                self.is_alive = False

            print(f'{self.full_name} попал в аварию его сбила {car.name} его здоровье {self.health}')




class Trafficlight:
    def __init__(self):
        self.red = False
        self.yellow = False
        self.green = False

    def set_color(self,color:int):
        if color % 2 == 1:
            self.red = True
            self.green = False
            self.yellow = False
        elif color == 'yellow':
            self.yellow = True
            self.green = False
            self.red = False
        elif color % 2 == 0:
            self.green = True
            self.red = False
            self.yellow = True





audi = Car(name = 'AUDI',year = 2021,color = 'grey',model = 'RX 8',is_crashed=False)
bmw = Car(name='BMW',year=2020,color='black',model='x 6',is_crashed=False)
honda = Car(name='HONDA',year=2020,color='black',model='x 6',is_crashed=False)
audi.speed = 50
human1 = Human(full_name='bob',age=22,height=180,weight=80,nation='french')

traffic_light = Trafficlight()


print(traffic_light.red,traffic_light.yellow,traffic_light.green)
for i in range(1,10):
    if human1.health > 0:
        traffic_light.set_color(i)
        human1.accident(audi,traffic_light)


# print(audi.fuel)



human1.accident(audi,traffic_light)
print('Здоровье человека: ',human1.health,human1.is_alive)


