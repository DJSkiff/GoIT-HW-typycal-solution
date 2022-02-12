-- Средний балл, который ставит преподаватель.
SELECT DISTINCT t.teacher, round(avg(grade), 2) AS avg_grade
FROM grades g
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN teachers t ON t.id = d.teacher
WHERE t.id = 2
GROUP BY t.teacher;