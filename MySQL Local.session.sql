

CREATE Table IF NOT EXISTS Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
);

INSERT INTO Customers VALUES
(1, 'Rahul', 'Delhi'),
(2, 'Priya', 'Mumbai'),
(3, 'Aman', 'Dehradun'),
(4, 'Sneha', 'Pune'),
(5, 'Arjun', 'Delhi');

INSERT INTO Orders VALUES
(101, 1, '2026-01-10', 2000),
(102, 2, '2026-01-12', 1500),
(103, 1, '2026-02-05', 3000),
(104, 3, '2026-02-10', 1000),
(105, 4, '2026-02-15', 4500),
(106, 2, '2026-03-01', 2500),
(107, 5, '2026-03-05', 500),
(108, 4, '2026-03-12', 1500);

SELECT * FROM Customers;
-- ANALYSIS 1: View all orders
SELECT * FROM Orders;

-- ANALYSIS 2: Find the top 5 customers by spending
SELECT c.customer_id, c.customer_name,
       SUM(o.amount) AS total_spent
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

-- ANALYSIS 3: Calculate average order value
SELECT AVG(amount) AS average_order_value
FROM Orders;

-- ANALYSIS 4: Calculate total revenue and orders
SELECT COUNT(*) AS total_orders,
       SUM(amount) AS total_revenue
FROM Orders;

-- ANALYSIS 5: Find average order value for each customer
SELECT c.customer_name,
       AVG(o.amount) AS average_order_value
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY average_order_value DESC;

-- ANALYSIS 6: Categorize orders using CASE
SELECT order_id, amount,
       CASE
           WHEN amount >= 3000 THEN 'High Value'
           WHEN amount >= 1500 THEN 'Medium Value'
           ELSE 'Low Value'
       END AS order_category
FROM Orders;

-- ANALYSIS 7: Find orders above the average order value
SELECT order_id, customer_id, amount
FROM Orders
WHERE amount > (
    SELECT AVG(amount)
    FROM Orders
)
ORDER BY amount DESC;

