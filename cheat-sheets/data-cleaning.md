# Data Cleaning Cheat Sheet 🧹

Essential techniques for cleaning and preprocessing data.

## Import Libraries
```python
import pandas as pd
import numpy as np
```

## Inspecting Data

### Initial Overview
```python
df.head()                    # First 5 rows
df.tail()                    # Last 5 rows
df.info()                    # Column types and non-null counts
df.describe()                # Statistical summary
df.shape                     # (rows, columns)
df.columns                   # Column names
df.dtypes                    # Data types
df.memory_usage()            # Memory usage per column
```

### Data Quality Checks
```python
# Missing values
df.isna().sum()              # Count missing per column
df.isna().sum() / len(df)    # Percentage missing

# Duplicates
df.duplicated().sum()        # Count duplicates
df[df.duplicated()]          # Show duplicate rows

# Unique values
df.nunique()                 # Count unique per column
df['column'].unique()        # Show unique values
df['column'].value_counts()  # Frequency of values
```

## Handling Missing Data

### Detection
```python
# Check for missing values
df.isna()
df.isnull()                  # Same as isna()

# Count missing per column
missing = df.isna().sum()

# Percentage missing
missing_pct = (df.isna().sum() / len(df)) * 100

# Visualize missing data
import missingno as msno
msno.matrix(df)
msno.heatmap(df)
```

### Removal
```python
# Drop rows with any missing values
df.dropna()

# Drop rows where all values are missing
df.dropna(how='all')

# Drop rows with missing values in specific columns
df.dropna(subset=['col1', 'col2'])

# Drop columns with any missing values
df.dropna(axis=1)

# Drop columns with more than 50% missing
threshold = len(df) * 0.5
df.dropna(axis=1, thresh=threshold)
```

### Imputation
```python
# Fill with a constant
df.fillna(0)
df.fillna('Unknown')

# Fill with column statistics
df.fillna(df.mean())         # Mean
df.fillna(df.median())       # Median
df.fillna(df.mode().iloc[0]) # Mode

# Fill per column
df['numeric_col'].fillna(df['numeric_col'].mean(), inplace=True)
df['categorical_col'].fillna('Unknown', inplace=True)

# Forward fill (use previous value)
df.fillna(method='ffill')

# Backward fill (use next value)
df.fillna(method='bfill')

# Interpolate
df.interpolate()             # Linear interpolation
df.interpolate(method='polynomial', order=2)
```

### Advanced Imputation
```python
from sklearn.impute import SimpleImputer, KNNImputer

# Simple imputation
imputer = SimpleImputer(strategy='mean')  # mean, median, most_frequent, constant
df_imputed = imputer.fit_transform(df)

# KNN imputation
imputer = KNNImputer(n_neighbors=5)
df_imputed = imputer.fit_transform(df)
```

## Handling Duplicates

### Detection
```python
# Check for duplicates
df.duplicated()

# Check duplicates based on specific columns
df.duplicated(subset=['col1', 'col2'])

# Show duplicate rows
df[df.duplicated()]
df[df.duplicated(keep=False)]  # Show all occurrences
```

### Removal
```python
# Remove duplicates
df.drop_duplicates()

# Keep first occurrence
df.drop_duplicates(keep='first')

# Keep last occurrence
df.drop_duplicates(keep='last')

# Based on specific columns
df.drop_duplicates(subset=['col1', 'col2'])
```

## Data Type Conversion

### Convert Types
```python
# To numeric
df['col'] = pd.to_numeric(df['col'], errors='coerce')

# To string
df['col'] = df['col'].astype(str)

# To integer
df['col'] = df['col'].astype(int)

# To float
df['col'] = df['col'].astype(float)

# To datetime
df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# To categorical
df['category'] = df['category'].astype('category')

# To boolean
df['bool_col'] = df['bool_col'].astype(bool)
```

### Handle Conversion Errors
```python
# Coerce errors to NaN
df['col'] = pd.to_numeric(df['col'], errors='coerce')

# Ignore errors (keep original)
df['col'] = pd.to_numeric(df['col'], errors='ignore')
```

## String Cleaning

### Case Conversion
```python
df['col'] = df['col'].str.lower()
df['col'] = df['col'].str.upper()
df['col'] = df['col'].str.title()
df['col'] = df['col'].str.capitalize()
```

