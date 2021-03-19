import sqlite3
import datetime
def create_db():
    db=sqlite3.connect("RABC.db")
    c=db.cursor()
    c.execute("create table if not exists URA(id text primary key,pass text,name text,dob text,date1 text,log text,role integer)")
    c.execute("create table if not exists ROLE(id integer primary key,name text)")
    c.execute("create table if not exists PRA(name text,id integer)")
    c.execute("create table if not exists PERM(id integer,name text)")
    
    list1=[('admin')]
    c.execute("Select * from URA where id=?",list1)
    result=c.fetchall()
    if(result):
        x=10
    else:
        today1=datetime.date.today()
        list2=[("admin","1234","Admin","20/02/2000",str(today1),"Just Created",1)]
        list3=[("Admin","1234","Admin","20/02/2000",str(today1),"Just Created",1)]
        list4=[("ADMIN","1234","Admin","20/02/2000",str(today1),"Just Created",1)]
        c.executemany("Insert into URA values(?,?,?,?,?,?,?)",list2)
        c.executemany("Insert into URA values(?,?,?,?,?,?,?)",list3)
        c.executemany("Insert into URA values(?,?,?,?,?,?,?)",list4)
        l1=[(1,'admin')]
        l2=[(2,'member')]
        l3=[(3,'user')]
        c.executemany("Insert into ROLE values(?,?)",l1)
        c.executemany("Insert into ROLE values(?,?)",l2)
        c.executemany("Insert into ROLE values(?,?)",l3)
        l1=[('admin',1),('admin',2),('admin',3),('admin',4),('admin',5),('admin',6),('admin',7),('admin',8),('admin',9),('admin',0)]
        l2=[('member',7),('member',8),('member',0)]
        l3=[('user',8),('user',0)]
        c.executemany("Insert into PRA values(?,?)",l1)
        c.executemany("Insert into PRA values(?,?)",l2)
        c.executemany("Insert into PRA values(?,?)",l3)
        l1=[(1,'To Add new User in Database')]
        l2=[(2,'To Update User Data in Database')]
        l3=[(3,'To Delete User Data from Database')]
        l4=[(4,'To Change the Role of the User')]
        l5=[(5,'To Add new the Role in the System')]
        l6=[(6,'To Delete the Role from the System')]
        l7=[(7,'To Train the Model again')]
        l8=[(8,'To Test some URL')]
        l9=[(9,'To Show all Users')]
        l0=[(0,'----> EXIT <----------')]
        c.executemany("Insert into PERM values(?,?)",l1)
        c.executemany("Insert into PERM values(?,?)",l2)
        c.executemany("Insert into PERM values(?,?)",l3)
        c.executemany("Insert into PERM values(?,?)",l4)
        c.executemany("Insert into PERM values(?,?)",l5)
        c.executemany("Insert into PERM values(?,?)",l6)
        c.executemany("Insert into PERM values(?,?)",l7)

        c.executemany("Insert into PERM values(?,?)",l8)
        c.executemany("Insert into PERM values(?,?)",l9)
        c.executemany("Insert into PERM values(?,?)",l0)
    db.commit()

