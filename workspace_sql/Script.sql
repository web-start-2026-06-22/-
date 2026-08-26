-- 주석
/*
범위 주석
*/

select
	*
from
	emp;

select
	*
from
	emp
where
	1 != 1

select
	*
from
	dept;

select
	*
from
	salgrade;

select
	empno
from
	emp;

select
	empno,
	ename
from
	emp;

select
	empno as '사번',
	ename as '사원명'
from
	emp;

select
	job
from
	emp;

-- 중복 결과를 하나만 보여준다.
select
	distinct
	job
from
	emp;

select
	job as '직책'
from
	emp;

-- as 생략 가능
select
	job 직책
from
	emp;

select
	sal,
	sal * 12 as '연봉'
from
	emp;

select
	100 * 12;

select
	sal,
	comm,
	sal + comm
from
	emp;

select
	*
from
	emp
where
	deptno = 20;

select
	*
from
	emp
where
	deptno = 20
	and job = 'CLERK';

select
	*
from
	emp
where
	deptno = 20
	or job = 'CLERK';

select
	*
from
	emp
where
	(deptno = 30
		or deptno = 20)
	and job = 'CLERK';

select
	*
from
	emp
where
	sal = 3000;

select
	*
from
	emp
where
	sal != 3000;

select
	*
from
	emp
where
	sal <> 3000;

select
	*
from
	emp
where
	not (sal = 3000);

-- 문제1
-- 급여가 2000 이상이고 3000 미만인 사원을 출력
select
	*
from
	emp
where
	sal >= 2000
	and sal < 3000;

-- between A and B
-- A 이상 and B 이하
select
	*
from
	emp
where
	sal between 2000 and 3000;

-- 문제2
-- job이 CLERK 이거나 급여가 2000 초과 이면서 부서 번호가 10인 사원만 출력
select
	*
from
	emp
where
	job = 'CLERK'
	or (sal > 2000
		and deptno = 10);

-- 컬럼이 같고 or로 연결되어 있는 경우
-- in으로 간편하게 표현 가능
select
	*
from
	emp
where
	deptno = 20
	or deptno = 30

select
	*
from
	emp
where
	deptno in (20, 30);

select
	*
from
	emp
where
	deptno not in (20, 30);

-- % : 모든 글자를 뜻 함(심지어 글씨가 없어도 포함)
select
	*
from
	emp
where
	ename like 'S%';

select
	*
from
	emp
where
	ename like '%N';

select
	*
from
	emp
where
	ename like '%A%';

select
	*
from
	emp
where
	ename like '%AM%';

-- _ : 아무 글자 딱 하나
select
	*
from
	emp
where
	ename like '_L%';

-- 문제4
-- 이름이 5글자인 사람만 출력
select
	*
from
	emp
where
	ename like '_____';

select
	'Human';
select
	lower('Human');
select
	upper('Human');

-- 문제5
-- 'Am'을 이용해서 am이 이름 중간에 들어가는 사람만 출력
-- (mariaDB는 like에서 대소문자 구분 원래 안함)
select
	*
from
	emp
where
	lower(ename) like lower('%Am%');

-- 문제6
-- 부서 10 또는 20의 사원 중 이름에 A가 들어가는 사원만 출력
select
	*
from
	emp
where
	deptno in (10, 20)
	and ename like '%A%';

select
	*
from
	emp;

select
	*
from
	emp
where
	comm = null;

select
	*
from
	emp
where
	comm < 100;

select
	*
from
	emp
where
	comm is null;

select
	*
from
	emp
where
	comm is not null;

select
	*
from
	emp
order by
	sal;

-- asc : 오름차순, 생략 가능
select
	*
from
	emp
order by
	sal asc; 

-- desc : 내림차순
select
	*
from
	emp
order by
	sal desc; 

select
	*
from
	emp
order by
	deptno;

-- order by에 여러 컬럼이 적혀있는 경우
-- 왼쪽부터 적용되고 동일한 값이 있는 경우 다음 조건이 적용된다.
select
	*
