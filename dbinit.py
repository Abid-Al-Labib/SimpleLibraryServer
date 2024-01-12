
import sqlite3
conn = sqlite3.connect('library.db')

conn.execute('''CREATE TABLE IF NOT EXISTS USER
         (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
         Name VARCHAR NOT NULL, 
         DOB DATE NOT NULL);''')
print("USER table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS STAFF
         (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
         Name VARCHAR NOT NULL,
         DOB DATE NOT NULL,
         Email VARCHAR NOT NULL);''')
print("STAFF table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS AUTHOR
         (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
         Name VARCHAR NOT NULL,
         DOB DATE NOT NULL);''')
print("AUTHOR table has been created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS BOOK
         (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
         Name VARCHAR NOT NULL,
         AuthorID INT NOT NULL,
         AuthorName VARCHAR NOT NULL,
         PUBLISHED DATE,
         GENRE VARCHAR NOT NULL,
         FOREIGN KEY (AuthorID) REFERENCES AUTHOR(ID));''')
print("BOOK table has been created successfully")   

conn.execute('''CREATE TABLE IF NOT EXISTS TRANSACTIONS
          (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
          UserID INT NOT NULL,
          BookID INT NOT NULL,
          StartDate DATE NOT NULL,
          DueDate DATE NOT NULL,
          ReturnDate DATE,
          FOREIGN KEY (UserID) REFERENCES USER(ID),
          FOREIGN KEY (BookID) REFERENCES BOOK(iD));''')   
print("TRANSACTIONS table has been created successfully")

conn.close()

#using faker to create dummy data for DB