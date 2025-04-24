CREATE TABLE IF NOT EXISTS dim_platform (
    platform_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS dim_brand (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS fact_mentions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    platform_id INTEGER,
    brand_id INTEGER,
    mentions INTEGER,
    FOREIGN KEY (platform_id) REFERENCES dim_platform(platform_id),
    FOREIGN KEY (brand_id) REFERENCES dim_brand(brand_id)
);
