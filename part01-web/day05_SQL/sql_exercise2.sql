/**********************************************************
*	SQL Query & Function Example2
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

/**
--Departments Table Columns
--DEPARTMENT_ID
--DEPARTMENT_NAME
--MANAGER_ID
--LOCATION_ID
**/

/**
50번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
SELECT ROUND(AVG(SALARY), 0), MAX(SALARY), MIN(SALARY), COUNT(*)
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 50;


/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
SELECT ROUND(AVG(SALARY), 0), MAX(SALARY), MIN(SALARY), COUNT(*)
FROM EMPLOYEES e 
GROUP BY DEPARTMENT_ID;


/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
SELECT DEPARTMENT_ID, JOB_ID, COUNT(*) 
FROM EMPLOYEES e
GROUP BY DEPARTMENT_ID, JOB_ID 
ORDER BY DEPARTMENT_ID


/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
SELECT JOB_ID, COUNT(*)
FROM EMPLOYEES e
GROUP BY JOB_ID
HAVING COUNT(*) >= 4; 


/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
SELECT ROUND(AVG(SALARY), 0), SUM(SALARY), MAX(SALARY), MIN(SALARY)
FROM EMPLOYEES e
GROUP BY DEPARTMENT_ID 
ORDER BY MAX(SALARY) DESC


/**
 부서번호, 부서명, 이름, 급여를 출력하라.
**/
SELECT e.DEPARTMENT_ID, d.DEPARTMENT_NAME, CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", e.SALARY
FROM DEPARTMENTS d, EMPLOYEES e
WHERE e.DEPARTMENT_ID = d.DEPARTMENT_ID


/**
이름이 adam인 사원의 부서명을 출력하라.
**/
SELECT d.DEPARTMENT_ID
FROM DEPARTMENTS d, EMPLOYEES e 
WHERE LOWER(e.FIRST_NAME) = 'adam'
AND d.DEPARTMENT_ID = e.DEPARTMENT_ID;


/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하라
'smith'의 매니저는 'ford'이다.
**/
-- SELECT e1.FIRST_NAME ||'의 매니저는 '||e2.FIRST_NAME ||'이다.'
SELECT CONCAT(CONCAT(CONCAT(e1.FIRST_NAME, '의 매니저는 '), e2.FIRST_NAME), '이다.') "매니저"
FROM EMPLOYEES e1, EMPLOYEES e2
WHERE e1.MANAGER_ID = e2.EMPLOYEE_ID;


/**
adam의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하라.
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", DEPARTMENT_ID, SALARY, JOB_ID 
FROM EMPLOYEES e
WHERE JOB_ID IN
(SELECT JOB_ID FROM EMPLOYEES e2 WHERE lower(FIRST_NAME) = 'adam');


/**
50번 부서사람들 중에서 30번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하라.
**/
SELECT e.EMPLOYEE_ID, CONCAT(CONCAT(e.FIRST_NAME, ' '), e.LAST_NAME) "FULL_NAME", e.DEPARTMENT_ID, e.HIRE_DATE
FROM EMPLOYEES e, EMPLOYEES e2
WHERE e.DEPARTMENT_ID = 50
AND e2.JOB_ID IN
(SELECT JOB_ID FROM EMPLOYEES e3 WHERE DEPARTMENT_ID=20)


/**
급여가 30번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하라.
**/
SELECT e.EMPLOYEE_ID, CONCAT(CONCAT(e.FIRST_NAME, ' '), e.LAST_NAME) "FULL_NAME", e.SALARY
FROM EMPLOYEES e
WHERE e.SALARY > ANY
(SELECT MAX(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID=30)