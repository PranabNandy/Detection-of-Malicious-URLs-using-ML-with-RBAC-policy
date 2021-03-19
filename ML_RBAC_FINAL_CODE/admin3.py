from create_database import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import re
import sqlite3
import datetime
from getpass import getpass
today1=datetime.date.today()


# Define tokenizer
#   The purpose of a tokenizer is to separate the features from the raw data
  
def tokenizer(url):
  """Separates feature words from the raw data
  Keyword arguments:
    url ---- The full URL
    
  :Returns -- The tokenized words; returned as a list
  """
  
  # Split by slash (/) and dash (-)
  tokens = re.split('[/-]', url)
  
  for i in tokens:
    # Include the splits extensions and subdomains
    if i.find(".") >= 0:
      dot_split = i.split('.')
      
      # Remove .com and www. since they are too common
      if "com" in dot_split:
        dot_split.remove("com")
      if "www" in dot_split:
        dot_split.remove("www")
      
      tokens += dot_split
      
  return tokens




def add(id5):
  print("Enter the following details ")
  flag=1
  while(flag==1):
    print("User id of New user : ")
    id2=input()
    db=sqlite3.connect("RABC.db")
    c=db.cursor()
    list1=[(id2)]
    c.execute("Select * from URA where id=?",list1)
    result=c.fetchall()
    if(len(result)==0):
      print("Password of New user : ")
      password2 = getpass()
      print("Name of New user : ")
      name=input()
      print("DOB of New user : ")
      dob=input()
      today1=datetime.date.today();
      c.execute("Select * from ROLE")
      result=c.fetchall();
      l=len(result)
      for i in range(0,l):
        print("Enter {} for \t{} role ".format(result[i][0],result[i][1]))
      ss=int(input())
      list1=[(id2,password2,name,dob,str(today1),"just Created",ss)]
      c.executemany("Insert into URA values(?,?,?,?,?,?,?)",list1)
      db.commit()
      print("Successfully Added new User")
      #db=sqlite3.connect("RABC.db")
      #c=db.cursor()
      list1=["Successfully Added new User",str(today1),id5]
      c.execute("Update URA set log=?,date1=? where id=?",list1)
      db.commit()
      flag=0
      return 1
    else:
      print("User id already exist ")
      return 1




