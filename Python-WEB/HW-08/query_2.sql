-- 1 студент с наивысшим средним баллом по одному предмету.
SELECT d.discipline, s.student, round(avg(g.grade), 2) AS grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
WHERE d.id = ?
GROUP BY s.id, d.id
ORDER BY (round(avg(g.grade), 2)) DESC
LIMIT 1;