### Whitespace Removal
```python
df['col'] = df['col'].str.strip()       # Both sides
df['col'] = df['col'].str.lstrip()      # Left side
df['col'] = df['col'].str.rstrip()      # Right side
df['col'] = df['col'].str.replace(r'\s+', ' ', regex=True)  # Multiple spaces
```

### String Replacement
```python
# Replace specific string
df['col'] = df['col'].str.replace('old', 'new')

# Replace with regex
df['col'] = df['col'].str.replace(r'\d+', '', regex=True)  # Remove digits

# Remove special characters
df['col'] = df['col'].str.replace(r'[^\w\s]', '', regex=True)
```

### String Extraction
```python
# Extract pattern
df['extracted'] = df['col'].str.extract(r'(\d+)')

# Extract all occurrences
df['extracted'] = df['col'].str.findall(r'\d+')

# Check if contains pattern
df['has_pattern'] = df['col'].str.contains(r'\d+')
```

### String Splitting
```python
# Split into multiple columns
df[['first', 'last']] = df['name'].str.split(' ', expand=True)

# Split into list
df['parts'] = df['col'].str.split(',')
```

## Outlier Detection and Handling

### Z-Score Method
```python
from scipy import stats

# Calculate z-scores
z_scores = np.abs(stats.zscore(df['col']))

# Remove outliers (|z| > 3)
df = df[z_scores < 3]

# Cap outliers
df.loc[z_scores > 3, 'col'] = df['col'].quantile(0.99)
```

### IQR Method
```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df['col'] >= lower_bound) & (df['col'] <= upper_bound)]

# Cap outliers
df['col'] = df['col'].clip(lower=lower_bound, upper=upper_bound)
```

### Winsorization
```python
from scipy.stats.mstats import winsorize

# Cap at 5th and 95th percentiles
df['col'] = winsorize(df['col'], limits=[0.05, 0.05])
```

## Standardization and Normalization

### Standardization (Z-score)
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['col_scaled'] = scaler.fit_transform(df[['col']])

# Manual
df['col_scaled'] = (df['col'] - df['col'].mean()) / df['col'].std()
```

### Min-Max Normalization
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['col_normalized'] = scaler.fit_transform(df[['col']])

# Manual
df['col_normalized'] = (df['col'] - df['col'].min()) / (df['col'].max() - df['col'].min())
```

### Robust Scaling
```python
from sklearn.preprocessing import RobustScaler

# Uses median and IQR (robust to outliers)
scaler = RobustScaler()
df['col_scaled'] = scaler.fit_transform(df[['col']])
```

## Encoding Categorical Variables

### Label Encoding
```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Manual with mapping
mapping = {'low': 0, 'medium': 1, 'high': 2}
df['category_encoded'] = df['category'].map(mapping)
```

### One-Hot Encoding
```python
# Pandas method
df_encoded = pd.get_dummies(df, columns=['category'])

# Sklearn method
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(df[['category']])
df_encoded = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
```

### Ordinal Encoding
```python
from sklearn.preprocessing import OrdinalEncoder

# With specific order
encoder = OrdinalEncoder(categories=[['low', 'medium', 'high']])
df['category_encoded'] = encoder.fit_transform(df[['category']])
```

### Target Encoding
```python
# Replace category with mean of target
category_means = df.groupby('category')['target'].mean()
df['category_encoded'] = df['category'].map(category_means)
```

## Feature Engineering

### Binning
```python
# Equal-width bins
df['age_bin'] = pd.cut(df['age'], bins=5)

# Custom bins
df['age_bin'] = pd.cut(df['age'], bins=[0, 18, 30, 50, 100], 
                       labels=['child', 'young', 'middle', 'senior'])

# Equal-frequency bins
df['age_bin'] = pd.qcut(df['age'], q=4)
```

### Creating Date Features
```python
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek
df['quarter'] = df['date'].dt.quarter
df['is_weekend'] = df['date'].dt.dayofweek.isin([5, 6]).astype(int)

# Time differences
df['days_since'] = (pd.Timestamp.now() - df['date']).dt.days
```

### Mathematical Transformations
```python
# Log transformation
df['log_col'] = np.log1p(df['col'])  # log(1 + x)

# Square root
df['sqrt_col'] = np.sqrt(df['col'])

# Power transformation
df['squared'] = df['col'] ** 2

# Box-Cox transformation
from scipy.stats import boxcox
df['boxcox_col'], _ = boxcox(df['col'] + 1)  # Add 1 if data contains 0
```

