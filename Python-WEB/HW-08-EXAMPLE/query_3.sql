--выберем сотрудников компаний у которых в 7 месяце была зарплата > 5000
SELECT c.company_name, e.employee, e.post, p.total
FROM companies c
    LEFT JOIN employees e ON e.company = c.id
    LEFT JOIN payments p ON p.employee = e.id
WHERE p.total > 5000
    and date_of = '2021-07-07'