## sqlite is a good method to use database for medium size apps
## or for prototyping

import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:') #will create the database file
#we can set it to :memory: to store in-ram

c = conn.cursor()   #a cursor is an object that executes sql commands on the connection

c.execute("""create table employees(
            first text,
            last text,
            pay integer
          ) """)
#just sql commands but the types are limited to:
# text, null, integer, real, blob
#creating the table must be done only once otherwise an error
conn.commit() #after doing any changes, we should commit to the db file

c.execute("insert into employees values('mahmoud','mohamed','5001')")
c.execute("insert into employees values('tarek','mohamed','6001')")

c.execute("select * from employees")
print(c.fetchall()) #fetchone(), fetchmany(n)
#returns the list of rows available


conn.commit() #commit changes to the db file


## Employee class
emp1 = Employee('Corey','Schafer',6437)
emp2 = Employee('Bob', 'Linda', 7862)

#Add class members to the db
# we can simply do f-string or .format like:
# c.execute("insert into employees values ('{}','{}',{})".format(emp1.first, emp1.second, emp1.pay))
#This is prone to sql injection
#instead we can use ?
c.execute('insert into employees values (?, ?, ?)', (emp1.first, emp1.last, emp1.pay))
c.execute("select * from employees")
#? is a db api and the execute method takes args for this api
#if we have only one value, we still have to put it inside a tuple ('Tarek', )

print(c.fetchall())

#another way is using a dictionary for more specificity
c.execute("insert into employees values (:first, :last, :pay)",
           {'first': emp2.first,'last': emp2.last, 'pay': emp2.last})
c.execute("select * from employees")
print(c.fetchall())

##it is a good practice to use these approaches for the select where statements

### Practice App
def insert_emp(emp): #pass the employee member 
    with conn:
        c.execute("insert into employees values (:first, :last, :pay)",
           {'first': emp.first,'last': emp.last, 'pay': emp.last})

#we can add functions to update and delete employees 
#we can do bulk inserts and it works with sqlalchemy
conn.close() #like closing a file
