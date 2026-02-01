# Exploratory Data Analysis (EDA) Guide 🔍

A comprehensive guide to exploring and understanding your data.

## 1. Initial Data Overview

### Load and Inspect
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')

# Basic info
print(df.shape)              # Dimensions
print(df.head(10))           # First 10 rows
print(df.tail(10))           # Last 10 rows
print(df.info())             # Column types and non-null counts
print(df.describe())         # Statistical summary
print(df.columns.tolist())   # Column names
```

### Data Structure
```python
# Data types
print(df.dtypes)

# Memory usage
print(df.memory_usage(deep=True))

# Index information
print(df.index)

# Column statistics
print(df.describe(include='all'))  # Include all types
```

## 2. Data Quality Assessment

### Missing Values
```python
# Count missing values
missing = df.isna().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'column': missing.index,
    'missing_count': missing.values,
    'missing_percentage': missing_pct.values
})
print(missing_df[missing_df.missing_count > 0].sort_values('missing_count', ascending=False))

# Visualize missing data
import missingno as msno
msno.matrix(df)
plt.show()

msno.heatmap(df)
plt.show()
```

### Duplicates
```python
# Check for duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")

# Show duplicate rows
duplicates = df[df.duplicated(keep=False)]
print(duplicates)

# Check duplicates on specific columns
print(f"Duplicate IDs: {df.duplicated(subset=['id']).sum()}")
```

### Data Types
```python
# Check data types
print(df.dtypes.value_counts())

# Identify potential type issues
for col in df.columns:
    if df[col].dtype == 'object':
        print(f"\n{col}:")
        print(df[col].head())
```

## 3. Univariate Analysis

### Numerical Variables

#### Distribution Analysis
```python
# For each numerical column
for col in df.select_dtypes(include=[np.number]).columns:
    print(f"\n{col}:")
    print(f"Mean: {df[col].mean():.2f}")
    print(f"Median: {df[col].median():.2f}")
    print(f"Std: {df[col].std():.2f}")
    print(f"Min: {df[col].min():.2f}")
    print(f"Max: {df[col].max():.2f}")
    print(f"Skewness: {df[col].skew():.2f}")
    print(f"Kurtosis: {df[col].kurtosis():.2f}")
```

#### Visualizations
```python
# Histogram
df['column'].hist(bins=30, edgecolor='black')
plt.title('Distribution of Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Box plot
df.boxplot(column='column')
plt.show()

# Distribution plot with KDE
sns.histplot(data=df, x='column', kde=True)
plt.show()

# Q-Q plot (check normality)
from scipy import stats
stats.probplot(df['column'].dropna(), dist="norm", plot=plt)
plt.show()
```

#### Multiple Distributions
```python
# All numerical columns
df.select_dtypes(include=[np.number]).hist(figsize=(15, 10), bins=30)
plt.tight_layout()
plt.show()

# Using seaborn
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
axes = axes.ravel()
numeric_cols = df.select_dtypes(include=[np.number]).columns

for i, col in enumerate(numeric_cols[:9]):
    sns.histplot(data=df, x=col, kde=True, ax=axes[i])
    axes[i].set_title(f'Distribution of {col}')

plt.tight_layout()
plt.show()
```

### Categorical Variables

#### Frequency Analysis
```python
# Value counts
print(df['category'].value_counts())
print(df['category'].value_counts(normalize=True))  # Proportions

# For each categorical column
for col in df.select_dtypes(include=['object', 'category']).columns:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10))
    print(f"Unique values: {df[col].nunique()}")
```

#### Visualizations
```python
# Bar chart
df['category'].value_counts().plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Pie chart (for small number of categories)
df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Category Distribution')
plt.ylabel('')
plt.show()

# Count plot (seaborn)
sns.countplot(data=df, x='category')
plt.xticks(rotation=45)
plt.show()
```

## 4. Bivariate Analysis

### Numerical vs Numerical

#### Correlation
```python
# Correlation matrix
corr_matrix = df.select_dtypes(include=[np.number]).corr()
print(corr_matrix)

# Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1)
plt.title('Correlation Heatmap')
plt.show()

# Find highly correlated pairs
threshold = 0.8
high_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > threshold:
            high_corr.append((corr_matrix.columns[i], 
                            corr_matrix.columns[j], 
                            corr_matrix.iloc[i, j]))
print(high_corr)
```

#### Scatter Plots
```python
# Single scatter plot
plt.scatter(df['x'], df['y'], alpha=0.5)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('X vs Y')
plt.show()

# With regression line
sns.regplot(data=df, x='x', y='y')
plt.show()

# Pair plot (all combinations)
sns.pairplot(df.select_dtypes(include=[np.number]))
plt.show()

# Pair plot with hue
sns.pairplot(df, hue='category')
plt.show()
```

### Categorical vs Numerical

#### Group Statistics
```python
# Group by and aggregate
print(df.groupby('category')['value'].describe())

# Multiple aggregations
print(df.groupby('category').agg({
    'value1': ['mean', 'median', 'std'],
    'value2': ['sum', 'count']
}))
```

#### Visualizations
```python
# Box plot by category
sns.boxplot(data=df, x='category', y='value')
plt.xticks(rotation=45)
plt.show()

# Violin plot
sns.violinplot(data=df, x='category', y='value')
plt.xticks(rotation=45)
plt.show()

# Bar plot with error bars
sns.barplot(data=df, x='category', y='value', ci=95)
plt.xticks(rotation=45)
plt.show()

# Strip plot (show individual points)
sns.stripplot(data=df, x='category', y='value', alpha=0.5)
plt.xticks(rotation=45)
plt.show()

# Combination
fig, ax = plt.subplots()
sns.boxplot(data=df, x='category', y='value', ax=ax)
sns.swarmplot(data=df, x='category', y='value', color='black', alpha=0.3, ax=ax)
plt.xticks(rotation=45)
plt.show()
```

### Categorical vs Categorical

#### Contingency Tables
```python
# Cross-tabulation
ct = pd.crosstab(df['category1'], df['category2'])
print(ct)

# With percentages
ct_pct = pd.crosstab(df['category1'], df['category2'], normalize='all') * 100
print(ct_pct)

# Chi-square test
from scipy.stats import chi2_contingency
chi2, p_value, dof, expected = chi2_contingency(ct)
print(f"Chi-square: {chi2:.4f}, p-value: {p_value:.4f}")
```

#### Visualizations
```python
# Stacked bar chart
ct.plot(kind='bar', stacked=True)
plt.title('Category1 vs Category2')
plt.ylabel('Count')
plt.legend(title='Category2')
plt.show()

# Grouped bar chart
ct.plot(kind='bar', stacked=False)
plt.show()

