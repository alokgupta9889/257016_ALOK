DBMS: Database Management System



Definition: A database is an organized collection of data that is stored and managed so it can be easily accessed, updated, and retrieved when needed.



Simple Definition

A database is a place where data is stored in a structured way so that computers can quickly find and use it.



Key Points:

It stores data in tables, rows, and columns (in most cases).



It allows adding, editing, deleting, and retrieving data efficiently.



It is managed by DBMS (Database Management System) like MySQL, Oracle, SQL Server, etc.



Example:

A school database may store:



Student information



Teacher records



Class schedules



Marks and attendance





Types of Database:  ✅ 1. Relational Database



Stores data in tables (rows \& columns).



Uses SQL for querying.



Very structured and consistent.



Examples: MySQL, Oracle, PostgreSQL, SQL Server



✅ 2. NoSQL Database



Stores unstructured or semi-structured data.



Does not use traditional tables.



Highly scalable.



Types include:



Document Database (MongoDB)



Key-Value Store (Redis)



Column-Oriented (Cassandra)



Graph Database (Neo4j)



✅ 3. Hierarchical Database



Data arranged in a tree-like structure (parent–child).



Oldest form of database.



Example: IBM IMS



✅ 4. Network Database



Data organized in a graph.



A child can have multiple parents.



Example: IDMS



✅ 5. Object-Oriented Database



Data stored as objects, just like in OOP languages (Java, C++).



Examples: ObjectDB, db4o



✅ 6. Distributed Database



Data is stored on multiple computers/locations.



Appears as one single database to the user.



Examples: Google Spanner, Apache Cassandra



✅ 7. Cloud Database



Hosted on cloud platforms.



Accessible via the internet.



Examples: Amazon RDS, Firebase, Azure SQL Database



✅ 8. Centralized Database



All data stored in a single location.



Easy to manage, but risk of failure is higher.



✅ 9. Operational (OLTP) Database



Used for day-to-day operations.



Fast insert, update, delete operations.



✅ 10. Data Warehouse (OLAP)



Used for analytics \& reporting.



Stores huge amounts of historical data.



CODE:

CREATE TABLE STUDENTS(

 Student1D varchar(100),Age int,city varchar(100));



CODE:

CREATE TABLE student(

  student\_1d INT PRIMARY KEY,

  name VARCHAR(50),

  age INT,

  gender VARCHAR(10),

  course VARCHAR(50));



CODE:

CREATE TABLE EMPLOYEE (

empID INTEGER PRIMARY KEY,

name TEXT NOT NULL,

  dept TEXT NOT NULL

);-- create





-- insert

INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');

INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');

INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');

INSERT INTO EMPLOYEE VALUES (0004, 'Sumit','Cameraman');

INSERT INTO EMPLOYEE VALUES (0005, 'Alok','saler');



-- fetch

SELECT \* FROM EMPLOYEE WHERE dept = 'Sales';



desc EMPLOYEE;

SELECT name FROM EMPLOYEE;



CODE FOR FIVE PLAYERS:

 CREATE TABLE Players (

    PlayerID INT PRIMARY KEY,

    PlayerName VARCHAR(50),

    Age INT,

    Country VARCHAR(50),

    Sport VARCHAR(50)

);



INSERT INTO Players (PlayerID, PlayerName, Age, Country, Sport)

VALUES

(1, 'Virat Kohli', 35, 'India', 'Cricket'),

(2, 'Lionel Messi', 37, 'Argentina', 'Football'),

(3, 'Rohit Sharma', 38, 'India', 'Cricket'),

(4, 'Cristiano Ronaldo', 40, 'Portugal', 'Football'),

(5, 'PV Sindhu', 30, 'India', 'Badminton');





SELECT \* FROM Players;

 

desc PLAYERS;



SELECT name FROM PLAYERS





###### **CODE:**

###### 

###### **CREATE TABLE EMPLOYEE (**

###### **empID INTEGER PRIMARY KEY,**

###### **name TEXT NOT NULL,**

###### **dept TEXT NOT NULL**

###### **);-- create**

###### 

###### 

###### **-- insert**

###### **INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');**

###### **INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');**

###### **INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');**

###### **INSERT INTO EMPLOYEE VALUES (0004, 'Sumit','Cameraman');**

###### **INSERT INTO EMPLOYEE VALUES (0005, 'Alok','saler');**

###### 

###### 

###### 

###### **delete from EMPLOYEE where empID = 2;**

###### **SELECT \* FROM EMPLOYEE;**



#### **DDL(Data Manipulation Language)**

1. ###### Create
2. ###### Alter: to change in the existing table
3. ###### Drop: Remove the table
4. ###### truncate: Remove the table

######  

#### **DML**(**Data** **Manipulation** **Language**)

1. ###### **Select**
2. ###### **Update**
3. ###### **Insert**
4. ###### **Delete**

### 

### CODE:

###### 

###### CREATE TABLE EMPLOYEE (

###### empID INTEGER PRIMARY KEY,

###### name TEXT NOT NULL,

######   dept TEXT NOT NULL

###### );-- create

###### 

###### 

###### -- insert

###### INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');

###### INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');

###### INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');

###### INSERT INTO EMPLOYEE VALUES (0004, 'Sumit','Cameraman');

###### INSERT INTO EMPLOYEE VALUES (0005, 'Alok','saler');

###### INSERT INTO EMPLOYEE VALUES (0006, 'Shivam','Teacher');

###### INSERT INTO EMPLOYEE VALUES (0007, 'Aman', 'Teacher');

###### 

###### SELECT \* from EMPLOYEE where empId >=0002 and empId <= 0005;































 

