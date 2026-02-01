# Pandas Cheat Sheet 🐼

Pandas is the essential library for data manipulation and analysis in Python.

## Installation
```bash
pip install pandas
```

## Importing
```python
import pandas as pd
import numpy as np
```

## Creating DataFrames

### From Dictionary
```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.5, 2.5, 3.5]
})
```

### From CSV
```python
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', sep=';', encoding='utf-8', index_col=0)
```

### From Excel
```python
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
```

### From SQL
```python
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///database.db')
df = pd.read_sql('SELECT * FROM table', engine)
```

## Viewing Data

```python
df.head()              # First 5 rows
df.tail(10)            # Last 10 rows
df.shape               # Dimensions (rows, columns)
df.info()              # Data types and memory usage
df.describe()          # Statistical summary
df.columns             # Column names
df.dtypes              # Data types of columns
df.index               # Index information
```

## Selecting Data

### By Column
```python
df['A']                # Single column (Series)
df[['A', 'B']]        # Multiple columns (DataFrame)
```

### By Row (Position)
```python
df.iloc[0]             # First row
df.iloc[0:5]           # First 5 rows
df.iloc[:, 0]          # First column
df.iloc[0:5, 0:3]     # Rows 0-4, columns 0-2
```

### By Label
```python
df.loc[0]              # Row with index 0
df.loc[:, 'A']         # Column 'A'
df.loc[0:5, ['A', 'B']] # Rows 0-5, columns A and B
```

### Boolean Indexing
```python
df[df['A'] > 5]        # Rows where A > 5
df[df['B'].isin(['a', 'b'])]  # Rows where B is 'a' or 'b'
df[(df['A'] > 5) & (df['B'] < 10)]  # Multiple conditions
```

## Data Manipulation

### Adding/Modifying Columns
```python
df['D'] = df['A'] + df['C']     # New column
df['E'] = df['A'].apply(lambda x: x * 2)  # Apply function
df.assign(F=df['A'] * 3)        # Chain-friendly assignment
```

### Dropping Columns/Rows
```python
df.drop('A', axis=1)            # Drop column
df.drop([0, 1], axis=0)         # Drop rows
df.drop_duplicates()            # Remove duplicates
```

### Renaming
```python
df.rename(columns={'A': 'Alpha', 'B': 'Beta'})
df.columns = ['col1', 'col2', 'col3']  # Rename all columns
```

### Sorting
```python
df.sort_values('A')                    # Sort by column A
df.sort_values(['A', 'B'], ascending=[True, False])
df.sort_index()                        # Sort by index
```

## Handling Missing Data

```python
df.isna()                    # Check for missing values
df.isna().sum()              # Count missing per column
df.dropna()                  # Drop rows with any NaN
df.dropna(axis=1)            # Drop columns with any NaN
df.fillna(0)                 # Fill NaN with 0
df.fillna(df.mean())         # Fill with column mean
df.fillna(method='ffill')    # Forward fill
df.fillna(method='bfill')    # Backward fill
df.interpolate()             # Interpolate missing values
```

## Grouping and Aggregation

```python
# Basic groupby
df.groupby('A').mean()
df.groupby('A').sum()
df.groupby('A').count()

# Multiple aggregations
df.groupby('A').agg(['mean', 'sum', 'count'])

# Different aggregations per column
df.groupby('A').agg({'B': 'mean', 'C': 'sum'})

# Multiple groupby columns
df.groupby(['A', 'B']).mean()

# Custom aggregation
df.groupby('A').agg(lambda x: x.max() - x.min())
```

## Merging and Joining

```python
# Merge (SQL-style joins)
pd.merge(df1, df2, on='key')
pd.merge(df1, df2, left_on='key1', right_on='key2')
pd.merge(df1, df2, how='left')   # left, right, inner, outer

# Concatenate
pd.concat([df1, df2])            # Vertical stack
pd.concat([df1, df2], axis=1)    # Horizontal stack

# Join (by index)
df1.join(df2, how='inner')
```

## Reshaping Data

```python
# Pivot
df.pivot(index='A', columns='B', values='C')

# Pivot table with aggregation
df.pivot_table(values='C', index='A', columns='B', aggfunc='mean')

# Melt (unpivot)
pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])

# Stack/Unstack
df.stack()
df.unstack()
```

## String Operations

```python
df['B'].str.lower()              # Lowercase
df['B'].str.upper()              # Uppercase
df['B'].str.strip()              # Remove whitespace
df['B'].str.replace('a', 'A')    # Replace substring
df['B'].str.contains('pattern')  # Check if contains
df['B'].str.split(',')           # Split string
df['B'].str.len()                # String length
df['B'].str.extract(r'(\d+)')    # Extract with regex
```

## DateTime Operations

```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek

# Date arithmetic
df['date'] + pd.Timedelta(days=7)
df['date'].diff()                # Difference between consecutive dates

# Filtering by date
df[df['date'] > '2023-01-01']
df[df['date'].between('2023-01-01', '2023-12-31')]
```

## Statistical Operations

```python
df.mean()                  # Mean of each column
df.median()                # Median
df.std()                   # Standard deviation
df.var()                   # Variance
df.min() / df.max()        # Min/Max
df.quantile(0.25)          # Quantiles
df.corr()                  # Correlation matrix
df.cov()                   # Covariance matrix
df['A'].value_counts()     # Count unique values
```

## Window Functions

```python
# Rolling window
df['A'].rolling(window=3).mean()
df['A'].rolling(window=3).sum()

# Expanding window
df['A'].expanding().mean()

# Exponentially weighted
df['A'].ewm(span=3).mean()
```

## Exporting Data

```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
df.to_json('output.json')
df.to_sql('table_name', engine, if_exists='replace')
df.to_dict()
```

## Performance Tips

1. **Use vectorized operations** instead of loops
2. **Use categorical data type** for strings with few unique values
3. **Read only needed columns**: `pd.read_csv('file.csv', usecols=['A', 'B'])`
4. **Use chunks for large files**: `pd.read_csv('file.csv', chunksize=10000)`
5. **Set appropriate dtypes** when reading data
6. **Use `inplace=True`** carefully (not always faster)

## Common Patterns

### Filter and Select
```python
df[df['A'] > 5][['B', 'C']]
```

### Chain Operations
```python
(df
 .query('A > 5')
 .groupby('B')
 .agg({'C': 'mean'})
 .sort_values('C', ascending=False)
 .head(10))
```

### Apply Functions by Group
```python
df.groupby('A')['B'].transform(lambda x: (x - x.mean()) / x.std())
```

### Create Binary Columns
```python
df['is_high'] = (df['A'] > df['A'].median()).astype(int)
```

## Quick Reference

| Operation | Code |
|-----------|------|
| Read CSV | `pd.read_csv('file.csv')` |
| First rows | `df.head()` |
| Info | `df.info()` |
| Select column | `df['col']` |
| Filter rows | `df[df['col'] > 5]` |
| Group by | `df.groupby('col').mean()` |
| Sort | `df.sort_values('col')` |
| Missing values | `df.isna().sum()` |
| Unique values | `df['col'].unique()` |
| Save CSV | `df.to_csv('file.csv')` |

---
[← Back to Main](../README.md)
