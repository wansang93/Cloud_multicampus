/**********************************************************
            	SQL Query & Function Example1
**********************************************************/

/**
-- Employees Table Columns
-- EMPLOYEE_ID
-- FIRST_NAME
-- LAST_NAME
-- EMAIL
-- PHONE_NUMBER
-- HIRE_DATE
-- JOB_ID
-- SALARY
-- COMMISSION_PCT
-- MANAGER_ID
-- DEPARTMENT_ID
**/


-- 부서번호가 10번인 부서의 사람 중 사원번호, 이름, 월급을 출력하라
SELECT
CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME",
SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 10;


-- 사원번호가 7369인 사람 중 이름, 입사일, 부서 번호를 출력하라.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME",
HIRE_DATE, DEPARTMENT_ID
FROM EMPLOYEES e
WHERE EMPLOYEE_ID = 7369;


-- 이름이 Ellen인 사람의 모든 정보를 출력하라.
SELECT *
FROM EMPLOYEES e 
WHERE FIRST_NAME = 'Ellen';


-- 입사일이 08/04/21인 사원의 이름, 부서번호, 월급을 출력하라.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME",
 DEPARTMENT_ID, SALARY 
FROM EMPLOYEES e 
WHERE HIRE_DATE >= '20080421';


-- 직무가 SA_MAN 아닌 사람의 모든 정보를 출력하라.
SELECT * 
FROM EMPLOYEES e
WHERE JOB_ID != 'SA_MAN';


-- 입사일이 08/04/21 이후에 입사한 사원의 정보를 출력하라.
SELECT *
FROM EMPLOYEES e 
WHERE HIRE_DATE > '20080421';


-- 부서번호와 20,30번을 제외한 모든 사람의 이름, 사원번호, 부서번호를 출력하라.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", EMPLOYEE_ID, DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID != 20 AND DEPARTMENT_ID != 30;


-- 이름이 S로 시작하는 사원의 사원번호, 이름, 입사일, 부서번호를 출력하라.
SELECT EMPLOYEE_ID, CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", HIRE_DATE, DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE UPPER(FIRST_NAME)  LIKE 'S%';


--이름이 s로 시작하고 마지막 글자가 t인 사람이 정보를 출력하라.
SELECT *
FROM EMPLOYEES e 
WHERE UPPER(FIRST_NAME) LIKE 'S%T';


-- employees 테이블에서 이름, 급여, 상여, 총액을 구하여 총액 많은 순서로 출력하라 단 상여금이 NULL인 사람은 제외
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, COMMISSION_PCT, SALARY+(COMMISSION_PCT*SALARY) "TOTAL" 
FROM EMPLOYEES e 
WHERE COMMISSION_PCT IS NOT NULL;


-- 10번 부서의 모든 사람들에게 급여의 13%를 보너스로 지불하기로 하였다. 이름, 급여, 보너스금액, 부서번호를 출력하라.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, (SALARY*13/100) "BONUS", DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 10;


