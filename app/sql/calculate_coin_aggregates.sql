INSERT INTO coin_aggregates (coin_id, year, month, max_price, min_price)
SELECT
    coin_id,
    EXTRACT(YEAR FROM date)::INT AS year,
    EXTRACT(MONTH FROM date)::INT AS month,
    MAX(price_usd) AS max_price,
    MIN(price_usd) AS min_price
FROM coin_history
GROUP BY coin_id, year, month
ON CONFLICT (coin_id, year, month)
DO UPDATE SET
    max_price = EXCLUDED.max_price,
    min_price = EXCLUDED.min_price;

--check on the upsert logic