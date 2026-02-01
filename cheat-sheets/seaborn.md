# Seaborn Cheat Sheet 🎨

Seaborn is a Python data visualization library based on Matplotlib, providing a high-level interface for statistical graphics.

## Installation
```bash
pip install seaborn
```

## Importing
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

## Setting Style

```python
# Set theme
sns.set_theme()

# Available styles
sns.set_style('darkgrid')   # darkgrid, whitegrid, dark, white, ticks
sns.set_context('notebook') # paper, notebook, talk, poster

# Set palette
sns.set_palette('husl')
sns.set_palette('Set2')
```

## Distribution Plots

### Histogram
```python
sns.histplot(data=df, x='column')
sns.histplot(data=df, x='column', bins=30, kde=True)
sns.histplot(data=df, x='column', hue='category')
```

### KDE Plot (Kernel Density Estimate)
```python
sns.kdeplot(data=df, x='column')
sns.kdeplot(data=df, x='column', hue='category')
sns.kdeplot(data=df, x='col1', y='col2')  # 2D KDE
```

### Distribution Plot (Combined)
```python
sns.displot(data=df, x='column', kind='hist')
sns.displot(data=df, x='column', kind='kde')
sns.displot(data=df, x='column', kind='ecdf')  # Empirical CDF
```

### Rug Plot
```python
sns.rugplot(data=df, x='column')
```

## Categorical Plots

### Bar Plot
```python
sns.barplot(data=df, x='category', y='value')
sns.barplot(data=df, x='category', y='value', hue='subcategory')
sns.barplot(data=df, x='category', y='value', estimator=sum)
```

### Count Plot
```python
sns.countplot(data=df, x='category')
sns.countplot(data=df, x='category', hue='subcategory')
```

### Box Plot
```python
sns.boxplot(data=df, x='category', y='value')
sns.boxplot(data=df, x='category', y='value', hue='subcategory')
```

### Violin Plot
```python
sns.violinplot(data=df, x='category', y='value')
sns.violinplot(data=df, x='category', y='value', split=True, hue='subcategory')
```

### Swarm Plot
```python
sns.swarmplot(data=df, x='category', y='value')
sns.swarmplot(data=df, x='category', y='value', hue='subcategory')
```

### Strip Plot
```python
sns.stripplot(data=df, x='category', y='value')
sns.stripplot(data=df, x='category', y='value', jitter=True)
```

### Point Plot
```python
sns.pointplot(data=df, x='category', y='value')
sns.pointplot(data=df, x='category', y='value', hue='subcategory')
```

## Relational Plots

### Scatter Plot
```python
sns.scatterplot(data=df, x='col1', y='col2')
sns.scatterplot(data=df, x='col1', y='col2', hue='category')
sns.scatterplot(data=df, x='col1', y='col2', size='value')
sns.scatterplot(data=df, x='col1', y='col2', style='category')
```

### Line Plot
```python
sns.lineplot(data=df, x='date', y='value')
sns.lineplot(data=df, x='date', y='value', hue='category')
sns.lineplot(data=df, x='date', y='value', style='category')
```

### Relational Plot (Figure-level)
```python
sns.relplot(data=df, x='col1', y='col2', kind='scatter')
sns.relplot(data=df, x='col1', y='col2', kind='line')
sns.relplot(data=df, x='col1', y='col2', col='category')  # Facet by column
sns.relplot(data=df, x='col1', y='col2', row='cat1', col='cat2')  # Grid
```

## Matrix Plots

### Heatmap
```python
# From DataFrame
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.heatmap(df.pivot_table(values='val', index='row', columns='col'))

# Customization
sns.heatmap(data, 
           annot=True,           # Show values
           fmt='.2f',            # Format
           cmap='viridis',       # Colormap
           linewidths=0.5,       # Grid lines
           cbar_kws={'label': 'Value'})
```

### Clustermap
```python
sns.clustermap(df, cmap='viridis', standard_scale=1)
sns.clustermap(df, method='average', metric='euclidean')
```

## Regression Plots

### Linear Regression Plot
```python
sns.regplot(data=df, x='col1', y='col2')
sns.regplot(data=df, x='col1', y='col2', order=2)  # Polynomial
```

### LM Plot (Figure-level)
```python
sns.lmplot(data=df, x='col1', y='col2')
sns.lmplot(data=df, x='col1', y='col2', hue='category')
sns.lmplot(data=df, x='col1', y='col2', col='category')
```

### Residual Plot
```python
sns.residplot(data=df, x='col1', y='col2')
```

## Multi-plot Grids

### PairPlot
```python
# Pairwise relationships
sns.pairplot(df)
sns.pairplot(df, hue='category')
sns.pairplot(df, diag_kind='kde')
sns.pairplot(df, vars=['col1', 'col2', 'col3'])
```

### FacetGrid
```python
# Custom grid
g = sns.FacetGrid(df, col='category', row='subcategory')
g.map(sns.scatterplot, 'x', 'y')

# With custom function
g = sns.FacetGrid(df, col='category', height=4)
g.map(plt.hist, 'value', bins=20)
```

