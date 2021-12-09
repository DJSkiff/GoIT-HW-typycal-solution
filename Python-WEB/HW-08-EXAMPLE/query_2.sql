-- Выберем количество сотрудников по компаниям
SELECT COUNT(*),
    c.company_name
FROM employees e
    LEFT JOIN companies c ON e.company = c.id
GROUP BY c.id;