/**
-- 30번 부서의 연봉을 계산하여 이름, 부서번호, 급여, 연봉을 출력하라. 단 연말에 급여의 150%를 보너스로 지급한다.
-- 연봉 = sal*12+(sal*1.5)
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", DEPARTMENT_ID , SALARY, SALARY*12+SALARY*1.5 "ANNUAL_SALARY"
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 30;


/**
-- 부서번호가 20인 부서의 시간당 임금을 계산하여 출력하라. 단 1달의 근무일수는 12일이고 1일 근무시간은 5시간이다.
-- 출력양식은 이름, 급여, 시간당 임금(소수이하 1번째 자리에서 반올림)을 출력하라.
-- 시급 = sal/일수/시간  -> sal/12/5 
-- round(m, n) m을 소수점 n자리에서 반올림
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, ROUND(SALARY/12/5, 1) "HOURLY" 
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 20;


/**
-- 급여가 1500부터 3000사이의 사람은 급여의 5%를 회비로 지불하기로 하였다. 이를 이름, 급여, 회비(-2자리에서 반올림)를 출력하라.
-- 회비  = sal * 0.05	
-- -2자리에서 반올림 : 정수 2번째 자리에서 반올림.. 100단위로  
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, ROUND(SALARY*0.05, -2) "MEMBERSHIP_DUES"
FROM EMPLOYEES e 
WHERE SALARY >= 1500 AND SALARY <= 3000;


/**
입사일부터 지금까지의 날짜수를 출력하라. 부서번호, 이름, 입사일, 현재일, 근무일수(소수점이하절삭), 근무년수,
근무월수(30일 기준)를 출력하라.
지금 날짜 : sysdate 
근무 일수 : 현재날짜 - 입사일 = sysdate - hire_date  -> 날짜 - 날짜 : 일수 나옴
근무 년수 : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
근무 월수 : 근무일수 / 1달(30일)
**/
SELECT
EMPLOYEE_ID, CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME",
HIRE_DATE,
SYSDATE "TODAY",
FLOOR(SYSDATE - HIRE_DATE) "WORKING DAYS",
-- 방법1 문제가 요구한 방법
TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY')) - TO_NUMBER(TO_CHAR(HIRE_DATE, 'YYYY')) "WORKING YEARS",
-- 방법2, 근무 달수를 구하고 12로 나눈 후 내림
-- TRUNC(MONTHS_BETWEEN(SYSDATE, HIRE_DATE) / 12, 0) "WORKING YEARS2",
FLOOR((SYSDATE - HIRE_DATE) / 30) "WORKING MONTHS"
FROM EMPLOYEES e;



/**
-- 입사일로부터 오늘까지의 일수를 구하여 이름, 입사일, 근무일수를 출력하라.
-- round(sysdate-hiredate,0) 근무일수
**/
SELECT
CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME",
HIRE_DATE,
ROUND(SYSDATE - HIRE_DATE, 0) "WORKING DAYS"
FROM EMPLOYEES e;


/**
-- 입사일을 2012년 7월 5일의 형태로 이름, 입사일을 출력하라.
-- 날짜 형시 앞에 fm 은 선행 '0'을 표현하지 않는다는 뜻.. 
-- 'fmYYYY"년" MM"월" DD"일' 
**/
SELECT
TO_CHAR(HIRE_DATE, 'fmYYYY"년" MM"월" DD"일"') "HIRE_DATE",
CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME"
FROM EMPLOYEES e;


/**
-- 이름(first_name)의 글자수가 6자이상인 사람의 이름을 앞에서 3자만 구하여 소문자로 이름만을 출력하라.
-- substr(str, position, length) : str 문자를 positin 부터 length길이 만큼 표현
-- lower(str)  소문자 변환
-- length(str)  str의 길이
**/
SELECT LOWER(SUBSTR(FIRST_NAME, 1, 3))
FROM EMPLOYEES e
WHERE LENGTH(FIRST_NAME) >= 6;


-- 10번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
SELECT ROUND(AVG(SALARY), 0), MAX(SALARY), COUNT(*) 
FROM EMPLOYEES e
WHERE DEPARTMENT_ID = 10;


-- 각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
SELECT ROUND(AVG(SALARY), 0), MIN(SALARY), MAX(SALARY), COUNT(*) 
FROM EMPLOYEES e
GROUP BY DEPARTMENT_ID;


-- 각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
SELECT DEPARTMENT_ID, JOB_ID, COUNT(*) 
FROM EMPLOYEES e
GROUP BY DEPARTMENT_ID, JOB_ID 
ORDER BY DEPARTMENT_ID


-- 같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
SELECT JOB_ID, COUNT(*)
FROM EMPLOYEES e
GROUP BY JOB_ID
HAVING COUNT(*) >= 4; 


-- 각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
SELECT ROUND(AVG(SALARY), 0), SUM(SALARY), MAX(SALARY), MIN(SALARY)
FROM EMPLOYEES e
GROUP BY DEPARTMENT_ID 
ORDER BY MAX(SALARY) DESC
