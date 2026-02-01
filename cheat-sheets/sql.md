# SQL Cheat Sheet for Data Analysis 🗄️

Essential SQL commands for data analysis and querying databases.

## Basic SELECT Queries

```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with alias
SELECT column1 AS col1, column2 AS col2 FROM table_name;

-- Select distinct values
SELECT DISTINCT column1 FROM table_name;

-- Limit results
SELECT * FROM table_name LIMIT 10;
```

## WHERE Clause (Filtering)

```sql
-- Basic conditions
SELECT * FROM table_name WHERE column1 = 'value';
SELECT * FROM table_name WHERE column1 > 100;
SELECT * FROM table_name WHERE column1 != 'value';

-- Multiple conditions
SELECT * FROM table_name WHERE column1 = 'value' AND column2 > 100;
SELECT * FROM table_name WHERE column1 = 'value' OR column2 = 'other';

-- IN operator
SELECT * FROM table_name WHERE column1 IN ('value1', 'value2', 'value3');

-- BETWEEN operator
SELECT * FROM table_name WHERE column1 BETWEEN 10 AND 20;

-- LIKE operator (pattern matching)
SELECT * FROM table_name WHERE column1 LIKE 'A%';      -- Starts with A
SELECT * FROM table_name WHERE column1 LIKE '%Z';      -- Ends with Z
SELECT * FROM table_name WHERE column1 LIKE '%pattern%'; -- Contains pattern

-- NULL checks
SELECT * FROM table_name WHERE column1 IS NULL;
SELECT * FROM table_name WHERE column1 IS NOT NULL;
```

## Sorting (ORDER BY)

```sql
-- Sort ascending (default)
SELECT * FROM table_name ORDER BY column1;

-- Sort descending
SELECT * FROM table_name ORDER BY column1 DESC;

-- Multiple columns
SELECT * FROM table_name ORDER BY column1 ASC, column2 DESC;
```

## Aggregate Functions

```sql
-- Count
SELECT COUNT(*) FROM table_name;
SELECT COUNT(DISTINCT column1) FROM table_name;

-- Sum
SELECT SUM(column1) FROM table_name;

-- Average
SELECT AVG(column1) FROM table_name;

-- Min/Max
SELECT MIN(column1), MAX(column1) FROM table_name;

-- Multiple aggregates
SELECT 
    COUNT(*) AS total_rows,
    AVG(column1) AS avg_value,
    SUM(column2) AS total_sum
FROM table_name;
```

## GROUP BY

```sql
-- Basic grouping
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;

-- Multiple columns
SELECT column1, column2, AVG(column3)
FROM table_name
GROUP BY column1, column2;

-- With HAVING (filter groups)
SELECT column1, COUNT(*) AS count
FROM table_name
GROUP BY column1
HAVING COUNT(*) > 5;

-- ORDER BY with GROUP BY
SELECT column1, SUM(column2) AS total
FROM table_name
GROUP BY column1
ORDER BY total DESC;
```

## JOINS

### INNER JOIN
```sql
SELECT a.column1, b.column2
FROM table_a AS a
INNER JOIN table_b AS b ON a.id = b.id;
```

### LEFT JOIN
```sql
SELECT a.column1, b.column2
FROM table_a AS a
LEFT JOIN table_b AS b ON a.id = b.id;
```

### RIGHT JOIN
```sql
SELECT a.column1, b.column2
FROM table_a AS a
RIGHT JOIN table_b AS b ON a.id = b.id;
```

### FULL OUTER JOIN
```sql
SELECT a.column1, b.column2
FROM table_a AS a
FULL OUTER JOIN table_b AS b ON a.id = b.id;
```

### CROSS JOIN
```sql
SELECT a.column1, b.column2
FROM table_a AS a
CROSS JOIN table_b AS b;
```

### Self Join
```sql
SELECT a.column1, b.column2
FROM table_name AS a
JOIN table_name AS b ON a.id = b.parent_id;
```

## Subqueries

### In WHERE clause
```sql
SELECT * FROM table_name
WHERE column1 IN (
    SELECT column1 FROM other_table WHERE condition
);
```

### In FROM clause
```sql
SELECT subquery.column1, COUNT(*)
FROM (
    SELECT column1, column2 FROM table_name WHERE condition
) AS subquery
GROUP BY subquery.column1;
```

### Correlated subquery
```sql
SELECT column1, column2
FROM table_a AS a
WHERE column1 > (
    SELECT AVG(column1) FROM table_b WHERE table_b.id = a.id
);
```

## UNION

```sql
-- Combine results (remove duplicates)
SELECT column1 FROM table_a
UNION
SELECT column1 FROM table_b;

-- Keep duplicates
SELECT column1 FROM table_a
UNION ALL
SELECT column1 FROM table_b;
```

## CASE Statements

```sql
-- Simple CASE
SELECT 
    column1,
    CASE 
        WHEN column2 > 100 THEN 'High'
        WHEN column2 > 50 THEN 'Medium'
        ELSE 'Low'
    END AS category
FROM table_name;

-- CASE in aggregation
SELECT 
    SUM(CASE WHEN column1 = 'A' THEN 1 ELSE 0 END) AS count_a,
    SUM(CASE WHEN column1 = 'B' THEN 1 ELSE 0 END) AS count_b
FROM table_name;
```

## Window Functions

### ROW_NUMBER
```sql
SELECT 
    column1,
    column2,
    ROW_NUMBER() OVER (ORDER BY column2 DESC) AS row_num
FROM table_name;
```

### RANK and DENSE_RANK
```sql
SELECT 
    column1,
    column2,
    RANK() OVER (ORDER BY column2 DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY column2 DESC) AS dense_rank
FROM table_name;
```

