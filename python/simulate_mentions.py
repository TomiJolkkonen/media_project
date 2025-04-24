import pandas as pd
import random
from datetime import datetime, timedelta

platforms = ["Google Trends", "Reddit", "Twitter", "Duunitori"]
brands = ["Nelonen", "MTV", "Bauermedia", "Yle"]
start_date = datetime(2023, 1, 1)
data = []

for i in range(52):  # viikoittain vuoden ajalta
    date = start_date + timedelta(weeks=i)
    for platform in platforms:
        for brand in brands:
            mentions = random.randint(50, 500)
            data.append([date.date(), platform, brand, mentions])

df = pd.DataFrame(data, columns=["date", "platform", "brand", "mentions"])
df.to_csv("../data/simulated_mentions.csv", index=False)
