-- Средний балл, который преподаватель ставит студенту.
SELECT DISTINCT s.student, t.teacher, round(avg(grade), 2) AS avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN teachers t ON t.id = d.teacher
WHERE g.student = 13 AND t.id = 2
GROUP BY s.student, t.teacher;