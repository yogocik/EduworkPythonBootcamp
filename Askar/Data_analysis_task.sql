USE data_analyst; -- import the database

WITH ORDERS AS(
    SELECT
        DATE_FORMAT(DATE(created_at), '%Y-%m-01') as month,
        COUNT(order_id) as total_orders,
        SUM(num_of_item) as total_items
    FROM orders
    WHERE YEAR(created_at) = 2023 AND status = 'Complete'
    GROUP BY 1
    ORDER BY 1
),
PREVIOUS AS(
    SELECT *,
        LAG(total_orders, 1) OVER(ORDER BY month) as previous_total_orders,
        LAG(total_items, 1) OVER(ORDER BY month) as previous_total_items
    FROM ORDERS
    ORDER BY month
),
GROWTH AS(
    SELECT *,
    CASE
        WHEN previous_total_orders is not null THEN
        -- USE CONCAT for insert a symbol, and for this case is %
        -- USE ROUND for take just 2 decimal number
        CONCAT(ROUND((total_orders-previous_total_orders)/previous_total_orders * 100, 2),'%')
    ELSE null END as total_orders_growth,
    CASE
        WHEN previous_total_items is not null THEN
        CONCAT(ROUND((total_items-previous_total_items)/previous_total_items * 100, 2),'%')
    ELSE null END as total_items_growth
    FROM PREVIOUS
)
SELECT * FROM GROWTH