# Assingment 6 Wine Quality Dataset: Hypothesis Testing - Neev Jain

### Objective

The purpose of this analysis is to explore relationships between various chemical properties in the Wine Quality dataset. By formlating three hypotheses based on observed patterns in the dataset and tested them using statistical measures and visualizations.

### Libraries and Data Import

We start by importing necessary libraries (`pandas`, `seaborn`, and `matplotlib`) and loading the dataset.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## Exploratory Data Analysis (EDA)

The dataset’s first few rows reveal that each row represents a wine sample, with variables for various chemical properties. There are no missing values(given in the dataset description), which simplifies the analysis.

```python
# Load the dataset
df = pd.read_csv('winequality_white.csv', delimiter=';')

# Exploratory Data Analysis (EDA) - Check dataset structure
print(df.info())
print(df.describe())
```

---

## Hypothesis Testing

### Hypothesis 1: Higher Levels of Citric Acid are Associated with Higher Levels of Fixed Acidity

#### Code

```python
# Hypothesis 1: Citric acid vs Fixed acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='citric_acid', y='fixed_acidity', data=df)
plt.title('Citric Acid vs Fixed Acidity')
plt.xlabel('Citric Acid')
plt.ylabel('Fixed Acidity')
plt.show()

# Correlation coefficient for Hypothesis 1
corr1 = df['citric_acid'].corr(df['fixed_acidity'])
print(corr1)
```

#### Interpretation

- The plot shows a weak positive relation betwen citric acid and fixed acidity
- The correlation coefficient is **0.29**
- This supports the hypothesis till some extent but the relation is not that strong

---

### Hypothesis 2: Wines with Higher Residual Sugar have a Lower pH

#### Code

```python
# Hypothesis 2: Residual sugar vs pH
plt.figure(figsize=(8, 6))
sns.scatterplot(x='residual_sugar', y='pH', data=df)
plt.title('Residual Sugar vs pH')
plt.xlabel('Residual Sugar')
plt.ylabel('pH')
plt.show()

# Correlation coefficient for Hypothesis 2
corr2 = df['residual_sugar'].corr(df['pH'])
print(corr2)
```

#### Interpretation

- The plot shows a minor negative trend, which suggests that as residual sugar increases, pH decreases slightly.
- The correlation coefficient is **-0.19**, which shows a weak negative relationship.

---

### Hypothesis 3: Higher Levels of Sulphates are Correlated with Higher Free Sulfur Dioxide Levels

#### Code

```python
# Hypothesis 3: Sulphates vs Free Sulfur Dioxide
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sulphates', y='free_sulfur_dioxide', data=df)
plt.title('Sulphates vs Free Sulfur Dioxide')
plt.xlabel('Sulphates')
plt.ylabel('Free Sulfur Dioxide')
plt.show()

# Correlation coefficient for Hypothesis 3
corr3 = df['sulphates'].corr(df['free_sulfur_dioxide'])
print(corr3)
```

#### Interpretation

- The plot shows almost no apparent relationship
- The correlation coefficient is **0.06**, indicating almost no correlation. This result does not support the hypothesis, as theres almost no relation between the variables 

---

## Summary of Findings

| Hypothesis                                                                           | Relationship  | Correlation Coefficient | Conclusion       |
| ------------------------------------------------------------------------------------ | ------------- | ----------------------- | ---------------- |
| 1. Higher levels of citric acid are associated with higher levels of fixed acidity.  | Weak Positive | 0.29                    | Weakly supported |
| 2. Wines with higher residual sugar have a lower pH.                                 | Weak Negative | -0.19                   | Weakly supported |
| 3. Higher levels of sulphates are correlated with higher free sulfur dioxide levels. | None          | 0.06                    | Not supported    |

### Conclusion

- I chose these 3 particular hypotesis because these are the ones I could form.
- **Hypothesis 1** and **Hypothesis 2** are weakly supported, indicating some degree of association, though these relationships are not strong.
- **Hypothesis 3** is not supported, suggesting no meaningful relationship between sulphates and free sulfur dioxide levels.
