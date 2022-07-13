class Person():
    def __init__(self,name,age,idNum):
        self.name=name
        self.age=age
        self.idNum=idNum
    def output(self):
        print("Your name is " +self.name,"and my age is " +self.age,"This is my Id number" +self.idNum)
        
john=Person('John','33','1285548767284640')        
j=Person('John','33','1285548767284640')
m=Person('Melissa','55','100345345')
p=Person('NBA  ','44','87487878293744')
o=Person('NEVER BROKE AGAIN','190','765763986939663')

j.output()
m.output()
p.output()
o.output()
print(john.output())
print(john.name)
print(john.age)
print(john.age)
print(john.idNum)