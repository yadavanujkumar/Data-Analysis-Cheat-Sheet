"""
Quick Start Data Analysis Example
==================================

A simple introduction to data analysis with pandas, numpy, and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed
np.random.seed(42)

# Set style
sns.set_style('whitegrid')

print("=" * 50)
print("QUICK START DATA ANALYSIS")
print("=" * 50)

# ============================================================================
# 1. CREATE SAMPLE DATA
# ============================================================================
print("\n1. Creating sample dataset...")

# Generate sample sales data
dates = pd.date_range('2023-01-01', periods=365, freq='D')
data = {
    'date': dates,
    'sales': np.random.normal(1000, 200, 365) + np.sin(np.arange(365) * 2 * np.pi / 7) * 100,
    'customers': np.random.randint(50, 150, 365),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 365)
}

df = pd.DataFrame(data)
df['revenue'] = df['sales'] * np.random.uniform(10, 20, 365)

print("Dataset created!")
print(f"Shape: {df.shape}")

# ============================================================================
# 2. BASIC EXPLORATION
# ============================================================================
print("\n2. Basic Data Exploration")
print("-" * 50)

print("\nFirst few rows:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

# ============================================================================
# 3. SIMPLE ANALYSIS
# ============================================================================
print("\n3. Simple Analysis")
print("-" * 50)

# Calculate metrics
print(f"\nAverage daily sales: ${df['sales'].mean():.2f}")
print(f"Total revenue: ${df['revenue'].sum():,.2f}")
print(f"Average customers: {df['customers'].mean():.0f}")

# Group by region
print("\nSales by region:")
region_sales = df.groupby('region')['sales'].mean().sort_values(ascending=False)
print(region_sales)

# ============================================================================
# 4. VISUALIZATIONS
# ============================================================================
print("\n4. Creating visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Sales over time
axes[0, 0].plot(df['date'], df['sales'], alpha=0.7, linewidth=1)
axes[0, 0].set_title('Daily Sales Over Time', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Sales ($)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Sales distribution
axes[0, 1].hist(df['sales'], bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0, 1].set_title('Sales Distribution', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Sales ($)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(True, alpha=0.3)

# 3. Sales by region
region_sales.plot(kind='bar', ax=axes[1, 0], color='coral')
axes[1, 0].set_title('Average Sales by Region', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Region')
axes[1, 0].set_ylabel('Average Sales ($)')
axes[1, 0].tick_params(axis='x', rotation=0)
axes[1, 0].grid(True, alpha=0.3)

# 4. Sales vs Customers scatter
axes[1, 1].scatter(df['customers'], df['sales'], alpha=0.5, s=30)
axes[1, 1].set_title('Sales vs Customers', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Number of Customers')
axes[1, 1].set_ylabel('Sales ($)')
axes[1, 1].grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['customers'], df['sales'], 1)
p = np.poly1d(z)
axes[1, 1].plot(df['customers'].sort_values(), 
               p(df['customers'].sort_values()), 
               "r--", linewidth=2, alpha=0.8, label='Trend')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('quick_start_analysis.png', dpi=300, bbox_inches='tight')
print("Saved: quick_start_analysis.png")
plt.show()

# ============================================================================
# 5. CORRELATION ANALYSIS
# ============================================================================
print("\n5. Correlation Analysis")
print("-" * 50)

correlation = df[['sales', 'customers', 'revenue']].corr()
print("\nCorrelation Matrix:")
print(correlation)

# Visualize correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
           center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
print("\nSaved: correlation_matrix.png")

# ============================================================================
# 6. TIME SERIES INSIGHTS
# ============================================================================
print("\n6. Time Series Insights")
print("-" * 50)

# Resample to monthly
df.set_index('date', inplace=True)
monthly = df.resample('M').agg({
    'sales': 'sum',
    'customers': 'sum',
    'revenue': 'sum'
})

print("\nMonthly totals:")
print(monthly.head())

# Plot monthly trend
plt.figure(figsize=(12, 5))
monthly['sales'].plot(marker='o', linewidth=2, markersize=8)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('monthly_trend.png', dpi=300, bbox_inches='tight')
print("Saved: monthly_trend.png")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 50)
print("ANALYSIS COMPLETE")
print("=" * 50)

print("\nKey Insights:")
print(f"1. Analyzed {len(df)} days of sales data")
print(f"2. Total revenue: ${df['revenue'].sum():,.2f}")
print(f"3. Best performing region: {region_sales.index[0]} (${region_sales.iloc[0]:.2f})")
print(f"4. Sales-Customers correlation: {correlation.loc['sales', 'customers']:.2f}")

print("\nGenerated Files:")
print("- quick_start_analysis.png")
print("- correlation_matrix.png")
print("- monthly_trend.png")

print("\n" + "=" * 50)
print("Quick start example completed!")
print("=" * 50)
