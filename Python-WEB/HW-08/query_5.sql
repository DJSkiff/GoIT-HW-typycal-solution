-- Какие курсы читает преподаватель.
SELECT t.teacher, d.discipline
FROM teachers t
LEFT JOIN disciplines d ON d.teacher = t.id
WHERE t.id = 1;