## Data Validation

### Value Range Checks
```python
# Check if values are within expected range
assert df['age'].between(0, 120).all(), "Invalid age values"
assert df['percentage'].between(0, 100).all(), "Invalid percentage"

# Filter invalid values
df = df[df['age'].between(0, 120)]
```

### Pattern Validation
```python
# Email validation
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
valid_emails = df['email'].str.match(email_pattern)
df = df[valid_emails]

# Phone number validation
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
valid_phones = df['phone'].str.match(phone_pattern)
```

### Consistency Checks
```python
# Date range consistency
assert (df['end_date'] >= df['start_date']).all(), "End date before start date"

# Cross-column validation
assert (df['total'] == df['subtotal'] + df['tax']).all(), "Total mismatch"
```

## Handling Inconsistent Data

### Standardize Categories
```python
# Fix inconsistent naming
df['category'] = df['category'].str.lower().str.strip()

# Replace variations
replacements = {
    'usa': 'United States',
    'u.s.a': 'United States',
    'us': 'United States'
}
df['country'] = df['country'].replace(replacements)
```

### Fix Data Entry Errors
```python
# Remove typos using fuzzy matching
from fuzzywuzzy import process

def standardize_name(name, choices):
    match = process.extractOne(name, choices)
    return match[0] if match[1] > 80 else name

standard_categories = ['Category A', 'Category B', 'Category C']
df['category'] = df['category'].apply(lambda x: standardize_name(x, standard_categories))
```

## Column Operations

### Renaming
```python
# Rename specific columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Rename all columns
df.columns = ['col1', 'col2', 'col3']

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
```

### Reordering
```python
# Specify new order
df = df[['col3', 'col1', 'col2']]

# Move column to front
cols = ['important_col'] + [col for col in df.columns if col != 'important_col']
df = df[cols]
```

### Dropping
```python
# Drop specific columns
df.drop(['col1', 'col2'], axis=1, inplace=True)

# Drop columns with all NaN
df.dropna(axis=1, how='all', inplace=True)

# Drop low-variance columns
low_var_cols = df.var()[df.var() < 0.01].index
df.drop(low_var_cols, axis=1, inplace=True)
```

## Best Practices

### 1. Always Keep Original Data
```python
df_clean = df.copy()  # Work on a copy
```

### 2. Document Cleaning Steps
```python
# Keep track of changes
cleaning_log = []
initial_rows = len(df)

df = df.dropna()
cleaning_log.append(f"Removed {initial_rows - len(df)} rows with missing values")
```

### 3. Validate After Each Step
```python
# Check data after transformations
assert df['col'].isna().sum() == 0, "Still has missing values"
assert df['col'].dtype == 'float64', "Wrong data type"
```

### 4. Create Cleaning Pipeline
```python
def clean_data(df):
    """Data cleaning pipeline"""
    df = df.copy()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df['numeric_col'].fillna(df['numeric_col'].median(), inplace=True)
    df['category_col'].fillna('Unknown', inplace=True)
    
    # Clean strings
    df['text_col'] = df['text_col'].str.strip().str.lower()
    
    # Remove outliers
    Q1 = df['numeric_col'].quantile(0.25)
    Q3 = df['numeric_col'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['numeric_col'] >= Q1 - 1.5*IQR) & 
            (df['numeric_col'] <= Q3 + 1.5*IQR)]
    
    return df

df_clean = clean_data(df)
```

## Quick Reference

| Task | Code |
|------|------|
| Check missing | `df.isna().sum()` |
| Drop missing | `df.dropna()` |
| Fill missing | `df.fillna(value)` |
| Remove duplicates | `df.drop_duplicates()` |
| Convert type | `df['col'].astype(type)` |
| Lowercase | `df['col'].str.lower()` |
| Strip whitespace | `df['col'].str.strip()` |
| Replace values | `df['col'].replace(old, new)` |
| Remove outliers | IQR or Z-score method |
| Standardize | `StandardScaler()` |
| Normalize | `MinMaxScaler()` |
| One-hot encode | `pd.get_dummies()` |

---
[← Back to Main](../README.md)
