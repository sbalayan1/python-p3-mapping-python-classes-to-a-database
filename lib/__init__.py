import sqlite3 #imports the sqlite3 module

#before we can create a songs table, we need to create a music database. It's not the job of our song class. Typically the __init__ module will contain variables that will be used by many classes in our program

CONN = sqlite3.connect('db/music.db') #uses the connect method within the sqlite3 module and connects to the provided file. This establishes a connection to SQLITE3 and saves it to a constant. 
#CONN is equal to a hash that contains our connection to the database

CURSOR = CONN.cursor() #CURSOR is a constant that allows us to interact with our database. The cursor() method creates a Cursor object. Cursor objects are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection.
#CURSOR objects are necessary for executing most sql statements

#The CURSOR object gives us access to commands such as 
    #execute() to execute SQL queries


#with these CONSTANTS, we can import them into files that need them!