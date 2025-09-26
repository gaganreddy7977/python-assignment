-- -- Questions on WHERE
-- # 25 Questions on WHERE

-- 1. Find customers born after the year 1990.
-- SELECT cust_year_of_birth   from sh.CUSTOMERS
-- where cust_year_of_birth>1990

-- 2. List all male customers (`CUST_GENDER = 'M'`).
-- SELECT CUST_GENDER from sh.CUSTOMERS
-- where CUST_GENDER='M'

-- 3. Retrieve all female customers (`CUST_GENDER = 'F'`) living in Sydney.
-- SELECT CUST_FIRST_NAME,CUST_GENDER,CUST_city from sh.CUSTOMERS 
-- where CUST_GENDER='F' 

-- 4. Find customers with income level `"G: 130,000 - 149,999"`.
-- SELECT CUST_FIRST_NAME,cust_income_level from sh.CUSTOMERS
-- where CUST_INCOME_LEVEL= 'G: 130,000 - 149,999'

-- 5. Get all customers with a credit limit above 10,000.
-- SELECT CUST_FIRST_NAME,CUST_CREDIT_LIMIT from sh.CUSTOMERS
-- where CUST_CREDIT_LIMIT > 10000

-- 6. Retrieve customers from the state "California".
-- select CUST_FIRST_NAME,CUST_STATE_PROVINCE from sh.customers
-- where CUST_STATE_PROVINCE = 'California'


-- 7. Find customers who have provided an email address.
-- select cust_id,CUST_EMAIL from sh.CUSTOMERS

-- 8. List customers with missing marital status.
-- SELECT CUST_FIRST_NAME,cust_marital_status from sh.CUSTOMERS
-- where CUST_MARITAL_STATUS is not NULL

-- 9. Find customers whose postal code starts with "53".
-- select cust_id,cust_postal_code  from sh.customers
-- where CUST_POSTAL_CODE like ('53%')

-- 10. Get customers born before 1980 with a credit limit above 5,000.
-- SELECT  cust_id,cust_year_of_birth,CUST_CREDIT_LIMIT from sh.CUSTOMERS
-- where CUST_YEAR_OF_BIRTH<1980 and CUST_CREDIT_LIMIT>5000

-- 11. Retrieve customers from Almere or Amersfoort.
-- SELECT cust_id,CUST_city from sh.CUSTOMERS
-- where CUST_CITY in 'Almere'or CUST_CITY='Amersfoort'

-- 12. Find customers who do not have a credit limit.
-- SELECT cust_id,CUST_CREDIT_LIMIT from sh.CUSTOMERS
-- where CUST_CREDIT_LIMIT is not  NULL

-- 13. List customers whose phone number starts with "487".
-- SELECT cust_id,cust_main_phone_number from sh.CUSTOMERS
-- where CUST_MAIN_PHONE_NUMBER like '487%'

-- 14. Find married customers with income level `"Medium"`.
-- SELECT cust_id,cust_marital_status,cust_income_level from sh.CUSTOMERS
-- where CUST_INCOME_LEVEL in 'Medium'

-- 15. Get customers whose last name starts with "G".
-- select cust_id,cust_last_name from sh.customers
-- where cust_last_name like 'G%'

-- 16. Find customers with city_id = 51057.
-- SELECT cust_id,CUST_CITY_ID from sh.CUSTOMERS
-- where CUST_CITY_ID like '51057'

-- 17. Retrieve all customers who are valid (`CUST_VALID = 'A'`).
-- SELECT cust_id,cust_valid FROM sh.CUSTOMERS
-- where CUST_VALID='A'

-- 18. Find customers whose effective start date (`CUST_EFF_FROM`) is after 2020.
-- SELECT cust_id,CUST_EFF_FROM from sh.CUSTOMERS
-- where CUST_EFF_FROM  > 'DATE 2020' ###########################################################################################

-- 19. Retrieve customers whose effective end date (`CUST_EFF_TO`) is before 2021.
-- select cust_id,cust_eff_to from sh.CUSTOMERS
-- where CUST_EFF_TO < 'DATE 2021'


-- 20. Find customers with credit limit between 5,000 and 9,000.
-- SELECT cust_id,CUST_CREDIT_LIMIT from sh.CUSTOMERS
-- where CUST_CREDIT_LIMIT BETWEEN 5000 and 9000

-- 21. Get all customers from country_id = 101.
-- SELECT cust_id,country_id from sh.CUSTOMERS
-- where COUNTRY_ID=101

-- 22. Find customers whose email ends with `"@company.example.com"`.
-- select cust_id,CUST_EMAIL from sh.customers
-- where CUST_EMAIL like '%@company.example.com'

-- 23. List customers with `CUST_TOTAL_ID = 52772`.
-- SELECT cust_id,CUST_TOTAL_ID from sh.CUSTOMERS
-- where CUST_TOTAL_ID=52772

-- 24. Find customers with `CUST_SRC_ID` in (10, 20, 30).
-- SELECT cust_id,CUST_SRC_ID from sh.CUSTOMERS
-- where CUST_SRC_ID in (10, 20, 30)

-- 25. Retrieve customers who either do not have email or do not have a credit limit.
SELECT cust_id,CUST_EMAIL,CUST_CREDIT_LIMIT FROM sh.customers
where CUST_EMAIL is  Null and CUST_CREDIT_LIMIT is  NULL

-- ---

-- # 25 Questions on GROUP BY and HAVING

-- 26. Count the number of customers in each city.
-- 27. Find cities with more than 100 customers.
-- 28. Count the number of customers in each state.
-- 29. Find states with fewer than 50 customers.
-- 30. Calculate the average credit limit of customers in each city.
-- 31. Find cities with average credit limit greater than 8,000.
-- 32. Count customers by marital status.
-- 33. Find marital statuses with more than 200 customers.
-- 34. Calculate the average year of birth grouped by gender.
-- 35. Find genders with average year of birth after 1990.
-- 36. Count the number of customers in each country.
-- 37. Find countries with more than 1,000 customers.
-- 38. Calculate the total credit limit per state.
-- 39. Find states where the total credit limit exceeds 100,000.
-- 40. Find the maximum credit limit for each income level.
-- 41. Find income levels where the maximum credit limit is greater than 15,000.
-- 42. Count customers by year of birth.
-- 43. Find years of birth with more than 50 customers.
-- 44. Calculate the average credit limit per marital status.
-- 45. Find marital statuses with average credit limit less than 5,000.
-- 46. Count the number of customers by email domain (e.g., `company.example.com`).
-- 47. Find email domains with more than 300 customers.
-- 48. Calculate the average credit limit by validity (`CUST_VALID`).
-- 49. Find validity groups where the average credit limit is greater than 7,000.
-- 50. Count the number of customers per state and city combination where there are more than 50 customers.