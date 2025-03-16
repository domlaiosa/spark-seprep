import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
url = 'wine/wine.data'
column_names = ['Class', 'Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 
                'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 
                'Proanthocyanins', 'Color Intensity', 'Hue', 'OD280/OD315', 'Proline']
df = pd.read_csv(url, header=None, names=column_names)

# Visualizing the relationship between Alcohol and Color Intensity
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Alcohol', y='Color Intensity', data=df, hue='Class', palette='deep')
plt.title('Alcohol Content vs. Color Intensity')
plt.xlabel('Alcohol Content')
plt.ylabel('Color Intensity')
plt.show()

# Visualizing the relationship between Magnesium and Total Phenols
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Magnesium', y='Total Phenols', data=df, hue='Class', palette='deep')
plt.title('Magnesium Content vs. Total Phenols')
plt.xlabel('Magnesium Content')
plt.ylabel('Total Phenols')
plt.show()

# Hypothesis Formulation
# Hypothesis 1: There is a correlation between alcohol content and color intensity in wine.
# Hypothesis 2: There is a correlation between magnesium content and total phenols in wine.

# Hypothesis Testing
# Testing correlation between Alcohol and Color Intensity
correlation_alcohol_color = df['Alcohol'].corr(df['Color Intensity'])
print(f"Correlation between Alcohol and Color Intensity: {correlation_alcohol_color}")

# Testing correlation between Magnesium and Total Phenols
correlation_magnesium_phenols = df['Magnesium'].corr(df['Total Phenols'])
print(f"Correlation between Magnesium and Total Phenols: {correlation_magnesium_phenols}")

# Documentation and Reporting
# 1. First, I imported and explored the dataset.
# 2. Next, I visualized the datasets that I was interested in (color intensity, alcohol content, magnesium levels, total phenols) using scatter plots.
# 3. Based on what I saw, I formulated my two hypotheses:
#    - Hypothesis 1: There is a correlation between Alcohol content and Color Intensity.
#    - Hypothesis 2: There is a correlation between Magnesium content and Total Phenols.
# 4. To test each hypothesis, I calculated the correlation coefficients between Alcohol and Color Intensity, as well as Magnesium levels and Total Phenols.

# Summarize the findings
if correlation_alcohol_color > 0:
    print("There is a positive correlation between Alcohol and Color Intensity.")
elif correlation_alcohol_color < 0:
    print("There is a negative correlation between Alcohol and Color Intensity.")
else:
    print("There is no correlation between Alcohol and Color Intensity.")

if correlation_magnesium_phenols > 0:
    print("There is a positive correlation between Magnesium and Total Phenols.")
elif correlation_magnesium_phenols < 0:
    print("There is a negative correlation between Magnesium and Total Phenols.")
else:
    print("There is no correlation between Magnesium and Total Phenols.")

# In the end, I found that there is a positive correlation between Alcohol and Color Intensity
# There is also a positive correlation between Magnesium and Total Phenols.