from
	emp
order by
	deptno desc,
	job;

select
	*
from
	emp
order by
	deptno desc,
	job asc,
	empno;

select
	*
from
	emp
where
	sal > 1000
order by
	deptno desc,
	job asc,
	empno;

-- limit : 보여줄 row의 수 제한
select
	*
from
	emp
where
	sal > 1000
order by
	deptno desc,
	job asc,
	empno
limit 3;

-- limit offset, rows
-- offset만큼 건너뛰고 rows만큼 보여줌
select
	*
from
	emp
where
	sal > 1000
order by
	deptno desc,
	job asc,
	empno
limit 5,
3;

-- 문제3
-- 부서번호가 20 또는 30인 사원 중에서
-- 급여가 2000~3000 사이(포함=이상, 이하)인 사원의
-- 연봉이 작은 순으로 출력
-- 연봉이 같으면 이름을 내림차순으로 정렬

select
	*
from
	emp
where
	(deptno = 20
		or deptno = 30)
	and (sal >= 2000
		and sal <= 3000)
order by
	sal asc,
	ename desc;

-- 집계 함수
select
	count(ename)
from
	emp;

select
	count(mgr)
from
	emp;

select
	count(comm)
from
	emp;

select
	count(*) '데이터 건수'
from
	emp;

select
	max(sal)
from
	emp;

select
	min(sal)
from
	emp;

select
	sum(sal)
from
	emp;

select
	avg(sal)
from
	emp;

select
	count(*),
	max(sal),
	min(sal),
	sum(sal),
	avg(sal)
from
	emp;

select
	length(ename),
	ename
from
	emp;

-- 집계 함수와 함께 컬럼을 select해오면 원하는 결과가 나오지 않음.
-- 집계 함수가 셀 병합처럼 동작하기 때문에.
select
	count(*),
	ename
from
	emp;

select
	*
from
	emp
where
	length(ename) = 4;

-- 대상의 몇 번째부터 몇 개를 잘라오기
select
	substring(ename, 2, 3),
	ename
from
	emp;

select
	substr(ename, 2, 3),
	ename
from
	emp;

-- 전부 교체
select
	replace(ename, 'A', '에이'),
	ename
from
	emp;

-- 대상의 자릿수를 맞춰주고 남으면 채워줌.
select
	lpad(ename, 10, '#')
from
	emp;

select
	lpad(ename, 3, '#')
from
	emp;

select
	rpad(ename, 10, '#')
from
	emp;

select
	trim('   a  b  c   ');

select
	concat(ename, job)
from
	emp;

select
	concat(ename, ' ', job)
from
	emp;

-- 오라클에서 합치기 ename || job으로 사용 가능

select
	concat_ws('-', ename, job, empno)
from
	emp;

-- 소수점 몇 째자리까지 살릴 것인지, 콤마 뒤에 표현
-- 반올림
select
	round(3.14);

select
	round(3.15, 1);

-- 올림
select
	ceil(3.14);

select
	ceil(-3.14);

-- 내림
select
	floor(3.14);

select
	floor(-3.14);

-- 버림
select
	truncate(-3.14, 1);

-- 나머지
select
	mod(10, 3);

-- 현재 시간
select
	now();

select
	sysdate();

-- 날짜 출력 양식 지정
select
	date_format(now(), '%Y년 %m월 %d일 %H시 %i분 %s초')
	
-- 문자를 날짜 형으로 변환
select
	str_to_date('2026-08-07', '%Y-%m-%d');

select
	ifnull(comm, 0),
	comm
from
	emp;

select
	coalesce(comm, 0),
	comm
from
	emp;

select
	sal * 12 + comm
from
	emp;

select
	sal * 12 + ifnull(comm, 0)
from
	emp;

-- 문제
-- ename의 앞 두 글자만 출력

select
	lpad(ename, 2)
from
	emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 4개의 *를 붙여서 출력
-- SM****

select
	concat(lpad(ename, 2), '****')