def update(id5):
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  print("User id of the user that you want to update  : ")
  id2=input()
  list1=[(id2)]
  c.execute("Select * from URA where id=?",list1)
  result=c.fetchall();
  if(len(result)==0):
    print("You have entered wrong user id ")
    return 1
  print("Enter the new name ")
  name=input()
  print("Enter new password ")
  password2 = getpass()
  print("Enter new DOB ")
  dob=input()
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  list1=[password2,name,dob,id2]
  c.execute("Update URA set pass=?,name=?,dob=? where id=?",list1)
  db.commit()
  print("Successfully updated")
  list1=["Successfully updated",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
  return 1



def delete(id5):
  print("User id of the user that you want to delete  : ")
  id2=input()
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  list1=[(id2)]
  c.execute("Select * from URA where id=?",list1)
  result=c.fetchall();
  if(len(result)==0):
    print("You have entered wrong user id ")
    return 1
  c.execute("Delete from URA where id=?",list1)
  db.commit()
  print("Successfully Deleted")
  list1=["Successfully Deleted",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
  return 1

def addRole(id5):
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  print("Alredy Existing Role Are as Follows : ")
  print("Id\t Name")
  c.execute("Select * from ROLE")
  result=c.fetchall();
  l=len(result)
  for i in range(0,l):
    print("{}  \t{} ".format(result[i][0],result[i][1]))

  print("List of Permission ")
  print("-" * 90)
  for i in range(1,10):
    idd=i
    #print("iddd:",idd)
    list3=[(idd)]
    c.execute("Select * from PERM where id=?",list3)
    result33=c.fetchall()
    print("Enter {} == {} ".format(result33[0][0],result33[0][1]))
  print("-" * 90)

  
  print("New Role id ")
  a=int(input())
  print("Name of the New Role")
  b=input()

  
  list1=[(a)]
  c.execute("Select * from ROLE where id=?",list1)
  result=c.fetchall();
  if(len(result)!=0):
    print("You have entered Existing Role id ")
    return 1

  l1=[(a,b)]
  c.executemany("Insert into ROLE values(?,?)",l1)
  length=int(input("Enter the Number of Permissions You want to add "))
  for i in range(0,length):
    ppp=int(input("Enter Permission NO : "))
    list9=[(b,ppp)]
    if(ppp>=0 and ppp<=9):
      c.executemany("Insert into PRA values(?,?)",list9)
      '''c.execute("Select * from PRA")
      result99=c.fetchall();
      for j in range(0,len(result99)):
        print("Enter {} == {} ".format(result99[j][0],result99[j][1]))'''
    else:
      print("You have entered wrong Permission Number")
  list9=[(b,0)]
  c.executemany("Insert into PRA values(?,?)",list9)
  print("Role has been Added successfully")
  list1=["Role has been Added successfully",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
  return 1

def delRole(id5):
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  print("Alredy Existing Role Are as Follows : ")
  print("Id\t Name")
  c.execute("Select * from ROLE")
  result=c.fetchall();
  l=len(result)
  for i in range(0,l):
    print("{} \t{} ".format(result[i][0],result[i][1]))
  print("Enter Role id that you want to delete ")
  a=int(input())
  list1=[(a)]
  c.execute("Select * from ROLE where id=?",list1)
  result=c.fetchall();
  if(len(result)==0):
    print("You have entered wrong Role id ")
    return 1
  rrr=result[0][0]
  l1=[(rrr)]
  name33=result[0][1]
  l2=[(name33)]
  
  c.execute("Delete from URA where role=?",l1)
  c.execute("Delete from ROLE where id=?",list1)
  c.execute("Delete from PRA where name=?",l2)
  
  print("Role has been Deleted successfully")
  list1=["Role has been Deleted successfully",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
  return 1


def changeRole(id5):
  print("User id of the user to change the Access Control of that User  : ")
  id2=input()
  db=sqlite3.connect("RABC.db")
  c=db.cursor()

  list1=[(id2)]
  c.execute("Select * from URA where id=?",list1)
  result=c.fetchall();
  if(len(result)==0):
    print("You have entered wrong user id ")
    return 1
  
  c.execute("Select * from ROLE")
  result=c.fetchall();
  l=len(result)
  for i in range(0,l):
    print("Enter {} to change the role as \t{} role ".format(result[i][0],result[i][1]))
  ch=int(input())
  list1=[ch,id2]
  c.execute("Update URA set role=? where id=?",list1)

  print("Role Changed Successfully")
  list1=["Role Changed Successfully",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
  return 1



  


def test(id5,mnb_count,mnb_tfidf,lgs_count,lgs_tfidf,cVec,tVec):
  print("Enter the URL you want to test(like amazon.com,flipcart.com,nitk.ac.in,youtube.com,apple.com,facebook.com etc)")
  str1=input()
  print("your given url is ",str1)
  print('\n')
  t_c2=cVec.transform([str1])
  t_t2=tVec.transform([str1]) 
  model1=mnb_count.predict(t_c2)
  print("Multinomial Naive Bayesian with Count Vectorizer Model predicted the URL as ::::: ",model1)
 
  model2 = mnb_tfidf.predict(t_t2)
  print("Multinomial Naive Bayesian with TF-IDF Model predicted the URL as  :::::: ",model2)
  
  model3=lgs_count.predict(t_c2)
  print("Logistic Regression with Count Vectorizer Model predicted the URL as ::::: ",model3)
    
  model4 = lgs_tfidf.predict(t_t2)
  print("Logistic Regression with TF-IDF Model predicted the URL as ::::: ",model4)
  
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  #list1=["Successfully Tested the URL",str(today1),id5]
  #c.execute("Update URA set log=?,date1=? where id=?",list1)
  today2=datetime.date.today()
  #print(today2)
  d1=str(today2)
  #print(d1)
  list1=["Successfully Tested the URL",d1,id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()

  return 1

def testing2(id5):
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  print("Enter the URL you want to test(like amazon.com,flipcart.com,nitk.ac.in,youtube.com,apple.com,facebook.com etc)")
  str1=input("Write your URL")
  '''print("your given url is ",str)
  print('\n')'''
  #list1=[(id2)]
  '''c.execute("Select * from ROLE")
  result=c.fetchall()
  l=len(result)
  print("Tuple i --> Id \t Role ")
  print("")
  for i in range(0,l):
    print("Tuple {} --> {}\t{} ".format(i,result[i][0],result[i][1]))
  '''
  c.execute("Select * from URA")
  '''result=c.fetchall()
  l=len(result)
  print("Tuple i --> Id \t\t Password \t UserName \t\t DOB \t date1 \t log \t\t\t Role ")
  print("")
  for i in range(0,l):
    l1=[(result[i][6])]
    c.execute("Select * from ROLE where id=?",l1)
    result1=c.fetchall()
    print("Tuple {} --> {}\t{}\t{}\t{}\t{}\t{}\t{}".format(i,result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result1[0][1]))
  '''
  print("Successfully Tested the URL")
  list1=["Successfully Tested the URL",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()

  
def show(id5):
  db=sqlite3.connect("RABC.db")
  c=db.cursor()
  #list1=[(id2)]
  '''c.execute("Select * from ROLE")
  result=c.fetchall()
  l=len(result)
  print("Tuple i --> Id \t Role ")
  print("")
  for i in range(0,l):
    print("Tuple {} --> {}\t{} ".format(i,result[i][0],result[i][1]))
  '''
  c.execute("Select * from URA")
  result=c.fetchall()
  l=len(result)
  print("Tuple i --> Id \t\t Password \t UserName \t\t DOB \t date1 \t log \t\t\t Role ")
  print("")
  for i in range(0,l):
    l1=[(result[i][6])]
    c.execute("Select * from ROLE where id=?",l1)
    result1=c.fetchall()
    print("Tuple {} --> {}\t{}\t{}\t{}\t{}\t{}\t{}".format(i,result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result1[0][1]))
  list1=["Successfully Displayed All Users",str(today1),id5]
  c.execute("Update URA set log=?,date1=? where id=?",list1)
  db.commit()
