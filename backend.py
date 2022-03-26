import sqlite3

# Creating Database Connection
def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()


# Creating an Insert Function to ADD some data in database
def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


# Creating a View Function to fetch all the rows of the table
def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows


# Creating a Search Function
def search(title = "", author = "", year = "", isbn = ""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


# Creating a Delete Function
def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id =?", (id,))
    connection.commit()
    connection.close()


# Creating an Update Function
def update(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    connection.commit()
    connection.close()



# To Execute the Function
connect()

# insert("The Ocean", "Neil Dawson", 1981, 822547838)
# insert("Secret Garden", "Rosalia Demore", 1992, 864899713)
# insert("Cosmic Universe", "Mark Albert Simpson", 2002, 924687819)

# delete(2)

# update(4, "Cosmos", "Mark Albert Tyson", 2003, 924811915)

# print(view())

# print(search(author = "Rosalia Demore"))