-- Список курсов, которые студенту читает преподаватель.
SELECT DISTINCT s.student, t.teacher, d.discipline 
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN teachers t ON t.id = d.teacher
WHERE g.student = 12 AND t.id = 2;