### PARTITION BY
```sql
SELECT 
    column1,
    column2,
    AVG(column2) OVER (PARTITION BY column1) AS avg_by_group
FROM table_name;
```

### LAG and LEAD
```sql
SELECT 
    date_column,
    value,
    LAG(value, 1) OVER (ORDER BY date_column) AS previous_value,
    LEAD(value, 1) OVER (ORDER BY date_column) AS next_value
FROM table_name;
```

### Running Total
```sql
SELECT 
    date_column,
    amount,
    SUM(amount) OVER (ORDER BY date_column) AS running_total
FROM table_name;
```

## String Functions

```sql
-- Concatenate
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- Length
SELECT LENGTH(column1) FROM table_name;

-- Upper/Lower case
SELECT UPPER(column1), LOWER(column1) FROM table_name;

-- Substring
SELECT SUBSTRING(column1, 1, 5) FROM table_name;

-- Replace
SELECT REPLACE(column1, 'old', 'new') FROM table_name;

-- Trim
SELECT TRIM(column1), LTRIM(column1), RTRIM(column1) FROM table_name;
```

## Date Functions

```sql
-- Current date/time
SELECT NOW(), CURRENT_DATE, CURRENT_TIME;

-- Extract parts
SELECT 
    YEAR(date_column),
    MONTH(date_column),
    DAY(date_column),
    HOUR(timestamp_column)
FROM table_name;

-- Date arithmetic
SELECT DATE_ADD(date_column, INTERVAL 7 DAY) FROM table_name;
SELECT DATEDIFF(date1, date2) FROM table_name;

-- Format date
SELECT DATE_FORMAT(date_column, '%Y-%m-%d') FROM table_name;
```

## Mathematical Functions

```sql
-- Basic math
SELECT ROUND(column1, 2) FROM table_name;
SELECT CEIL(column1), FLOOR(column1) FROM table_name;
SELECT ABS(column1) FROM table_name;

-- Power and square root
SELECT POWER(column1, 2), SQRT(column1) FROM table_name;

-- Modulo
SELECT MOD(column1, 10) FROM table_name;
```

## Common Table Expressions (CTE)

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name WHERE column1 > 10;

-- Multiple CTEs
WITH 
    cte1 AS (SELECT * FROM table_a WHERE condition),
    cte2 AS (SELECT * FROM table_b WHERE condition)
SELECT * FROM cte1 JOIN cte2 ON cte1.id = cte2.id;
```

## Data Modification

### INSERT
```sql
-- Single row
INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');

-- Multiple rows
INSERT INTO table_name (column1, column2) 
VALUES 
    ('value1', 'value2'),
    ('value3', 'value4');

-- From SELECT
INSERT INTO table_name (column1, column2)
SELECT column1, column2 FROM other_table WHERE condition;
```

### UPDATE
```sql
UPDATE table_name
SET column1 = 'new_value', column2 = 100
WHERE condition;
```

### DELETE
```sql
DELETE FROM table_name WHERE condition;
```

## CREATE TABLE

```sql
CREATE TABLE table_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    column1 VARCHAR(255) NOT NULL,
    column2 INT DEFAULT 0,
    column3 DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Indexes

```sql
-- Create index
CREATE INDEX idx_column1 ON table_name(column1);

-- Create unique index
CREATE UNIQUE INDEX idx_unique ON table_name(column1);

-- Drop index
DROP INDEX idx_column1 ON table_name;
```

## Views

```sql
-- Create view
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;

-- Use view
SELECT * FROM view_name;

-- Drop view
DROP VIEW view_name;
```

## Common Data Analysis Patterns

### Top N per Group
```sql
SELECT * FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY value DESC) AS rn
    FROM table_name
) AS ranked
WHERE rn <= 5;
```

### Pivot Table (Cross Tabulation)
```sql
SELECT 
    category,
    SUM(CASE WHEN month = 'Jan' THEN value ELSE 0 END) AS Jan,
    SUM(CASE WHEN month = 'Feb' THEN value ELSE 0 END) AS Feb,
    SUM(CASE WHEN month = 'Mar' THEN value ELSE 0 END) AS Mar
FROM table_name
GROUP BY category;
```

### Running Average
```sql
SELECT 
    date,
    value,
    AVG(value) OVER (
        ORDER BY date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM table_name;
```

### Percent of Total
```sql
SELECT 
    category,
    value,
    value * 100.0 / SUM(value) OVER () AS percent_of_total
FROM table_name;
```

### Year-over-Year Comparison
```sql
SELECT 
    date,
    value,
    LAG(value, 12) OVER (ORDER BY date) AS value_last_year,
    value - LAG(value, 12) OVER (ORDER BY date) AS yoy_change
FROM monthly_data;
```

## Performance Tips

1. **Use indexes** on columns in WHERE, JOIN, and ORDER BY clauses
2. **Avoid SELECT *** - specify only needed columns
3. **Use LIMIT** when testing queries
4. **Filter early** in subqueries
5. **Use appropriate JOIN types**
6. **Avoid functions** on indexed columns in WHERE clauses
7. **Use EXPLAIN** to analyze query performance

## Quick Reference

| Operation | Code |
|-----------|------|
| Select all | `SELECT * FROM table` |
| Filter | `WHERE column = value` |
| Sort | `ORDER BY column DESC` |
| Group | `GROUP BY column` |
| Count | `COUNT(*)` |
| Average | `AVG(column)` |
| Join | `JOIN table ON a.id = b.id` |
| Distinct | `SELECT DISTINCT column` |
| Top 10 | `LIMIT 10` |
| Create view | `CREATE VIEW name AS SELECT...` |

---
[← Back to Main](../README.md)
