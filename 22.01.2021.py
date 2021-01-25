# list1 = ['red','blue','white',1,2,3,4,5,6]
# for color in list1:
#     print(color)



class Employer:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __add__(self, other):
        return(self.salary + other.salary) / 2


emp1 = Employer(name='Trump',age=74,salary=500)
emp2 = Employer(name='baiden',age=78,salary=600)

print(emp1 + emp2)


