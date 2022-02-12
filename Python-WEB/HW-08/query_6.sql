-- Список студентов в группе.
SELECT g.[group], s.student
FROM students s
LEFT JOIN [groups] g ON g.id = s.[group]
WHERE g.id = 1;