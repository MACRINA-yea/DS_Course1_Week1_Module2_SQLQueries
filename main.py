import sqlite3
import pandas as pd

conn = sqlite3.connect("planets.db")

# Planets with no moons
df_no_moons = pd.read_sql("SELECT * FROM planets WHERE num_of_moons = 0", conn)

# Planets whose name has 7 letters (Mercury, Jupiter, Neptune)
df_name_seven = pd.read_sql("SELECT name FROM planets WHERE LENGTH(name) = 7", conn)