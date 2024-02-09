from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from orm import Author, Staff, User
import datetime

fake = Faker()
engine = create_engine("sqlite:///library.db", echo=True)

##Loading author onto DB
author_names = []
author_DOBs = []
for i in range(5):
    a_name = fake.name()
    a_dob_str = fake.date()
    a_dob = datetime.date.fromisoformat(a_dob_str)
    author_names.append(a_name)
    author_DOBs.append(a_dob)
    with Session(engine) as session:
        author = Author(
            name = a_name,
            dob = a_dob
        )
        session.add(author)
        session.commit()    


##Loading staff onto DB
staff_names = []
staff_DOBs = []
for i in range(5):
    s_name = fake.name()
    s_dob_str = fake.date()
    s_dob = datetime.date.fromisoformat(s_dob_str)
    staff_names.append(s_name)
    staff_names.append(s_dob)
    s_email = s_name.strip(".").replace(" ","")+"@simpleLibrary.com"
    with Session(engine) as session:
        staff = Staff(
            name = s_name,
            dob = s_dob,
            email = s_email
        )
        session.add(staff)
        session.commit()        

##Loading user Onto DB
#hardcoding a user so that it is easy to test if i ever make a FE client
u_name = "abd lbd"
u_email = "abd@simpleLibrary.com"
u_pass =  "123abd123"
u_dob= datetime.date.fromisoformat("1999-08-12")
with Session(engine) as session:
    user = User(
        name = u_name,
        email = u_email,
        password = u_pass,
        dob = u_dob
    )
    session.add(user)
    session.commit() 


##Loading books onto DB




