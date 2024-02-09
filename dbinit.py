
import sqlite3
conn = sqlite3.connect('library.db')

conn.execute('''CREATE TABLE IF NOT EXISTS USER
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Name VARCHAR NOT NULL,
         Email VARCHAR NOT NULL,
         Password VARCHAR NOT NULL,
         DOB DATE NOT NULL);''')
print("USER table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS STAFF
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Name VARCHAR NOT NULL,
         DOB DATE NOT NULL,
         Email VARCHAR NOT NULL);''')
print("STAFF table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS AUTHOR
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Name VARCHAR NOT NULL,
         DOB DATE NOT NULL);''')
print("AUTHOR table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS BOOK
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Name VARCHAR NOT NULL,
         AuthorID INTEGER NOT NULL,
         AuthorName VARCHAR NOT NULL,
         PUBLISHED DATE,
         GENRE VARCHAR NOT NULL,
         FOREIGN KEY (AuthorID) REFERENCES AUTHOR(ID));''')
print("BOOK table has been created successfully")   

conn.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
          UserID INTEGER NOT NULL,
          BookID INTEGER NOT NULL,
          StartDate DATE NOT NULL,
          DueDate DATE NOT NULL,
          ReturnDate DATE,
          FOREIGN KEY (UserID) REFERENCES USER(ID),
          FOREIGN KEY (BookID) REFERENCES BOOK(iD));''')   
print("TRANSACTIONS table has been created successfully")

conn.close()

#using faker to create dummy data for DB