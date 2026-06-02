import streamlit as st
import pyperclip

assignments = {
    "1" : '''CREATE DATABASE Krishna;
USE Krishna;
Create table Student:
CREATE TABLE Student(
 RollNo INT(10) PRIMARY KEY,
 Name VARCHAR(35), Class VARCHAR(30), Marks INT(10)
);
Insert records in the table:
INSERT INTO Student VALUES
 (1701, 'Krishna Sarovar', 'BCA', 81),
 (1702, 'Dinesh Jadhav', 'BBA', 75),
 (1703, 'Mahesh Patil', 'B.Com', 74),
 (1704, 'Nagesh Kale', 'Bsc', 72),
 (1705, 'Dipak Sonawane', 'BBA', 79),
 (1706, 'Rishikesh Bherde', 'B.Com', 70);
 Create table Emp.
CREATE TABLE Emp(
 Emp_id INT(10) PRIMARY KEY,
 EName VARCHAR(35),
 Department VARCHAR(30),
 Designation VARCHAR(30), Jdate DATE, Salary INT(40));
Insert records in the table.
INSERT INTO Emp VALUES
 (1, 'Krishna Sarovar', 'IT', 'Programmer', '2023-01-15', 55000),
 (2, 'Dinesh Jadhav', 'HR', 'Manager', '2022-06-10', 70000),
 (3, 'Mahesh Patil', 'Sales', 'Executive', '2025-06-01', 45000),
 (4, 'Nagesh Kale', 'IT', 'Programmer', '2021-03-20', 60000),
 (5, 'Dipak Sonawane', 'Finance', 'Analyst', '2024-09-05', 48000);
 Create table Employee.
CREATE TABLE Employee(
 Emp_id INT(10) PRIMARY KEY,
 EName VARCHAR(35),
 DOB DATE,
 Department VARCHAR(30),
 Designation VARCHAR(30), Jdate DATE, Salary INT(40));
Insert records in the table.
INSERT INTO Employee VALUES
 (1, 'Krishna Sarovar', '1998-05-12', 'Sales', 'Executive', '2022-03-01', 28000),
 (2, 'Dinesh Jadhav', '1995-08-20', 'IT', 'Programmer', '2020-07-15', 35000),
 (3, 'Mahesh Patil', '2000-11-30', 'Sales', 'Manager', '2023-01-10', 22000),
 (4, 'Nagesh Kale', '1993-02-14', 'Finance', 'Analyst', '2018-06-05', 40000),
 (5, 'Dipak Sonawane', '1997-07-25', 'IT', 'Developer', '2021-09-20', 31000),
 (6, 'Rishikesh Bherde', '1999-03-18', 'HR', 'Executive', '2024-04-01', 26000);
 reate table Department.
CREATE TABLE Department(
 Dept_id INT(10) PRIMARY KEY,
 DName VARCHAR(35),
 Emp_id INT(10), City VARCHAR(30), FOREIGN KEY
 (Emp_id) REFERENCES Employee(Emp_id) );
Insert records in the table.
INSERT INTO Department VALUES
 (1, 'IT', 2, 'Mumbai'), (2, 'Sales', 1, 'Delhi'),
 (3, 'Sales', 3, 'Delhi'), (4, 'Finance', 4, 'Pune'),
 (5, 'IT', 5, 'Mumbai'), (6, 'HR', 6, 'Delhi');
 
 Create table Books.
CREATE TABLE Books(
 BookID INT(10) PRIMARY KEY,
 Title VARCHAR(100),
 Author VARCHAR(60),
 Publisher VARCHAR(60),
 ISBN VARCHAR(20),
 YearPublished INT(4),
 Total_Copies INT(5),
 Price DECIMAL(8,2)
);
Insert records in the table.
INSERT INTO Books VALUES
 (1, 'Automobile Engineering', 'R.B. Gupta', 'Satya Prakashan', '978-81-7144-123-4', 2015, 10, 499.00),
 (2, 'Strength of Materials', 'R.K. Bansal', 'Laxmi Pub.', '978-81-318-0083-1', 2010, 8, 450.00),
 (3, 'C# Programming', 'Andrew Troelsen','Apress', '978-1-4842-3018-3', 2017, 5, 599.00),
 (4, 'Core Java', 'Cay Horstmann', 'Pearson', '978-0-13-516630-7', 2019, 12, 399.00),
 (5, 'Ruby on Rails', 'Michael Hartl', 'Pearson', '978-0-13-445445-7', 2016, 6, 349.00),
 (6, 'Artificial Intelligence','Stuart Russell', 'Pearson', '978-0-13-461099-3', 2020, 4, 649.00)'''
    "12": '''Stored Procedures
Query's:
1. Create a Stored Procedure to Display All Students.
DELIMITER //
CREATE PROCEDURE GetAllStudents()
BEGIN
 SELECT * FROM Student;
END //
DELIMITER ;
CALL GetAllStudents();
2. Create a stored procedure 'GetCity' to select employee from a particular city.
DELIMITER //
CREATE PROCEDURE GetCity(IN cityName VARCHAR(30))
BEGIN
 SELECT * FROM Department WHERE City = cityName;
END //
DELIMITER ;
CALL GetCity('Delhi');
Extra Added Queries
1. Procedure: Increase Marks and return marks (IN, OUT).
DELIMITER //
CREATE PROCEDURE IncreaseMarks(IN rno INT, IN inc INT, OUT newMarks INT)
BEGIN
 UPDATE Student SET Marks = Marks + inc WHERE RollNo = rno;
 SELECT Marks INTO newMarks FROM Student WHERE RollNo = rno;
END //
DELIMITER ;
CALL IncreaseMarks(1701, 5, @result); SELECT @result;

2. Pass RollNo and check student Pass or Fail.
DELIMITER //
CREATE PROCEDURE CheckResult(IN rno INT)
BEGIN
 DECLARE m INT;
 SELECT Marks INTO m FROM Student WHERE RollNo = rno;
 IF m >= 35 THEN SELECT 'Pass' AS Result;
 ELSE SELECT 'Fail' AS Result;
 END IF;
END //
DELIMITER ;
CALL CheckResult(1701);

3. Procedure to check if a number is Even or Odd.
DELIMITER //
CREATE PROCEDURE CheckEvenOdd(IN n INT)
BEGIN
 IF n % 2 = 0 THEN SELECT 'Even' AS Type;
 ELSE SELECT 'Odd' AS Type;
 END IF;
END //
DELIMITER ;
CALL CheckEvenOdd(4);

4. Procedure to Display 10 Numbers.
DELIMITER //
CREATE PROCEDURE Display10Numbers()
BEGIN
 DECLARE i INT DEFAULT 1;
 WHILE i <= 10 DO
 SELECT i;
 SET i = i + 1;
 END WHILE;
END //
DELIMITER ;
CALL Display10Numbers();

5. Insert Record in table using Procedure.
DELIMITER //
CREATE PROCEDURE InsertStudent(IN rno INT, IN nm VARCHAR(35),
 IN cls VARCHAR(30), IN mrk INT)
BEGIN
 INSERT INTO Student(RollNo,Name,Class,Marks) VALUES(rno,nm,cls,mrk);
END //
DELIMITER ;
CALL InsertStudent(1706, 'Rahul Kumar', 'BCA', 80);

6. Check grade using IF ELSE by passing RollNo.
DELIMITER //
CREATE PROCEDURE CheckGrade(IN rno INT)
BEGIN
 DECLARE m INT;
 SELECT Marks INTO m FROM Student WHERE RollNo = rno;
 IF m >= 90 THEN SELECT 'A+' AS Grade;
 ELSEIF m >= 80 THEN SELECT 'A' AS Grade;
 ELSEIF m >= 70 THEN SELECT 'B' AS Grade;
 ELSE SELECT 'C' AS Grade;
 END IF;
END //
DELIMITER ;
CALL CheckGrade(1701);

7. CASE Statement - procedure to display color by passing number.
DELIMITER //
CREATE PROCEDURE GetColor(IN n INT)
BEGIN
 SELECT CASE n
 WHEN 1 THEN 'Red'
 WHEN 2 THEN 'Green'
 WHEN 3 THEN 'Blue'
 WHEN 4 THEN 'Yellow'
 ELSE 'Unknown'
 END AS Color;
END //
DELIMITER ;
CALL GetColor(2);
''',
    "2": '''Views
Query's:
1. Create View on Student table and display record using view.
CREATE VIEW StudentView AS
SELECT RollNo, Name, Class, Marks FROM Student;
SELECT * FROM StudentView;
2. Modify view and check how it reflects in original table.
CREATE OR REPLACE VIEW StudentView AS
SELECT RollNo, Name, Class, Marks FROM Student WHERE Class = 'BCA';
UPDATE StudentView SET Marks = 90 WHERE RollNo = 1701;
SELECT * FROM Student WHERE RollNo = 1701;
Note: Changes made through a view are reflected in the original base table''',
"14": '''Index
Query's:
1. Create index on Student table and display index.
CREATE INDEX idx_student_name ON Student(Name);
SHOW INDEX FROM Student;
Explanation:
PRIMARY - Unique index on RollNo (Primary Key)
idx_student_name - Index created on Name column for faster search.-- To drop the index:
DROP INDEX idx_student_name ON Student''',
"15" : '''Display all records from Student table.
1) While inserting record I want to fire trigger insert
a) Insert record in student table.
INSERT INTO Student VALUES (1707, 'Rahul Suresh Patil', 'BCA', 68);
b) Display all records from Student table using trigger.
DELIMITER $$
CREATE TRIGGER after_student_insert
AFTER INSERT ON Student
FOR EACH ROW
BEGIN
 SELECT * FROM Student;
END$$
DELIMITER ;
2) While deleting record I want to fire trigger delete 
a) Create empty backup table.
CREATE TABLE Student_Backup (
 RollNo INT(10) PRIMARY KEY,
 Name VARCHAR(35),
 Class VARCHAR(30),
 Marks INT(10)
);
b) While deleting record fire trigger delete.
DELIMITER $$
CREATE TRIGGER before_student_delete
BEFORE DELETE ON Student
FOR EACH ROW
BEGIN
 INSERT INTO Student_Backup VALUES
 (OLD.RollNo, OLD.Name, OLD.Class, OLD.Marks);
END$$
DELIMITER ;
c) Display all records from Student table.
SELECT * FROM Student;
d) Delete record from Student table.
DELETE FROM Student WHERE RollNo = 1707;
e) Display record from backup table.
SELECT * FROM Student_Backup;
3) While updating record I want to fire trigger update
a) Create empty backup table for update.
CREATE TABLE Student_Update_Backup (
 RollNo INT(10) PRIMARY KEY,
 Name VARCHAR(35),
 Class VARCHAR(30),
 Marks INT(10)
);
b) While updating record fire trigger update.
DELIMITER $$
CREATE TRIGGER before_student_update
BEFORE UPDATE ON Student
FOR EACH ROW
BEGIN
 INSERT INTO Student_Update_Backup VALUES
 (OLD.RollNo, OLD.Name, OLD.Class, OLD.Marks);
END$$
DELIMITER ;
c) Display all records from Student table.
SELECT * FROM Student;
d) Update record from student table.
UPDATE Student SET Marks = 90 WHERE RollNo = 1701;
e) Updated record display student table.
SELECT * FROM Student;
f) Display old record from student backup table.
SELECT * FROM Student_Update_Backup;
Create new table stud
CREATE TABLE stud (
 RollNo INT(10) PRIMARY KEY,
 Name VARCHAR(35),
 Marks INT(10)
);
Insert record in stud
INSERT INTO stud VALUES (1, 'Krishna Sarovar', 68);
INSERT INTO stud VALUES (2, 'Dinesh Jadhav', 45);
INSERT INTO stud VALUES (3, 'Mahesh Patil', 55);
Display all record stud
SELECT * FROM stud;
4) Check student mark Pass and Fail.
i) Insert record into student.
INSERT INTO stud VALUES (4, 'Nagesh Kale', 38);
ii) Display record student pass or fail.
DELIMITER $$
CREATE TRIGGER check_pass_fail
BEFORE INSERT ON stud
FOR EACH ROW
BEGIN
 IF NEW.Marks >= 40 THEN
 SET NEW.Result = 'Pass';
 ELSE
 SET NEW.Result = 'Fail';
 END IF;
END$$
DELIMITER ;
5) Create trigger to check salary of employee
a) Create trigger check salary.
DELIMITER $$
CREATE TRIGGER check_salary
BEFORE INSERT ON Emp
FOR EACH ROW
BEGIN
 IF NEW.Salary < 0 THEN
 SIGNAL SQLSTATE '45000'
 SET MESSAGE_TEXT = 'Salary cannot be negative';
 END IF;
END$$
DELIMITER ;
b) Display record employee.
SELECT * FROM Emp;

c) Insert new record emp trigger.
INSERT INTO Emp VALUES
(6, 'Rishikesh Bherde', 'Sales', 'Executive', '2024-01-10', 42000);
d) Display all record emp and show trigger.
SELECT * FROM Emp;

6) While inserting a record I want to fire trigger what name is insert the name is uppercase
Create new table stud
CREATE TABLE stud (
 RollNo INT(10) PRIMARY KEY,
 Name VARCHAR(35),
 Marks INT(10)
);
Display student record
SELECT * FROM stud;
Use delimiter
a) Create uppercase trigger.
DELIMITER $$
CREATE TRIGGER uppercase_name
BEFORE INSERT ON stud
FOR EACH ROW
BEGIN
 SET NEW.Name = UPPER(NEW.Name);
END$$
DELIMITER ;
b) Insert record in student table.
INSERT INTO stud VALUES (4, 'rahul patil', 72);
c) Display all record student uppercase trigger.
SELECT * FROM stud;''',
"16" : '''Cursor
Use delimiter //
mysql>delimiter //
Display all record employes table
mysql> select * from employes//
1) Write a cursor to display total salary
mysql> create procedure totals()
 -> begin
 -> declare sal int;
 -> declare total int default 0;
 -> declare done int default 0;
 -> declare curs cursor for select salary from employes;
 -> declare continue handler for not found set done=1;
 -> open curs;
 -> read_loop:loop
 -> fetch curs into sal;
 -> if done=1 then
 -> leave read_loop;
 -> end if;
 -> set total=total+sal;
 -> end loop;
 -> close curs;
 -> select total;
 -> end //
Display total salary
mysql> call totals()//
+--------+
| total  |
+--------+
| 135500 |
+--------+
2) Write a cursor count total number of employes similarly
mysql> create procedure count_emp()
 -> begin
 -> declare done int default 0;
 -> declare cemp int;
 -> declare total int default 0;
 -> declare empcur cursor for select Emp_id from employes;
 -> declare continue handler for not found set done=1;
 -> open empcur;
 -> read_loop:loop
 -> fetch empcur into cemp;
 -> if done=1 then
 -> leave read_loop;
 -> end if;
 -> set total=total+1;
 -> end loop;
 -> close empcur;
 -> select total as total_Employe;
 -> end //
Display total employes
mysql> call count_emp()//

3) Write a cursor to show employe with salary more than 30000
mysql> create procedure eslary()
 -> begin
 -> declare name varchar(20);
 -> declare salarys int;
 -> declare done int default 0;
 -> declare scurs cursor for select Ename,salary from employes;
 -> declare continue handler for not found set done = 1;
 -> open scurs;
 -> read_loop: LOOP
 -> fetch scurs into name,salarys;
 -> if done = 1 then
 -> leave read_loop;
 -> end if;
 -> if salarys > 30000 then
 -> select name, salarys;
 -> end if;
 -> end loop;
 -> close scurs;
 -> end //
Display salary more than 30000
mysql> call eslary()//

4) Write a cursor to print name in uppercase
mysql> create procedure dist()
 -> begin
 -> declare name varchar(20);
 -> declare done int default 0;
 -> declare ucurs cursor for select Ename from employes;
 -> declare continue handler for not found set done=1;
 -> open ucurs;
 -> read_loop:loop
 -> fetch ucurs into name;
 -> if done=1 then
 -> leave read_loop;
 -> end if;
 -> select upper(name);
 -> end loop;
 -> close ucurs;
 -> end //
Display upper case names
mysql> call dist()//

Save
mysql> commit/'''

}

for num, content in assignments.items():
    if st.button(num):
        pyperclip.copy(content)
        st.success(f"Assignment {num} copied to clipboard!")