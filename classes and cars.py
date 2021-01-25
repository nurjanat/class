class Customers:

    def __init__(self,name,age,email,preference,weight,growth,size,wallet):
        self.name = name
        self.age = age
        self.email = email
        self.preference = preference
        self.weight = weight
        self.growth = growth
        self.size = size
        self.wallet = wallet


    def buy(self, clothes: list, size, color, price):
        for cloth in clothes:
            if size == cloth.size or color == cloth.color and price == cloth.price:
                print('buy it')
            else:
                print("not ok")

    def money(self,price):
        if self.wallet > price:
            self.wallet -= price
            print("you can buy it",self.wallet)
        else:
            print("you can not buy it")


class Cloth:

    def __init__(self,color,name,size,price,section):
        self.name = name
        self.color = color
        self.size = size
        self.price = price
        self.section = section
        self.is_dirty = False
        self.position = 0

    def dirty(self,another_dirty):
        if another_dirty == self.position:
            self.is_duty = True
            print("dirty")




    def __str__(self):
        return "{} {} {}".format(self.color, self.price,self.size)





cloth1 = Cloth(color='black',name='jeans',size=26,price=119,section='pants')
cloth2 = Cloth(color='blue',name='jeans',size=27,price=219,section='pants')
cloth3 = Cloth(color='yellow',name='dress',size=44,price=179,section='dresses')
cloth4 = Cloth(color='pink',name='dress',size=46,price=149,section='dresses')
cloth5 = Cloth(color='white',name='shirt',size=48,price=198,section='shirts')
cloth6 = Cloth(color='beige',name='sweater',size=38,price=99,section='sweaters')
clothes = [cloth1,cloth2,cloth3,cloth4,cloth5,cloth6]


cloth6.dirty(0)


customer1 = Customers(name='Aigerim',age=18,email='aigerim@gmail.com',preference='dresses',weight=45,growth=165,size=42,wallet=15000)
customer2 = Customers(name='aijan',age=18,email='aijan@gmail.com',preference='sweaters',weight=48,growth=156,size=44,wallet=5000)

customer1.buy(clothes=clothes,size=44,color='yellow',price=179)
customer2.money(200)

