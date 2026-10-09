import seaborn as sns
import sqlite3
import pandas as pd


titanic = sns.load_dataset("titanic")

connection = sqlite3.connect("titanic.db")
titanic.to_sql("passengers", connection, if_exists="replace", index=False)

result = connection.execute("SELECT sex, age FROM passengers WHERE age > 50 LIMIT 5")
for row in result:
    print(row)

result = connection.execute("SELECT pclass, AVG(survived) FROM passengers GROUP BY pclass")
for row in result:
    print(row)

fare_categories = pd.DataFrame({
    "pclass": [1, 2, 3],
    "fare_category": ["Expensive", "Moderate", "Cheap"]
})
fare_categories.to_sql("fare_info", connection, if_exists="replace", index=False)

result = connection.execute("""
    SELECT passengers.pclass, passengers.age, fare_info.fare_category
    FROM passengers
    JOIN fare_info ON passengers.pclass = fare_info.pclass
    LIMIT 5
""")
for row in result:
    print(row)