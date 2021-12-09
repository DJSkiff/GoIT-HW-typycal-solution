-- 5 студентов с наибольшим средним баллом по всем предметам
SELECT s.student,
    round(avg(g.grade), 2) AS avg_grade
FROM grades g
    LEFT JOIN students s ON s.id = g.student
GROUP BY s.id
ORDER BY (round(avg(g.grade), 2)) DESC
LIMIT 5;