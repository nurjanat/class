class Animal:

    def __init__(self,weight,name,power):
        self.weight = weight
        self.name = name
        self.power = power

    def set_bridge(self,weight_bridge):
        if self.weight >= weight_bridge:
            print(f"{self.name} can to build")
        else:
            print(f"{self.name} can not to build")






class Bridge:

    def __init__(self,len,weight,name):
        self.len = len
        self.name = name
        self.weight = weight




beaver1 = Animal(name='mursik',weight=24,power=0)
beaver2 = Animal(name='barsik',weight=34,power=10)
bridge1 = Bridge(name='golden',weight=240000,len=23)
beaver1.set_bridge(bridge1.weight)