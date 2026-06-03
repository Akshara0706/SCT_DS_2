# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("train.csv")

# -----------------------------
# DATA OVERVIEW
# -----------------------------

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Age missing values using median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill Embarked missing values
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Fill Cabin missing values
df['Cabin'].fillna("Unknown", inplace=True)

# Duplicate Check
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# -----------------------------
# EXPLORATORY DATA ANALYSIS
# -----------------------------

# Survival Distribution
plt.figure(figsize=(6,4))

sns.countplot(
    x='Survived',
    data=df,
    palette='Set2'
)

plt.title("Survival Distribution")
plt.xlabel("0 = Not Survived | 1 = Survived")
plt.show()

# -----------------------------
# Gender vs Survival
# -----------------------------

plt.figure(figsize=(7,5))

sns.countplot(
    x='Sex',
    hue='Survived',
    data=df
)

plt.title("Gender vs Survival")

plt.show()

# -----------------------------
# Passenger Class vs Survival
# -----------------------------

plt.figure(figsize=(7,5))

sns.countplot(
    x='Pclass',
    hue='Survived',
    data=df
)

plt.title("Passenger Class vs Survival")

plt.show()

# -----------------------------
# Age Distribution
# -----------------------------

plt.figure(figsize=(8,5))

sns.histplot(
    df['Age'],
    bins=30,
    kde=True
)

plt.title("Age Distribution")

plt.show()

# -----------------------------
# Fare Distribution
# -----------------------------

plt.figure(figsize=(8,5))

sns.histplot(
    df['Fare'],
    bins=40,
    kde=True
)

plt.title("Fare Distribution")

plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,7))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# Age vs Survival Boxplot
# -----------------------------

plt.figure(figsize=(8,5))

sns.boxplot(
    x='Survived',
    y='Age',
    data=df
)

plt.title("Age vs Survival")

plt.show()

# -----------------------------
# Embarked vs Survival
# -----------------------------

plt.figure(figsize=(7,5))

sns.countplot(
    x='Embarked',
    hue='Survived',
    data=df
)

plt.title("Embarked Port vs Survival")

plt.show()