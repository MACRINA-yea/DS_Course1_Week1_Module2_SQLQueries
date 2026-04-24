import sqlite3
import pandas as pd

# Planets database
conn1 = sqlite3.connect("planets.db")

# Step 1 - planets with no moons
df_no_moons = pd.read_sql("SELECT * FROM planets WHERE num_of_moons = 0", conn1)

# Step 2 - planets with 7-letter names (name and mass)
df_name_seven = pd.read_sql("SELECT name, mass FROM planets WHERE name LIKE '_______'", conn1)

# Step 3 - name and mass where mass <= 1.00
df_mass = pd.read_sql("SELECT name, mass FROM planets WHERE mass <= 1.00", conn1)

# Step 4 - all columns, at least one moon and mass < 1.00
df_mass_moon = pd.read_sql("SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00", conn1)

# Step 5 - name and color where color contains 'blue'
df_blue = pd.read_sql("SELECT name, color FROM planets WHERE color LIKE '%blue%'", conn1)

# Dogs database
conn2 = sqlite3.connect("dogs.db")

# Step 6 - hungry dogs sorted youngest to oldest
df_hungry = pd.read_sql("SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC", conn2)

# Step 7 - hungry dogs aged 2-7, sorted alphabetically
df_hungry_ages = pd.read_sql("SELECT name, age, hungry FROM dogs WHERE age BETWEEN 2 AND 7 AND hungry = 1 ORDER BY name ASC", conn2)

# Step 8 - 4 oldest dogs sorted by breed
df_4_oldest = pd.read_sql("SELECT name, age, breed FROM dogs ORDER BY age DESC, breed ASC LIMIT 4", conn2)

# Babe Ruth database
conn3 = sqlite3.connect("babe_ruth.db")

# Step 9 - total years played
df_ruth_years = pd.read_sql("SELECT COUNT(year) AS total_years FROM babe_ruth_stats", conn3)

# Step 10 - total homeruns (HR column)
df_hr_total = pd.read_sql("SELECT SUM(HR) AS total_homeruns FROM babe_ruth_stats", conn3)

# Step 11 - team and number of years per team
df_teams_years = pd.read_sql("SELECT team, COUNT(year) AS number_years FROM babe_ruth_stats GROUP BY team", conn3)

# Step 12 - team and average at bats where avg > 200
df_at_bats = pd.read_sql("SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200", conn3)