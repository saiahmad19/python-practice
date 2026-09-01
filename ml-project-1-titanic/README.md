# Titanic Survival Prediction

A classification project predicting whether a Titanic passenger survived, based on passenger data (class, age, sex, fare, family size, and port of embarkation). Built as Project 1 of a self-directed AI/ML learning roadmap, using scikit-learn.

## What this project does

Given facts about a passenger, the model predicts whether they survived (1) or did not (0). The dataset (891 real passengers) is split into a training set and a held-out test set, so the model is always evaluated on passengers it never saw during training.

## Data cleaning decisions

The raw dataset needed real cleaning before it could be used:

- **age** was missing for 177 of 891 passengers (~20%). Rather than dropping a fifth of the dataset, missing ages were filled with the median age (28), a common, defensible compromise. This does slightly reduce the column's true variance, which is a known trade-off of this approach, not a free fix.
- **deck** was missing for 688 of 891 passengers (~77%). At that level of missingness, filling it in would mean mostly inventing data, so the column was dropped entirely.
- **sex** was mapped from text (male/female) to numbers (0/1), since models require numeric input.
- **embarked** (which port a passenger boarded from - Southampton, Cherbourg, or Queenstown) was one-hot encoded into three separate True/False columns instead of a single 0/1/2 column, to avoid implying a fake numeric order between three categories that have no real ranking.
- **class, embark_town, who, adult_male** were dropped as redundant - each one just restates information already captured by another column (pclass, embarked, sex/age), in a different format.
- **alive** was dropped because it's the same information as the target column (survived), just written as text instead of 0/1. Leaving it in as a feature would let the model "cheat" by reading the answer directly instead of learning a real pattern.
- **alone** was checked directly against the data before deciding what to do with it: it's True exactly when both sibsp and parch are 0, with no exceptions found. It was kept in the final version rather than dropped, since testing showed it gave a small accuracy improvement for two of the three models tried.

## Models compared

Three different classification approaches were trained and evaluated on the same train/test split, so results are directly comparable:

| Model | Test accuracy |
|---|---|
| Baseline (always predict "did not survive") | 58.7% |
| Logistic Regression | 79.9% |
| Decision Tree | 79.3% |
| Random Forest | 82.7% |

The baseline matters as much as the model results: roughly 59-62% of passengers did not survive, so a model that predicts nothing useful and just guesses the majority class every time would already look "accurate" by that percentage alone. All three real models clearly beat this baseline, which is the actual evidence that they learned something real about survival, not just the class imbalance.

Random Forest performed best. A single Decision Tree performed slightly worse than Logistic Regression, likely because a single tree tends to overfit - it can end up memorizing quirks of the specific training passengers rather than a pattern that generalizes. Random Forest fixes this by training many trees on different random slices of the data and averaging their votes, which is consistent with it outperforming the single tree here.

## Sanity check

The trained Logistic Regression model was also tested on one made-up passenger: a 29-year-old, first-class, female passenger traveling alone, boarded at Southampton. The model predicted survival (1), which matches well-documented Titanic history (women and higher-class passengers had substantially higher survival rates). The model was never given any historical information directly - this prediction came purely from patterns in the numbers, which is good independent evidence it learned something real rather than noise.

## What I'd do differently / next

- Try scaling the numeric features (e.g. fare, age), since Logistic Regression can be sensitive to features on very different numeric scales, and this wasn't done here.
- Test a few different random_state values to check how much the exact accuracy numbers depend on which specific passengers ended up in the test set, rather than trusting a single split.
- Try this same pipeline on a dataset from a personal interest area (e.g. customer retention data) now that the core workflow - clean, split, train, evaluate, compare models - is solid.

## Tools used

Python, pandas, seaborn (for the dataset), scikit-learn (LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, train_test_split, accuracy_score).
