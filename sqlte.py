import sqlite3
from company import employee
connection = sqlite3.connect("company.db")



c=connection.cursor()

# c.execute("""create table employ(
#
# first  text,
# last text,
# pay integer
#                      )""")
#
# #c.execute("insert into employ values('raman','singh',500000)")
# c.execute("insert into employ values('raman','singh',400000)")
# c.execute("insert into employ values('raj','kumar',6000)")
# c.execute("insert into employ values('rahul','singh',4500000)")
# c.execute("insert into employ values('kabir','singh',5900000)")
# c.execute("select * from employ ")

emp_1=employee('john','singh',5000)

c.execute("insert into employ values(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)

print(c.fetchall())
connection.commit()

connection.close()

