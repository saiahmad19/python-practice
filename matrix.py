import pandas as pd

data = {
    "name": ["ahmed", "sara", "ali"],
    "age": [45, 30, 60],
    "diagnosis": ["diabetes", "asthma", "hypertension"]
}

df = pd.DataFrame(data)
print(df)