from
	emp;

select
	rpad(substring(ename, 1, 2), 6, '*')
from
	emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 나머지 이름 만큼의 * 출력
-- WARD >> WA**, SMITH >> SM***

select
	rpad(substring(ename, 1, 2), length(ename), '*')
from
	emp;

-- case 문
select
	*
from
	emp;

select
	job,
	sal,
	case
		job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal * 1
	end as upsal
from
	emp;

select
	job,
	sal,
	case
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal * 1
	end as upsal
from
	emp;

select
	sal,
	comm,
	case
		when comm is null then 0
		else comm
	end
from
	emp;

select
	deptno
from
	emp
group by
	deptno;

select
	deptno,
	count(*),
	sum(sal)
from
	emp
group by
	deptno;

select
	deptno,
	job,
	count(*)
from
	emp
group by
	deptno,
	job;

select
	deptno,
	job
from
	emp
where
	deptno = 10
group by
	deptno,
	job

	
select
	deptno,
	job
from
	emp
where
	deptno = 10
group by
	deptno,
	job
order by
	job;

select
	avg(sal)
from
	emp;

-- select
-- 	ename,
-- 	sal,
-- 	avg(sal)
-- from
-- 	emp
-- where
-- 	sal >= avg(sal);

select
	avg(sal) as avg_sals,
	deptno,
	job
from
	emp
where
	deptno = 10
group by
	deptno,
	job
having
	deptno = 10;


-- 직업 별로 연봉 1000 이상인 사람이 3명 이상인 경우만 출력
select
	job,
	count(*) cnt
from
	emp
where
	sal >= 1000
	-- 	and cnt >= 3
	-- 	and count(*) >= 3
group by
	job
having
	count(*) >= 3;

select
	job,
	1 as num
from
	emp
where
	sal > 1000
group by
	job
having
	count(*) >= 3
order by
	job desc;

select
	*
from
	emp
where
	deptno = 10
union
select
	*
from
	emp
where
	deptno = 10;

select
	*
from
	emp
where
	deptno = 10
union all
select
	*
from
	emp
where
	deptno = 10;

select
	*
from
	emp
where
	sal > (
	select
		sal
	from
		emp
	where
		ename = 'WARD'
);

select * from emp
where sal > (select avg(sal) from emp);

-- 'WARD'의 연봉만 출력

select
	sal
from
	emp
where
	ename = 'WARD';

-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉

select
	deptno,
	max(sal)
from
	emp
group by
	deptno;

select
	ename,
	sal
from
	emp
	-- where
	-- 	sal = 3000
	-- 	or sal = 2850
	-- 	or sal = 5000;
where
	sal in (3000, 2850, 5000);

select
	ename,
	sal,
	deptno
from
	emp
where
	sal in (
	select
		max(sal)
	from
		emp
	group by
		deptno
);

select * from dept;

select
	*
from
	emp,
	dept;

select
	*
from
	emp,
	dept
where
	emp.deptno = dept.deptno;

select
	e.empno,
	e.ename,
	e.mgr,
	m.ename
from
	emp as e
join emp as m on
	e.mgr = m.empno;

select
	*
from
	emp e,
	dept d
where
	e.deptno = d.deptno;

-- select
	-- 	ename,
	-- 	dname,
	-- 	deptno
	-- from
	-- 	emp e,
	-- 	dept d
	-- where
	-- 	e.deptno = d.deptno;

select
	e.ename,
	d.dname,
	d.deptno
from
	emp e,
	dept d
where
	e.deptno = d.deptno;

select
	*
from
	salgrade;

select
	e.ename,
	e.sal,
	s.grade,
	s.losal,
	s.hisal
from
	emp e,
	salgrade s
where
	(e.sal between s.losal and hisal)
	and e.ename = 'SMITH';

select * from emp;


-- mgr이 null인 것은 빠졌다.
select
	e.empno,
	e.ename,
	e.mgr '상사 사번',
	m.ename 상사
