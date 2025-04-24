# Media Visibility Analytics Project

This project simulates visibility data of Finnish media brands from platforms like Google Trends, Reddit, and job sites. Data is modeled with SQL and can be visualized using e.g. Apache Superset.

## Steps

1. Simulate data:
    ```bash
    cd python/
    python simulate_mentions.py
    ```

2. Load data into SQLite:
    ```bash
    python load_to_sqlite.py
    ```

3. Connect `data/media.db` to Superset as a SQLite DB

4. Import the dataset into Superset and build visualizations per `superset/dashboard_plan.md`
