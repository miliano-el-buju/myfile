class Person():
    def __init__(self,name,age,idNum):
        self.name=name
        self.age=age
        self.idNum=idNum
    def output(self):
        print("Your name is " +self.name,"and my age is " +self.age,"This is my Id number" +self.idNum)
john=Person('John','33','1285548767284640')

john.output()