from
	emp as e
join emp as m on
	e.mgr = m.empno;
-- where
-- 	e.ename = 'SMITH';

-- 문제
-- 이름, 급여, 부서명, 급여 등급, 등급 순 내림차순

select
	e.ename 사원명,
	e.sal 급여,
	d.dname 부서명,
	s.grade 급여등급
from
	emp e
join dept d on
	e.deptno = d.deptno,
	salgrade s
where
	e.sal between s.losal and s.hisal
order by
	s.grade desc,
	e.sal desc;

select
	*
from
	emp e
join dept d on
	(e.deptno = d.deptno);

select
	*
from
	emp e
join dept d
		using(deptno);

select
	e.empno,
	e.ename,
	e.mgr '상사 사번',
	m.ename 상사
from
	emp as e
left outer join emp as m on
	e.mgr = m.empno;

select
	e.empno,
	e.ename,
	e.mgr '상사 사번',
	m.ename 상사
from
	emp as e
right outer join emp as m on
	e.mgr = m.empno;

select
	*
from
	dept;

select
	sal
from
	emp
where
	ename = 'SCOTT';

select
	grade
from
	salgrade
where
	3000 between losal and hisal;

select
	sal,
	ename,
	(
	select
		grade
	from
		salgrade
	where
		3000 between losal and hisal) grade
from
	emp
where
	ename = 'SCOTT';



-- 문제
-- deptno, dname, empno, ename
-- 모든 부서가 다 나오게 출력
-- 부서 번호 오름차순, 이름 오름차순

select
	d.deptno,
	d.dname,
	e.empno,
	e.ename
from
	dept d
left outer join emp e on
	(d.deptno = e.deptno)
order by
	d.deptno asc,
	e.ename asc;


-- select
-- 	ename + sal
-- from
-- 	emp;

-- DDL
-- create
desc emp;

create table emp2(
	empno int(4) primary key,
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리 소수점
	comm decimal(7, 2),
	deptno int(2)
);

select
	*
from
	emp2;

desc emp2;

desc dept;

create table dept2(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);

select
	*
from
	dept2;

desc dept2;

-- 테이블 복사
create table emp_copy
as select * from emp;


select
	*
from
	emp_copy;

create table emp_copy2
as select * from emp where 1 <> 1;

select * from emp_copy2;

create table dept3
as select * from dept where 1 != 1;

select * from dept3;

desc dept3;

-- 테이블 삭제
drop table dept3;

create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2),
	comm decimal(7, 2),
	deptno int(2),
	primary key(empno),
	foreign key(deptno) references dept3(deptno)
);

select * from emp3;

desc emp3;

create table dept3(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);

-- alter
alter table emp3
add gender varchar(10) not null default'남';
select * from emp3;
desc emp3;

alter table emp3
change gender gender2 varchar(10);

alter table emp3
rename column gender2 to gender3;
select * from emp3;

alter table emp3
drop column gender;

drop table emp3;

drop table dept3;
desc dept3;

select * from emp_copy;
truncate table emp_copy; 

select * from dept2;
drop table dept2;

select * from emp2;
drop table emp2;

create table dept2(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);

create table emp2 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9) default 'CLERK',
	mgr int(4),
	hiredate date default now(),
	sal decimal(7, 2),
	comm decimal(7, 2),
	deptno int(2),
	primary key(empno),
	foreign key(deptno) references dept2(deptno)
);

select * from emp2;

insert into dept2
values (
	10,
	'맞아맞아마',
	'아카라이브'
);

insert into emp2
values (1000, '아무개', '아니아니마', 2000, str_to_date('2026-08-09', '%Y-%m-%d'), 4000, 100, 10)

insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '지에엥', 4100, 150, 10);


-- ename은 not null 제한.
-- insert에 누락하면 null이 들어간다.
-- 그래서 에러 발생.
-- insert into emp2 (empno, sal, comm, deptno)
-- values (1001, 4100, 150, 10);

