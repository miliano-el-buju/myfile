dic={'Toyota': ('Camry', 'Yaris', 'Cariner e'), 'Cylinder': ('V12', 'V8', 'V6', 'V4'), 'Colour': ('Blue', 'BLACK', 'WHITE'), 'Benz': ('ML550', 'C300', 'ML320', 'ML350', 'ML450', 'ML500', 'C300', 'C250')}
dic["Toyota"]='Camry','Yaris','Cariner e'
dic["Cylinder"]='V12','V8','V6','V4'
dic["Colour"]='Blue','BLACK','WHITE'
dic["Benz"]='ML550','C300','ML320','ML350','ML450','ML500','C300','C250'
print("BEFORE DELETION")
print(dic)
print("AFTER DELETION")
del dic['Cylinder']
print(dic)