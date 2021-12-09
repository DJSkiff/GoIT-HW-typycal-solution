-- Выберем среднюю зарплату по должностям
SELECT AVG(p.total),
    e.post
FROM payments p
    LEFT JOIN employees e ON p.employee = e.id
GROUP BY e.post;