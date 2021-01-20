class Human:
    def __init__(self,name,age,nation,gender):
        self.name = name
        self.age = age
        self.nation = nation
        self.health = 100
        self.documents = []
        self.gender = gender
        self.married = False


    def description(self):
        print(self.name,self.nation,self.gender,self.age,self.documents,self.health)


    def damage(self,number):
        self.health -= number
        if self.health <= 0:
            print('пора в больницу')

    def set_documents(self,document):
        # for document in docs:
        #     if document not in self.documents:
        #         self.documents.append(document)

        if document == 'passport' and self.age > 16:
            self.documents.append(document)
        if document == 'visa' and self.age > 18:
            self.documents.append(document)

human1 = Human('Harry Poter',19,'english','male')
human2 = Human('Aigerim',18,'kyrgyz','female')

# human1.description()
# human2.description()
# human1.description()
# human1.damage(101)
# human1.description()
human1.set_documents('visa')


human1.description()