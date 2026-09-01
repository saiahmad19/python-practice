import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset("titanic")
titanic = titanic.drop(columns=["deck", "class", "embark_town", "alive", "who", "adult_male"])
titanic["sex"] = titanic["sex"].map({"male": 0, "female": 1})
titanic = pd.get_dummies(titanic, columns=["embarked"])
median_age = titanic["age"].median()
titanic["age"] = titanic["age"].fillna(median_age)

y = titanic["survived"]
X = titanic.drop(columns=["survived"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

baseline_accuracy = 1 - y_test.mean()
print("Baseline accuracy (always predict 'did not survive'):", baseline_accuracy)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_predictions = log_model.predict(X_test)
log_accuracy = accuracy_score(y_test, log_predictions)
print("Logistic Regression accuracy:", log_accuracy)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_predictions = tree_model.predict(X_test)
tree_accuracy = accuracy_score(y_test, tree_predictions)
print("Decision Tree accuracy:", tree_accuracy)

forest_model = RandomForestClassifier(random_state=42)
forest_model.fit(X_train, y_train)
forest_predictions = forest_model.predict(X_test)
forest_accuracy = accuracy_score(y_test, forest_predictions)
print("Random Forest accuracy:", forest_accuracy)

new_passenger = pd.DataFrame({
    "pclass": [1],
    "sex": [1],
    "age": [29],
    "sibsp": [0],
    "parch": [0],
    "fare": [100],
    "alone": [True],
    "embarked_C": [False],
    "embarked_Q": [False],
    "embarked_S": [True],
})
prediction = log_model.predict(new_passenger)
print("Prediction for hypothetical passenger (1=survived, 0=did not):", prediction)