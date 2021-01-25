class Employee:


    amount = 1.1

    def __init__(self,first,last,email,salary):
        self.first = first
        self.last = last
        self.email = email
        self.salary = salary


    def total_amount(self):
        print(self.salary * self.amount)


class Developer(Employee):

    amount = 1.2



    def __init__(self,first,last,email,salary,prog_lang):
        super().__init__(first,last,email,salary)
        self.prog_lang = prog_lang
        self.is_remote = True


class Manager(Employee):

    amount = 1

    def __init__(self, first, last, email, salary, employers=None):
        super().__init__(first, last, email, salary)
        if employers is None:
            self.employers = []
        else:
            self.employers = employers

    def recruit(self,employer):
        if employer not in self.employers:
            self.employers.append(employer)


    def delete(self,employer):
        if employer in self.employers:
            self.employers.remove('nurjanat')




    def show_employers(self):
        for employer in self.employers:
            print(employer)



class Designer(Employee):


    amount = 1.1

    def __init__(self,first,last,email,salary,portfolio):
        super().__init__(first,last,email,salary)
        if portfolio is None:
            self.portfolio = []
        else:
            self.portfolio = portfolio
            if len(portfolio) > 20:
                Designer.amount = 1.5

    def show_portfolio(self):
        for picture in self.portfolio:
            print(picture)





    def delete(self,portfolio):
        if portfolio in self.portfolio:
            self.portfolio.remove('apple')





    def appending(self,portfolio):
        if portfolio not in self.portfolio:
            self.portfolio.append('yahoo')


    # def __str__(self):
    #     return self.portfolio.append('yahoo')
    #     # return f"{self.name} {self.age}"




emp1 = Employee(first='Maksim',last='Surovkin',email='maksim@gmail.com',salary=4)
emp1.total_amount()

dev1 = Developer(first='Nurjanat',last='Abaeva',email='abaeva@gmail.com',salary=15000,prog_lang='python')
dev1.total_amount()

mng1 = Manager(first='Aigerim',last='Kashkarbekova',email='kashkarbekova@gmail.com',salary=10000,employers=['nurjanat'])
mng1.total_amount()



mng1.recruit('jarkynai')
print(mng1.employers)


mng1.delete('nurjanat')
mng1.show_employers()



dsn1 = Designer(first='Baiel',last='Nurmanbek uulu',email='baiel@gmail.com',salary= 16000,portfolio=['youtube','google','apple','github'])
dsn1.total_amount()

dsn1.delete('apple')
dsn1.show_portfolio()

dsn1.appending('yahoo')
print(dsn1.portfolio)

