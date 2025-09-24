USE finsent_db;

-- Vérifier les tables
SHOW TABLES;

-- Vérifier les colonnes et PK
DESCRIBE StockPrices;
DESCRIBE YahooAPI;
DESCRIBE Events;
DESCRIBE NewsArticles;

-- Vérifier les FK
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    information_schema.KEY_COLUMN_USAGE
WHERE
    TABLE_SCHEMA = 'finsent_db' AND
    REFERENCED_TABLE_NAME IS NOT NULL;
