CREATE TABLE IF NOT EXISTS coin_aggregates (
    id SERIAL PRIMARY KEY,
    coin_id TEXT NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    max_price NUMERIC,
    min_price NUMERIC,
    UNIQUE (coin_id, year, month)
);

--  coin id, the year and month and
-- the maximum/minimum values