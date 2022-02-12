-- Оценки студентов в группе по предмету на последнем занятии.
SELECT d.discipline, gr.[group], s.student, g.date_of, g.grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN [groups] gr ON gr.id = s.[group]
WHERE d.id = 2 AND gr.id = 3 AND g.date_of = (SELECT MAX(grades.date_of) FROM grades WHERE grades.discipline = d.id);