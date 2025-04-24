import sqlite3
import pandas as pd

df = pd.read_csv("../data/simulated_mentions.csv")
conn = sqlite3.connect("../data/media.db")

# Create tables
with open("../sql/create_tables.sql") as f:
    conn.executescript(f.read())

# Insert platforms & brands
platforms = df["platform"].unique()
brands = df["brand"].unique()
for p in platforms:
    conn.execute("INSERT OR IGNORE INTO dim_platform (name) VALUES (?)", (p,))
for b in brands:
    conn.execute("INSERT OR IGNORE INTO dim_brand (name) VALUES (?)", (b,))
conn.commit()

# Get ids
platforms_map = {row[1]: row[0] for row in conn.execute("SELECT * FROM dim_platform")}
brands_map = {row[1]: row[0] for row in conn.execute("SELECT * FROM dim_brand")}

# Insert fact rows
for _, row in df.iterrows():
    conn.execute("""
        INSERT INTO fact_mentions (date, platform_id, brand_id, mentions)
        VALUES (?, ?, ?, ?)
    """, (
        row["date"],
        platforms_map[row["platform"]],
        brands_map[row["brand"]],
        row["mentions"]
    ))
conn.commit()
conn.close()
