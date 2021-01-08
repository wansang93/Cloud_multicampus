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


-- �μ���ȣ�� 10���� �μ��� ��� �� �����ȣ, �̸�, ������ ����϶�
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME", SALARY
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 10;


-- �����ȣ�� 7369�� ��� �� �̸�, �Ի���, �μ� ��ȣ�� ����϶�.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME", HIRE_DATE, DEPARTMENT_ID
FROM EMPLOYEES e
WHERE EMPLOYEE_ID = 7369;


-- �̸��� Ellen�� ����� ��� ������ ����϶�.
SELECT *
FROM EMPLOYEES e 
WHERE FIRST_NAME = 'Ellen';


-- �Ի����� 08/04/21�� ����� �̸�, �μ���ȣ, ������ ����϶�.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "NAME", DEPARTMENT_ID, SALARY 
FROM EMPLOYEES e 
WHERE HIRE_DATE >= '20080421';


-- ������ SA_MAN �ƴ� ����� ��� ������ ����϶�.
SELECT * 
FROM EMPLOYEES e
WHERE JOB_ID != 'SA_MAN';


-- �Ի����� 08/04/21 ���Ŀ� �Ի��� ����� ������ ����϶�.
SELECT *
FROM EMPLOYEES e 
WHERE HIRE_DATE > '20080421';


-- �μ���ȣ�� 20,30���� ������ ��� ����� �̸�, �����ȣ, �μ���ȣ�� ����϶�.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", EMPLOYEE_ID, DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID != 20 AND DEPARTMENT_ID != 30;


-- �̸��� S�� �����ϴ� ����� �����ȣ, �̸�, �Ի���, �μ���ȣ�� ����϶�.
SELECT EMPLOYEE_ID, CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", HIRE_DATE, DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE UPPER(FIRST_NAME)  LIKE 'S%'


--�̸��� s�� �����ϰ� ������ ���ڰ� t�� ����� ������ ����϶�.
SELECT *
FROM EMPLOYEES e 
WHERE UPPER(FIRST_NAME) LIKE 'S%T'


-- employees ���̺��� �̸�, �޿�, ��, �Ѿ��� ���Ͽ� �Ѿ� ���� ������ ����϶� �� �󿩱��� NULL�� ����� ����
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, COMMISSION_PCT, SALARY+(COMMISSION_PCT*SALARY) "TOTAL" 
FROM EMPLOYEES e 
WHERE COMMISSION_PCT IS NOT NULL


-- 10�� �μ��� ��� ����鿡�� �޿��� 13%�� ���ʽ��� �����ϱ�� �Ͽ���. �̸�, �޿�, ���ʽ��ݾ�, �μ���ȣ�� ����϶�.
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, (SALARY*13/100) "BONUS", DEPARTMENT_ID
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 10


/**
-- 30�� �μ��� ������ ����Ͽ� �̸�, �μ���ȣ, �޿�, ������ ����϶�. �� ������ �޿��� 150%�� ���ʽ��� �����Ѵ�.
-- ���� = sal*12+(sal*1.5)
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", DEPARTMENT_ID , SALARY, SALARY*12+SALARY*1.5 "ANNUAL_SALARY"
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 30


/**
-- �μ���ȣ�� 20�� �μ��� �ð��� �ӱ��� ����Ͽ� ����϶�. �� 1���� �ٹ��ϼ��� 12���̰� 1�� �ٹ��ð��� 5�ð��̴�.
-- ��¾���� �̸�, �޿�, �ð��� �ӱ�(�Ҽ����� 1��° �ڸ����� �ݿø�)�� ����϶�.
-- �ñ� = sal/�ϼ�/�ð�  -> sal/12/5 
-- round(m, n) m�� �Ҽ��� n�ڸ����� �ݿø�
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, ROUND(SALARY/12/5, 1) "HOURLY" 
FROM EMPLOYEES e 
WHERE DEPARTMENT_ID = 20


/**
-- �޿��� 1500���� 3000������ ����� �޿��� 5%�� ȸ��� �����ϱ�� �Ͽ���. �̸� �̸�, �޿�, ȸ��(-2�ڸ����� �ݿø�)�� ����϶�.
-- ȸ��  = sal * 0.05	
-- -2�ڸ����� �ݿø� : ���� 2��° �ڸ����� �ݿø�.. 100������  
**/
SELECT CONCAT(CONCAT(FIRST_NAME, ' '), LAST_NAME) "FULL_NAME", SALARY, ROUND(SALARY*0.05, -2) "MEMBERSHIP_DUES"
FROM EMPLOYEES e 
WHERE SALARY >= 1500 AND SALARY <= 3000


/**
�Ի��Ϻ��� ���ݱ����� ��¥���� ����϶�. �μ���ȣ, �̸�, �Ի���, ������, �ٹ��ϼ�(�Ҽ�����������), �ٹ����,
�ٹ�����(30�� ����)�� ����϶�.
���� ��¥ : sysdate 
�ٹ� �ϼ� : ���糯¥ - �Ի��� = sysdate - hire_date  -> ��¥ - ��¥ : �ϼ� ����
�ٹ� ��� : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
�ٹ� ���� : �ٹ��ϼ� / 1��(30��)
**/




/**
-- �Ի��Ϸκ��� ���ñ����� �ϼ��� ���Ͽ� �̸�, �Ի���, �ٹ��ϼ��� ����϶�.
-- round(sysdate-hiredate,0) �ٹ��ϼ�
**/



/**
-- �Ի����� 2012�� 7�� 5���� ���·� �̸�, �Ի����� ����϶�.
-- ��¥ ���� �տ� fm �� ���� '0'�� ǥ������ �ʴ´ٴ� ��.. 
-- 'fmYYYY"��" MM"��" DD"��' 
**/



/**
-- �̸�(first_name)�� ���ڼ��� 6���̻��� ����� �̸��� �տ��� 3�ڸ� ���Ͽ� �ҹ��ڷ� �̸����� ����϶�.
-- substr(str, position, length) : str ���ڸ� positin ���� length���� ��ŭ ǥ��
-- lower(str)  �ҹ��� ��ȯ
-- length(str)  str�� ����
**/



-- 10�� �μ� ������ ��դ� �ְ�, ����, �ο����� ���Ͽ� ����϶�


-- �� �μ��� �޿��� ���, �ְ�, ����, �ο����� ���Ͽ� ����϶�.


-- �� �μ��� ���� ������ �ϴ� ����� �ο����� ���Ͽ� �μ���ȣ, ������, �ο����� ����϶�.


-- ���� ������ �ϴ� ����� ���� 4�� �̻��� ������ �ο����� ����϶�.


-- �� �μ��� ��տ���, ��ü����, �ְ����, ��������,�� ���Ͽ� ��տ����� ���������� ����϶�.