# Heatmap
sns.heatmap(ct, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Category1 vs Category2')
plt.show()
```

## 5. Multivariate Analysis

### 3D Scatter Plot
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df['x'], df['y'], df['z'], c=df['color_var'], cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.colorbar(scatter)
plt.show()
```

### Parallel Coordinates
```python
from pandas.plotting import parallel_coordinates

parallel_coordinates(df, 'category', colormap='viridis')
plt.legend(loc='upper right')
plt.show()
```

### Facet Grid
```python
# Create grid of plots
g = sns.FacetGrid(df, col='category1', row='category2', height=4)
g.map(plt.scatter, 'x', 'y', alpha=0.5)
g.add_legend()
plt.show()
```

## 6. Outlier Detection

### Statistical Methods
```python
# Z-score method
from scipy import stats
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
outliers_z = (z_scores > 3).any(axis=1)
print(f"Outliers (Z-score): {outliers_z.sum()}")

# IQR method
Q1 = df.select_dtypes(include=[np.number]).quantile(0.25)
Q3 = df.select_dtypes(include=[np.number]).quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = ((df.select_dtypes(include=[np.number]) < (Q1 - 1.5 * IQR)) | 
                (df.select_dtypes(include=[np.number]) > (Q3 + 1.5 * IQR))).any(axis=1)
print(f"Outliers (IQR): {outliers_iqr.sum()}")
```

### Visual Detection
```python
# Box plots for all numerical columns
df.select_dtypes(include=[np.number]).boxplot(figsize=(15, 6))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot with potential outliers highlighted
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.1, random_state=42)
outliers = iso_forest.fit_predict(df[['x', 'y']])

plt.scatter(df['x'], df['y'], c=outliers, cmap='coolwarm')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Outlier Detection (Isolation Forest)')
plt.colorbar(label='Outlier (-1) / Normal (1)')
plt.show()
```

## 7. Time Series Analysis

### Temporal Patterns
```python
# Ensure datetime type
df['date'] = pd.to_datetime(df['date'])

# Set as index
df.set_index('date', inplace=True)

# Plot over time
df['value'].plot(figsize=(12, 6))
plt.title('Value Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Resampling
df_monthly = df.resample('M').mean()
df_monthly.plot(figsize=(12, 6))
plt.title('Monthly Average')
plt.show()

# Rolling statistics
df['rolling_mean'] = df['value'].rolling(window=7).mean()
df['rolling_std'] = df['value'].rolling(window=7).std()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value'], label='Original')
plt.plot(df.index, df['rolling_mean'], label='7-day Moving Average', linewidth=2)
plt.fill_between(df.index, 
                 df['rolling_mean'] - df['rolling_std'],
                 df['rolling_mean'] + df['rolling_std'],
                 alpha=0.2)
plt.legend()
plt.show()
```

### Seasonality and Trend
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose time series
decomposition = seasonal_decompose(df['value'], model='additive', period=12)

fig, axes = plt.subplots(4, 1, figsize=(12, 10))
decomposition.observed.plot(ax=axes[0], title='Original')
decomposition.trend.plot(ax=axes[1], title='Trend')
decomposition.seasonal.plot(ax=axes[2], title='Seasonal')
decomposition.resid.plot(ax=axes[3], title='Residual')
plt.tight_layout()
plt.show()
```

## 8. Feature Relationships

### Feature Importance (if target available)
```python
from sklearn.ensemble import RandomForestRegressor

X = df.drop('target', axis=1).select_dtypes(include=[np.number])
y = df['target']

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=importance_df.head(15), x='importance', y='feature')
plt.title('Top 15 Feature Importances')
plt.show()
```

## 9. Reporting Summary

### Create EDA Report
```python
def eda_summary(df):
    """Generate comprehensive EDA summary"""
    print("="*50)
    print("EXPLORATORY DATA ANALYSIS SUMMARY")
    print("="*50)
    
    print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    print(f"\n{'Missing Values':-^50}")
    missing = df.isna().sum()
    if missing.sum() == 0:
        print("No missing values found")
    else:
        print(missing[missing > 0].sort_values(ascending=False))
    
    print(f"\n{'Duplicates':-^50}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    
    print(f"\n{'Data Types':-^50}")
    print(df.dtypes.value_counts())
    
    print(f"\n{'Numerical Features Summary':-^50}")
    print(df.describe())
    
    print(f"\n{'Categorical Features':-^50}")
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        print(f"\n{col}:")
        print(df[col].value_counts().head())
    
    print("="*50)

eda_summary(df)
```

## Quick EDA Checklist

- [ ] Load and inspect data structure
- [ ] Check data types and memory usage
- [ ] Identify and handle missing values
- [ ] Detect and remove duplicates
- [ ] Analyze distribution of numerical variables
- [ ] Analyze frequency of categorical variables
- [ ] Explore correlations between numerical variables
- [ ] Investigate relationships between categorical and numerical variables
- [ ] Detect outliers
- [ ] Check for temporal patterns (if time series)
- [ ] Document findings and insights

---
[← Back to Main](../README.md)
