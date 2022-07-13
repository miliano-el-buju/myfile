#simple program for age...

print("answer the questions to know how long you lived in this life...? ")
name=input('name: ')
print('What is your age?',(name),'?')
age=int(input('age: '))
# its takes only integer succh as 1,2,3 or -1,-2,-3
days=age*365
minutes=age*525948
seconds=age*31556926

print(name,'Has been alive for',days,'days',minutes,'minutes',seconds,'seconds')
print("Thanks for using my age calculator program")