#---------------------------------VERY IMPORTANT/ after closing this (connection.close()) enter in Terminal python3 sql_lite_beginners.py show new db file

import sqlite3
#---------------------------------create Database--name it gta--add db extension to it to indicate  thats a database--assign db to variable called connection
connection = sqlite3.connect("gta.db")  #we need to close it after tuple release_list

#---------------------------------Cursor object in order to use SQL commands--assigning it to cursor variable for ex

cursor = connection.cursor()        #---in charge  of communicating w/database--

#---------------------------------passing SQL commands in brackets
#---------------------------------executing commands on a cursor object.First columns release year, second..third
#---------------------------------first column expect integer, second expects strig(in SQL text)


cursor.execute("create table gta (release_year integer, release_name text, city text)")   #---executing commands on a cursor object.
#First columns release year, second..third





#---------------------------------Tuple

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]


cursor.executemany ("insert into gta values(?,?,?)", release_list) ###-------??? is our template, second argument is 

for row in cursor.execute("select * from gta"):
    print (row)


print("********************")


#print specific rows--search for a particular row where particular value 
# is stored.Lets select releases that happen inside liberty city
# condition: the column of city will be represented by the dict key of c. 
# follwoed by the dict itself where the key of c corresponds to the value of liberty city


cursor.execute("select * from gta where city=:c", {"c": "Liberty City"}) 
gta_search= cursor.fetchall()

print(gta_search)

#---------------------------------Tuple
connection.close()


#
#cursor.execute("create table cities (gta_city text, real_city text)") #first and sec column
#cursor.execute("insert into cities values(?,?)", ("Liberty City", "New York")) # in the form of a tuplewith 2 items ??
#cursor.execute("select * from cities where gta_city=:c", {"c": "Liberty City"})  
#cities_search = cursor.fetchall()
#print(cities_search)  
