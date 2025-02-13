#!python
import sqlite3
"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()

query ="""CREATE TABLE if not exists vetcustomerst2 (
    id integer primary key autoincrement,
    name tinytext,
    species tinytext,
    breed tinytext,
    age int,
    gender tinytext,
    sn tinytext,
    oID int);"""
cursor.execute(query)
connection.commit()

cursor.execute('PRAGMA table_info(vetcustomerst2);') #name of table is vetcustomers
print(cursor.fetchall())

data = [
    ['Fluffy','dog','Pomeraniam',5,'m','true',101],
    ['Benjamin','cat','Siberian',8,'m','true',103],
    ['Casey','cat','Siberian',8,'m','true',103],
    ['Friend','cat','Domestic',4,'m','false',102],
    ['Copper','dog','Beagle',12,'m','true',104]]

for i in data:
    query = f"insert into vetcustomerst2 (name,species,oPhoneNum,oID,address,balance) values ('{i[0]}','{i[1]}','{i[2]}',{i[3]},'{i[4]}',{i[5]});"
    #print(query)
    cursor.execute(query)
connection.commit()
query = "select * from vetcustomerst2"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)