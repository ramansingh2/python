from tabulate import tabulate

mydata=[('raman','up',10),
        ('rohan','hydrabad',8),
        ('rahul','bihar',7),
        ('raj','mp',6)]

headers=['name','city','score']

print(tabulate(mydata,headers=headers,tablefmt='grid'))