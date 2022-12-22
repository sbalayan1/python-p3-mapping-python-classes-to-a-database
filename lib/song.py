from . import CURSOR


# note that in building an ORM, it is convention to pluralize the name of the class to create the name of the table. Therefore the Song class maps to the SONGS table. 
class Song:
    def __init__(self, name, album):
        self.id = None #we initialize a song with an ID attr equal to NONE because a song gets an id attribute when its saved to the database. This leaves it up to the database to assign a songs id attribute and also lets us create song instances without needing an id value. Leaving it up to the database is beneficial here because the database will create unique id's for us
        self.name = name
        self.album = album


    #to map our class to our database table, we need a method that creates a table. This method will be a class method because it's the responsibility of the class itself to create a table that holds all of the songs, not the instance.

    #To "map" our class to a database table, we will create a table with the same name as our class and give that table column names that match the instance attributes of the class. 

    #note we pluralize the class when creating the table. Song => songs
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    
    #now that our create_table method is created, we can now work on SAVING DATA regarding invidual songs into the table. Save() inserts a record into the database. 

    def save(self):
        pass
        sql = """
            INSERT INTO songs (name, album) VALUES (?, ?)
        """
        #note string interpolation won't work because sqlite3 will misinterpret the values. 

        CURSOR.execute(sql, (self.name, self.album))

        #to pass in our name and albums, we use bound parameters. The ? characters act as placeholders. Then when we invoke the execute method, the method will take the arguments passed in and apply them to the question marks. 