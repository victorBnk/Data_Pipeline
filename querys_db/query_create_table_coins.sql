CREATE TABLE TB_COINS_VALUES(
    pk_id SERIAL PRIMARY KEY,
    coin_name VARCHAR(100),
    coin_code VARCHAR(100),
    dt_date DATE NOT NULL,
    value_opening DECIMAL(30,8),
    value_lowest  DECIMAL(30,8),
    value_highest  DECIMAL(30,8),
    value_volume  DECIMAL(30,8),
    value_quantity  DECIMAL(30,8),
    value_amount BIGINT,
    value_avg_price  DECIMAL(30,8)
)