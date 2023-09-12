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

