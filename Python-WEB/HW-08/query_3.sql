-- Cредний балл в группе по одному предмету.
SELECT d.discipline, gr.[group], round(avg(g.grade), 2) AS grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN disciplines d ON d.id = g.discipline
LEFT JOIN [groups] gr ON gr.id = s.[group]
WHERE d.id = 2
GROUP BY gr.id
ORDER BY (round(avg(g.grade), 2)) DESC;