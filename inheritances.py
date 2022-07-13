class Person():
    def __init__(self,name,age,idNum):
        self.name=name
        self.age=age
        self.idNum=idNum
    def output(self):
        print("Your name is " +self.name,"and my age is " +self.age,"This is my Id number" +self.idNum)
class Man():
    def strong(self):
        print("MAN IS STRONG %%%")
        
class Child(Person,Man):
    pass
kid=Child('Johnny','5','2039389489')
kid.output()
kid.strong()
