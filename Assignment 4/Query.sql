--1. Select employee details  of dept number 10 or 30
select * from emp where DeptNo=10 or DeptNo=30;

--2. Write a query to fetch all the dept details with more than 1 Employee.
select Dname from department inner join emp
on emp.DeptNo = department.DeptNo group by
Dname having count(*)>1; 

--3. Write a query to fetch employee details whose name starts with the letter “S”
select * from emp where Ename like 'S%';

--4. Select Emp Details Whose experience is more than 2 years 

--5. Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)
select Ename, replace(Ename, 'a','#')
as new_ename from emp;

--6. Write a query to fetch employee name and his/her manager name. 
select E.Ename as "employee", M.Ename as "manager" 
from emp E left outer join emp M
on E.mgr=M.EmpNo;

--7. Fetch Dept Name , Total Salry of the Dept
select department.DeptNo, department.Dname, sum(emp.Sal) from 
department left join emp on department.DeptNo=emp.DeptNo
group by department.DeptNo;

--8. Write a query to fetch ALL the  employee details along with 
--department name, department location, irrespective of employee existance in the department.
select * from emp, department where emp.DeptNo = department.DeptNo;

--9. Write an update statement to increase the employee salary by 10 %
update emp set Sal = Sal+(Sal*10/100);
select Ename,Sal from emp;

--10. Write a statement to delete employees belong to Chennai location.
delete from empwhere DeptNo in(select DeptNofrom department
where Loc = 'Chennai'
);

--11. Get Employee Name and gross salary (sal + comission) 
select ename,
(Sal+ coalesce(comission, 0)) as GrossSal from emp;

--12. Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement
alter table emp modify Ename varchar(250);

--13. Write query to get current datetime
select current_timestamp();

--14. Write a statement to create STUDENT table, with related 5 columns
create table student(student_id int primary key,
first_name varchar(20) not null,
last_name varchar(20),
dob date,
gender char(1),
branch varchar(20)
);

--15.  Write a query to fetch number of employees in who is getting salary more than 10000
select count(Ename) from emp where Sal>10000;

--16. Write a query to fetch minimum salary, maximum salary and average salary from emp table.
select min(Sal), max(Sal), avg(Sal) from emp;

--17. Write a query to fetch number of employees in each location
select count(e.Ename), d.Loc from department d
left join emp e on  d.DeptNo = e.DeptNo group by d.Loc;

--18. Write a query to display emplyee names in descending order
select Ename from emp order by Ename desc;

--19. Write a statement to create a new table(EMP_BKP) from the existing EMP table 
create table emp_bkp as select * from emp;

--20. Write a query to fetch first 3 characters from employee name appended with salary.
select concat(substring(Ename,1,3),Sal) from emp;

--21. Get the details of the employees whose name starts with S
select * from emp where Ename like 'S%';

--22. Get the details of the employees who works in Bangalore location
select e.* from emp e join department d on e.DeptNo = d.DeptNo
where d.Loc="Bangalore";

--23.  Write the query to get the employee details whose name started within  any letter between  A and K
select * from emp where Ename like '[A-K]%';

--24. Write a query in SQL to display the employees whose manager name is Stefen 
select e1.* from emp e1
join emp e2 on e1.mgr=e2.EmpNo where e2.Ename="Stefen";

--25. Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
select mgr
from(
    select mgr, count(*) as ecount
    from emp
    group by mgr
    order by ecount desc
    limit 1
) as MaxEmployees
join emp e on MaxEmployees.mgr = e.EmpNo;

--27. Write a query to list all details of all the managers
select * from emp where EmpNo in(select distinct mgr from 
emp where mgr is not null);



