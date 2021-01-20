class Cat:

    def __init__(self,size,weight):
        self.size = size
        self.weight = weight
        self.position = 0
        self.power = 0
        self.damage = 0
        self.exp = 0
        print('кот успешно создан')


    def  description(self):
        print(f"размер:{self.size},вес:{self.weight},позиция:{self.position},сила:{self.power},урон:{self.damage}")



    def set_weight(self,weight):
        if weight == 'available':
            self.power += 1
            self.exp += 1
            print('кот летит')
        elif weight == "not available":
            print("вес не позволяет кошке взлететь")



    def move(self):
        self.position += 1


    def run(self):
        self.position = self.position + 10
        print("побежал")



cat1 = Cat('s',14)
cat1.set_weight("not available")
cat1.run()
cat1.description()



