class Beaver:

    finished_bridges = 0

    def __init__(self,name,age,weight,power):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = power
        if self.age > 11:
            self.power -= 5


    def __str__(self):
        return "{} {}".format(self.name,self.age)
        # return f"{self.name} {self.age}"




    # def building(self,bridge):
    #     if (self.weight * self.power) >= bridge.weight:
    #         self.finished_bridges += 1
    #     else:
    #         print("бобер слишком слаб")


class Bridge:

    def __init__(self,length,weight):
        self.length = length
        self.weight = weight
        self.material = 'tree'



    def building(self,team:list):
        group_power = 0
        for beaver in team:
            group_power += (beaver.weight + beaver.power)
        print(group_power,self.weight+self.length)
        if group_power >= self.weight + self.length:
            print('мост успешно построен')
            Beaver.finished_bridges += 1
        else:
            print("команда слишком слабая выберете другую")


beaver1 = Beaver('Bobrik',5,9,10)
beaver2 = Beaver('Musya',7,4,3)
beaver3 = Beaver('Sam',8,11,14)
beaver4 = Beaver('John',12,12,14)
beaver5 = Beaver('aktan',10,14,14)
beaver6 = Beaver('Trump',9,15,17)
bridge1 = Bridge(length=10,weight=100)

beaver_team = [beaver1,beaver4,beaver3,beaver2,beaver5,beaver6]

bridge1.building(beaver_team)