-- primary key
-- unique + not null
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1001, '지에엥', 4100, 150, 10);

-- dept 테이블에 deptno 20값이 없어서 에러.
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1002, '지에엥', 4100, 150, 20);


insert into emp2 (empno, ename, sal, comm, deptno)
values
(1002, '뇨치킨', 4100, 150, 10),
(1003, '도망도망마', 4100, 150, 10),
(1004, '뇨이이익', 4100, 150, 10);

insert into emp2 (empno, ename, sal, comm, deptno)
values
(1012, '상처를 치료', 4100, 150, 10),
(1013, '해줄 사람', 4100, 150, 10),
(1014, '어디 없나', 4100, 150, 10);

select * from emp2;

-- update
update emp2
set
	sal = 1000,
	comm = 200;

update emp2
set
	sal = sal * 1.1,
	comm = comm * 1.2
where empno = 1002;

select * from dept2;

update dept2
set deptno = 20
where deptno = 10;

delete from emp2
where empno = 1001;

delete from emp2;

select * from emp2;

commit;

rollback;

select
	*
from
	emp e
left outer join emp e2 on
	(e.mgr = e2.empno)
left outer join dept d on
	(e.deptno = d.deptno)
order by
	e.ename desc;

select * from emp
where deptno = 10;

-- index
create index idx_emp_empno_desc
on emp(empno desc);

select * from emp;

select * from emp
order by empno desc;

create index idx_emp_deptno
on emp(deptno);

show index from emp;

select * from emp
where deptno = 10;

select *
from emp force index (idx_emp_deptno);

-- use
-- 강제는 아닌데 권장하는 느낌. force보다 약함.

-- mariadb 한글 한 글자는 3Byte
select length('한구');
select length('ab');

create table emp_auto (
	empno int auto_increment,
	ename varchar(50),
	primary key(empno)
);

insert into emp_auto (ename)
values ('가만히 놔두다간 끊임없이 덧나');

select * from emp_auto;

-- 무한 대댓글
select
empno, ename, mgr, 1 as level
from emp
where mgr is null
union all
select
empno, ename, mgr, 2 as level
from emp
where mgr = 7839;

with recursive emp_recu as (
select
	empno,
	ename,
	mgr,
	lpad(ename, length(ename), ' '),
	1 as level,
	cast(ename as char(200)) as sort_key
from
	emp
where
	mgr is null
union all
select
	e.empno,
	e.ename,
	e.mgr,
	lpad(e.ename, (er.level * 4)+ length(e.ename), ' '),
	er.level + 1 as level,
	concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
from
	emp e
join emp_recu er on
	e.mgr = er.empno
)
select
	*
from
	emp_recu
order by
	sort_key;
/*
문제 1
1981년에 입사한 사원 중에서
급여가 가장 낮은 사원을 조회하시오
*/

select ename 사원명, sal 최저급여 from emp
where sal =(
select min(sal)
from emp
where hiredate between '1981-01-01' and '1981-12-31'
);


/*
문제 2
각 부서 별
급여가 가장 높은 사원 가장 낮은 사원의 차이를 조회하시오
출력 : 부서명, 차이 금액
*/
select d.dname, (max(sal) - min(sal)) as '차이 금액'
from dept d join emp e using(deptno)
group by deptno;

/*
문제 3
BLAKE보다 높은 연봉을 받는 사람들 출력
*/
-- select sal
-- from emp
-- where ename = 'BLAKE';

select ename, sal
from emp
where sal > (
select sal
from emp
where ename = 'BLAKE'
);

/*
문제 4
JONES랑 같은 job을 가진 사람들
*/
-- select job
-- from emp
-- where ename = 'JONES';
select ename, job
from emp
where job = (
select job
from emp
where ename = 'JONES'
);


/*
문제 5
급여 등급 별 사원 수를 등급 오름차순으로 정렬
단, 모든 등급을 표시한다
*/
-- select * from salgrade;

select e.ename, s.grade
from emp e join salgrade s
where e.sal between losal and hisal
order by s.grade;

