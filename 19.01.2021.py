class Dog:
    def __init__(self,name,poroda,age):
        self.name = name
        self.poroda = poroda
        self.age = age
        print(f"{self.name} родился !")


    def take(self):
        print(f"{self.name} принес!")

    def jump(self):
        print(f'{self.name} подпрыгнула')



dog1 = Dog('hatiko','haski',10)
dog2 = Dog('strelka','common',6)
dog1.take()
dog1.jump()