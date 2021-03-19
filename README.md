
# Detection of Malicious URLs using ML with Role Base Access Control Policy

Link of the video which demonstrate the working Principle Of the Project

https://drive.google.com/file/d/1iMP-7zWGrULcO_CjZ9Pfj4_KPs2kG3pk/view?usp=sharing


<--------------------------------------------------------------------------------------------------------------------------------->


Entire project is developed in Python language with some set of available libraries and here SQLite3 is used as Database.

First you need to install the Python compiler (version above 3.0 ).

Before running the Program in Python Shell (i.e Python IDLE ) please install the following Libraries though pip installation Process 

 	pandas, numpy, matplotlib, sklearn, random, re, sqlite3, datetime, getpass, seaborn
	
[ Note: Don’t run the Program in Python Command Line ]

Ex:

	python get-pip.py   (if you don’t have pip)
	pip install --upgrade pip (To upgrade pip)
	pip install pysqlite3    (for windows)
	pip install pandas   (for windows)
	py -m pip install numpy (for windows) 
	pip install matplotlib (for windows)
	pip install scipy (for windows)
	pip install scikit-learn (for windows)
	
[ For Ubuntu use pip3 ]
	
<--------------------------------------------------------------------------------------------------------------------------------->

To train the model we need dataset.

In our case, Dataset is present in ‘URL2.csv’ file . 

We need to set the path of the Dataset file in program . <h4>In  RBAC.py file , there is a line 

url_df = pd.read_csv(r'C:\Users\PRANAB\Downloads\URL2.csv')   

Please set the path of the dataset according to your system 'C:\Users\PRANAB\Downloads\URL2.csv'
which is present in  RBAC.py file.

[ For Ubuntu path will be ‘/home/pranab/Downloads/URL2.csv’ ] </h4>

<--------------------------------------------------------------------------------------------------------------------------------->

 <h4> Then Run the RBAC.py file. It will take approximate 2 min to train all 4 models. Whenever a Model training will complete then it show a pop up regarding the training result. Please close the pop up every time to proceed further .
	

For the first time a database RBAC.db will be created . The table inside the  RBAC.db  are URA,ROLE,PRA,PERM.

</h4> 

To visualize the database table you can install SQLite3 Database Manager.  [ It is not manditary ]


After the training process application will ask for Credential for authentication.

The User Id and Password for Admin user is

User Id=Admin

Password=1234

Then the permission of the Admin will be visible . 

------------------------------------------------------------------------------------------

Enter 1 == To Add new User in Database 

Enter 2 == To Update User Data in Database 

Enter 3 == To Delete User Data from Database 

Enter 4 == To Change the Role of the User 

Enter 5 == To Add new the Role in the System 

Enter 6 == To Delete the Role from the System 

Enter 7 == To Train the Model again 

Enter 8 == To Test some URL 

Enter 9 == To Show all Users 

Enter 0 == ----> EXIT <---------- 

------------------------------------------------------------------------------------------





<--------------------------------------------------------------------------------------------------------------------------------->

There are already 3 roles in the system i.e admin,user,member.

User role has only Permission 8.

Member Role has Permission 7 & Permission 8.

Then Create New Roles, Users and assign an user with role.

In our system user can create any kind of role through a good combination of 9 permissions. So set of Roles in our application is not fixed . Based on the requirement , Roles can be created and deleted but you can not the change the permission of the existing role. In that case, first you need to create the new Role then assign the required users to that newly created role and delete the old role.

<--------------------------------------------------------------------------------------------------------------------------------->

Basically 2 kinds of actions we can perform with these model object which are as follows

 	 Test whether a URL is malicious or not 
	
	 Train the model again by changing some Hypermeters
	
 In this project we have 2 hypermeters one is the alpha factor of Multinomial Naïve Bayesian and another is percentage of test data i.e it splits the dataset into 2 parts i.e training dataset and test dataset. In our system, we have a dataset of size 444321 having a good combination of Normal URLs and Malicious URLs.
 
<--------------------------------------------------------------------------------------------------------------------------------->


![Methodology](/Image/1.jpg)

**Summary ==>**

i)Data Gathering  
ii)Data Preparation (Vectorizing  the Data with a user defined Tokenizer Function  )   
iii)Chose a Classificatoin Model (Multinomial Naive Bayes and Logistic Regression )   
iv)Model Training  
v) Model Evaluation  
vi)Hyper-parameter Traing   
vii)Deploy The Model    

The model accepts the combination of malicious and non-malicious urls as input.  
                                                                          

![Methodology](/Image/100.jpg)

**Role Base Access Control Policy **

![Methodology](/Image/101.jpg)

**Our Design Priciple**

![Methodology](/Image/102.jpg)

**Core Priciple of the Project**

![Methodology](/Image/103.JPG)
