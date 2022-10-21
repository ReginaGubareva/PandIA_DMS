import sqlite3
import pandas as pd

df = pd.read_csv("../../../PandIA project/PandIA exploratory analysis/data/water/braganca/main.csv")


conn = sqlite3.connect('../identifier.sqlite')
cur = conn.cursor()

df.to_sql(name='water_braganca', con=conn, if_exists='append')