### JointPlot
```python
# Bivariate with marginals
sns.jointplot(data=df, x='col1', y='col2')
sns.jointplot(data=df, x='col1', y='col2', kind='scatter')
sns.jointplot(data=df, x='col1', y='col2', kind='hex')
sns.jointplot(data=df, x='col1', y='col2', kind='kde')
sns.jointplot(data=df, x='col1', y='col2', kind='reg')
```

### PairGrid
```python
# More control than pairplot
g = sns.PairGrid(df)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
```

## Color Palettes

### Sequential
```python
sns.color_palette('Blues', n_colors=8)
sns.color_palette('viridis', n_colors=8)
```

### Diverging
```python
sns.color_palette('coolwarm', n_colors=8)
sns.color_palette('RdBu', n_colors=8)
```

### Qualitative
```python
sns.color_palette('Set2')
sns.color_palette('husl', n_colors=8)
```

### Custom
```python
colors = ['#FF5733', '#33FF57', '#3357FF']
sns.set_palette(colors)
```

### Show Palette
```python
sns.palplot(sns.color_palette())
```

## Customization

### Figure Size
```python
# For figure-level functions
sns.relplot(data=df, x='x', y='y', height=6, aspect=1.5)

# For axes-level functions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y')
```

### Titles and Labels
```python
# Figure-level
g = sns.relplot(data=df, x='x', y='y')
g.set_axis_labels('X Label', 'Y Label')
g.fig.suptitle('Main Title')

# Axes-level
ax = sns.scatterplot(data=df, x='x', y='y')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')
```

### Rotating Labels
```python
plt.xticks(rotation=45)
# Or
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
```

### Legend
```python
# Customize legend
ax = sns.scatterplot(data=df, x='x', y='y', hue='category')
plt.legend(title='Category', loc='upper right', frameon=False)

# For figure-level plots
g = sns.relplot(data=df, x='x', y='y', hue='category')
g._legend.set_title('New Title')
```

## Statistical Annotations

### Add Statistical Tests
```python
from scipy import stats

# Example with pointplot showing confidence intervals
sns.pointplot(data=df, x='category', y='value', capsize=0.1)
```

## Advanced Examples

### Combined Plot Types
```python
fig, ax = plt.subplots()
sns.boxplot(data=df, x='category', y='value', ax=ax)
sns.swarmplot(data=df, x='category', y='value', color='black', alpha=0.5, ax=ax)
plt.show()
```

### Annotated Heatmap
```python
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, square=True, linewidths=1)
```

### Time Series Plot
```python
df['date'] = pd.to_datetime(df['date'])
sns.lineplot(data=df, x='date', y='value', hue='category')
plt.xticks(rotation=45)
plt.tight_layout()
```

### Multiple Y-axes
```python
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

sns.lineplot(data=df, x='x', y='y1', ax=ax1, color='blue')
sns.lineplot(data=df, x='x', y='y2', ax=ax2, color='red')
ax1.set_ylabel('Y1', color='blue')
ax2.set_ylabel('Y2', color='red')
```

## Performance Tips

1. **Use categorical dtype** for categorical variables
2. **Sample large datasets** for exploration
3. **Use figure-level functions** for faceting
4. **Cache color palettes** for consistency

## Common Workflows

### Exploratory Data Analysis
```python
# Quick overview
sns.pairplot(df)

# Distribution of single variable
sns.histplot(data=df, x='value', kde=True)

# Relationship between variables
sns.scatterplot(data=df, x='x', y='y', hue='category')

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

### Publication-Ready Plot
```python
# Set style
sns.set_theme(style='white', context='paper', font_scale=1.2)

# Create plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df, x='x', y='y', hue='category', 
                style='category', s=100, alpha=0.7, ax=ax)

# Customize
ax.set_xlabel('X Variable', fontsize=14)
ax.set_ylabel('Y Variable', fontsize=14)
ax.set_title('Publication Title', fontsize=16, fontweight='bold')
ax.legend(title='Category', frameon=False)
sns.despine()

# Save
plt.savefig('figure.pdf', bbox_inches='tight', dpi=300)
```

## Quick Reference

| Plot Type | Code |
|-----------|------|
| Histogram | `sns.histplot(data=df, x='col')` |
| Scatter | `sns.scatterplot(data=df, x='x', y='y')` |
| Line | `sns.lineplot(data=df, x='x', y='y')` |
| Bar | `sns.barplot(data=df, x='cat', y='val')` |
| Box | `sns.boxplot(data=df, x='cat', y='val')` |
| Violin | `sns.violinplot(data=df, x='cat', y='val')` |
| Heatmap | `sns.heatmap(df.corr())` |
| Pairplot | `sns.pairplot(df)` |
| Regression | `sns.regplot(data=df, x='x', y='y')` |
| Count | `sns.countplot(data=df, x='cat')` |

---
[← Back to Main](../README.md)
