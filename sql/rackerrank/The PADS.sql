/*
Enter your query here.
*/
SELECT CONCAT(NAME, '(', SUBSTRING(OCCUPATION, 1, 1),')')
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are total ',COUNT(OCCUPATION), ' ', CONCAT(LOWER(OCCUPATION),'s.'))
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;