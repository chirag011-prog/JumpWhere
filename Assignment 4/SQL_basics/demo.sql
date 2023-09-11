use demo;
create table student(
	student_id int auto_increment,
    student_name varchar(20),
    major varchar(20) ,
    primary key(student_id)
    ); 


desc student;

alter table student add gpa decimal(3,2);
drop table student;
desc student;


insert into student(student_name,major,gpa) values("jake","aiml",8.4);
insert into student (student_name,major,gpa) 
values("sam","cse",8.0);
insert into student (student_name,major,gpa) 
values("chirag","aiml",8.4);
insert into student (student_name,major,gpa) 
values("king","cse",8.6);
insert into student (student_name,major,gpa) 
values("prince","ise",8.2);
select * from student;







