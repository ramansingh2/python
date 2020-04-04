import sqlite3

dbase=sqlite3.connect('sqdata.db')
c=dbase.cursor()
print('data base opoened ')

c.execute(''' create table  if not exists emp(
    id int primary key not null,
    name text not null,
    division text not null,
    stars int not null
    
    
    
    )''')
print('table created')

# c.execute("insert into emp values(1,'raklman','soft',55)")
# c.execute("insert into emp values(2,'majn','skoft',58)")
# c.execute("insert into emp values(3,'n','softj',75)")
# c.execute("insert into emp values(4,'man','sofot',55)")
dbase.commit()
print(c.fetchall())
dbase.close()

print('data base closedd')



