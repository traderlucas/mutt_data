CREATE TABLE IF NOT EXISTS coin_history (
    id SERIAL PRIMARY KEY,
    coin_id TEXT NOT NULL,
    date DATE NOT NULL,
    price_usd NUMERIC,
    raw_json JSONB,
    UNIQUE (coin_id, date)
);
