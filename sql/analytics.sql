
SELECT category, AVG(price) AS avg_price
FROM products_clean
GROUP BY category
ORDER BY avg_price DESC;

SELECT
    title,
    category,
    price,
    AVG(price) OVER (PARTITION BY category) AS avg_category_price
FROM products_clean;

SELECT r.id, r.title, c.price_category
FROM products_raw r
JOIN products_clean c
ON r.id = c.id;
