PRAGMA foreign_keys = off;
BEGIN TRANSACTION;
-- Table: companies
DROP TABLE IF EXISTS companies;
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name STRING UNIQUE NOT NULL
);
-- Table: employees
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    employee STRING UNIQUE NOT NULL,
    post STRING NOT NULL,
    company REFERENCES companies (id)
);
-- Table: payments
DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee REFERENCES employees (id),
    date_of DATE NOT NULL,
    total INTEGER NOT NULL
);
COMMIT TRANSACTION;
PRAGMA foreign_keys = on;