select grade.grade, count(grade)
from (
select s.grade
from emp e join salgrade s
where e.sal between s.losal and s.hisal
) as grade
group by grade
order by grade;


/*
문제 6
이름, 급여, 급여 등급, 부서 이름 조회
단, 급여 등급 3 이상만 조회.
급여 등급 내림차순, 등급이 같은 경우 급여 내림차순, 급여가 같은 경우 이름 내림차순
*/
select e.ename, e.sal, s.grade, d.dname
from emp e join dept d using(deptno)
join salgrade s
where e.sal between s.losal and s.hisal and s.grade >= 3
order by s.grade desc, e.sal desc, e.ename desc;

/*
문제 7
부서명이 SALES인 사원 중
급여 등급이 2 또는 3인 사원을 급여 내림차순으로 정렬
*/

select d.dname, e.ename, e.sal, s.grade
from emp e join dept d using(deptno)
join salgrade s
where e.sal between s.losal and s.hisal and s.grade in (2, 3) and d.dname = 'SALES'
order by sal desc;


-- ---------------------------------------------------------------------------
/* 시험 */
-- ---------------------------------------------------------------------------
/*
 * 문제1
 */

select e.ename, e.sal, d.dname
from emp e join dept d using(deptno)
where e.sal > 2000;

/*
* 문제2
*/

select e.ename, e.sal, s.grade
from emp e join salgrade s on e.sal between s.losal and s.hisal
where e.sal between 1000 and 3000;

/*
* 문제3
*/

select e.ename, e.hiredate, d.dname
from emp e join dept d using(deptno)
order by e.hiredate asc;

/*
* 문제4
*/

select e.ename, d.dname, e.sal, s.grade
from emp e join dept d using(deptno)
join salgrade s on e.sal between s.losal and s.hisal
where s.grade >= 3
order by e.sal desc;

/*
* 문제5
*/

-- 평균 구하기
select deptno, avg(sal)
from emp
group by deptno;

-- 부서번호 10에 해당하는 사원
select e.ename, d.dname, e.sal
from emp e join dept d using(deptno)
where deptno = 10 and sal >
(
select avg(sal)
from emp
where deptno = 10
);

-- 부서번호 20에 해당하는 사원
select e.ename, d.dname, e.sal
from emp e join dept d using(deptno)
where deptno = 20 and sal >
(
select avg(sal)
from emp
where deptno = 20
);

-- 부서번호 30에 해당하는 사원
select e.ename, d.dname, e.sal
from emp e join dept d using(deptno)
where deptno = 30 and sal >
(
select avg(sal)
from emp
where deptno = 30
);


-- 합치면
select e.ename, d.dname, e.sal
from emp e join dept d using(deptno)
where deptno = 10 and e.sal >
(
select avg(sal)
from emp
where deptno = 10
) or deptno = 20 and e.sal >
(
select avg(sal)
from emp
where deptno = 20
) or deptno = 30 and e.sal >
(
select avg(sal)
from emp
where deptno = 30
);


-- 값 나오는지 테스트
select * from emp e join (select deptno, avg(sal) as avsal
from emp
group by deptno ) as avsalT using(deptno)
where sal > avsalT.avsal;

-- 최종 코드
select e.ename, d.dname, e.sal, avsalT.avsal as '평균 급여'
from emp e join (select deptno, avg(sal) as avsal
from emp
group by deptno ) avsalT using(deptno)
join dept d using(deptno)
where e.sal > avsalT.avsal
order by d.dname asc, e.sal desc;

-- python으로 만든 테이블
select * from emp3;

select * from dept3;

commit;

insert into dept3
select * from dept;

insert into emp3
select * from emp;

drop table emp3;

-- update emp3
-- set sal = sal * 1.1
-- where deptno = 30;

-- select e.ename, d.dname, e.sal, avg(e.sal)
-- from emp e join dept d using(deptno)
-- group by deptno
-- order by d.dname asc, e.sal desc;
