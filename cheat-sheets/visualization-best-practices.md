# Data Visualization Best Practices 🎨

Guidelines for creating effective, clear, and impactful data visualizations.

## General Principles

### 1. Know Your Audience
- **Technical audience**: Can handle complex visualizations, technical terms
- **Non-technical audience**: Need simpler charts, clear labels, minimal jargon
- **Executive audience**: Focus on key insights, high-level trends

### 2. Choose the Right Chart Type

| Data Type | Purpose | Best Chart |
|-----------|---------|------------|
| Compare categories | Show differences | Bar chart, Column chart |
| Show trend over time | Temporal patterns | Line chart, Area chart |
| Show distribution | Data spread | Histogram, Box plot, Violin plot |
| Show relationship | Correlation | Scatter plot, Bubble chart |
| Show composition | Parts of whole | Pie chart, Stacked bar, Treemap |
| Show geographic data | Location patterns | Map, Choropleth |

### 3. Data-Ink Ratio
Maximize the data-to-ink ratio by removing non-essential elements:
- Eliminate chartjunk (unnecessary decorations)
- Remove or lighten gridlines
- Minimize borders and backgrounds
- Use direct labeling instead of legends when possible

## Color Guidelines

### Color Selection
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Use colorblind-friendly palettes
sns.set_palette("colorblind")

# Sequential (for continuous data)
# Good: Blues, Greens, viridis, plasma
colors = sns.color_palette("Blues", n_colors=8)

# Diverging (for data with meaningful center)
# Good: RdBu, coolwarm, seismic
colors = sns.color_palette("RdBu", n_colors=8)

# Qualitative (for categories)
# Good: Set2, tab10, husl
colors = sns.color_palette("Set2")
```

### Color Best Practices
1. **Limit colors**: Use 5-7 colors maximum
2. **Be consistent**: Same colors for same categories across charts
3. **Consider colorblindness**: Avoid red-green combinations
4. **Use color purposefully**: Don't use color just because you can
5. **High contrast**: Ensure text is readable on backgrounds

### Effective Color Usage
```python
# Good: Highlight one category
colors = ['#808080'] * 5
colors[2] = '#FF5733'  # Highlight third bar
plt.bar(categories, values, color=colors)

# Good: Use colormap for continuous values
scatter = plt.scatter(x, y, c=values, cmap='viridis')
plt.colorbar(scatter, label='Value')

# Bad: Random colors for unrelated categories
# Avoid rainbow colors unless showing continuous gradient
```

## Chart-Specific Guidelines

### Line Charts

#### Good Practices
```python
# Clear, simple line chart
plt.figure(figsize=(10, 6))
plt.plot(dates, values, linewidth=2, color='#2E86AB')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()

# Multiple lines with clear differentiation
plt.plot(dates, series1, label='Product A', linewidth=2)
plt.plot(dates, series2, label='Product B', linewidth=2, linestyle='--')
plt.legend(frameon=False)
```

#### Avoid
- Too many lines (max 5-7)
- 3D line charts
- Unnecessary decorations
- Poor color contrast

### Bar Charts

#### Good Practices
```python
# Horizontal bars for long category names
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color='#2E86AB')
plt.xlabel('Value')
plt.ylabel('Category')
plt.title('Category Comparison')
# Remove top and right spines
sns.despine()
plt.show()

# Sort bars by value for easier comparison
df_sorted = df.sort_values('value', ascending=True)
plt.barh(df_sorted['category'], df_sorted['value'])
```

#### Avoid
- Starting y-axis at non-zero (misleading)
- 3D bars (distort perception)
- Too many bars (consider grouping)
- Unnecessary gradients or patterns

### Scatter Plots

#### Good Practices
```python
# Clear scatter with trend line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=50, color='#2E86AB')

# Add trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2, label='Trend')

plt.xlabel('X Variable', fontsize=12)
plt.ylabel('Y Variable', fontsize=12)
plt.title('X vs Y Relationship', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Use size or color to show 3rd dimension
plt.scatter(x, y, s=sizes*10, c=categories, cmap='Set2', alpha=0.6)
plt.colorbar(label='Category')
```

#### Avoid
- Overplotting (use alpha or sample data)
- Too small or too large points
- No clear pattern or message

### Heatmaps

#### Good Practices
```python
# Clear correlation heatmap
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))  # Show only lower triangle
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', 
           cmap='coolwarm', center=0, square=True, 
           linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### Avoid
- Wrong color scheme (use diverging for correlations)
- Too many decimal places in annotations
- Missing color bar
- Not centering diverging colors at meaningful point

## Typography

### Font Guidelines
```python
# Set readable fonts
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

# Hierarchy: Title > Axis labels > Tick labels
plt.title('Main Title', fontsize=16, fontweight='bold')
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
```

### Text Best Practices
1. **Use hierarchy**: Larger, bolder for important text
2. **Be concise**: Clear, short labels
3. **Avoid vertical text**: Rotate 45° if needed
4. **Consistent fonts**: Use same font family throughout
5. **Sufficient contrast**: Ensure readability

## Axes and Scales

### Axis Best Practices
```python
# Start at zero for bar charts (show true magnitude)
plt.ylim(0, max_value * 1.1)

# Include zero only when meaningful
# For trends, focus on the data range
plt.ylim(data.min() * 0.95, data.max() * 1.05)

# Use appropriate scale
plt.yscale('log')  # For exponential data

# Clear axis labels with units
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')

# Format tick labels
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
```

### Avoid
- Misleading scales (truncated y-axis for bar charts)
- Dual y-axes (confusing, consider separate charts)
- Too many tick marks
- Unlabeled axes

## Annotations and Labels

### Direct Labeling
```python
# Label data points directly
for i, (x, y) in enumerate(zip(x_values, y_values)):
    plt.text(x, y + 0.5, f'{y:.1f}', ha='center', fontsize=10)

# Label line ends instead of using legend
plt.text(x_values[-1], y1_values[-1], 'Series 1', 
        va='center', fontsize=11, fontweight='bold')
plt.text(x_values[-1], y2_values[-1], 'Series 2', 
        va='center', fontsize=11, fontweight='bold')
```

### Effective Annotations
```python
# Highlight important points
plt.annotate('Peak Sales', 
            xy=(peak_date, peak_value),
            xytext=(peak_date, peak_value + 1000),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, fontweight='bold', color='red')

# Add reference lines
plt.axhline(y=target, color='gray', linestyle='--', 
           linewidth=2, alpha=0.7, label='Target')
```

## Layout and Composition

### Figure Size and Resolution
```python
# Appropriate size for medium
plt.figure(figsize=(10, 6), dpi=100)  # Screen
plt.savefig('chart.png', dpi=300, bbox_inches='tight')  # Print

# Maintain aspect ratio
fig, ax = plt.subplots(figsize=(8, 8))  # Square
```

### Whitespace
```python
# Use tight_layout to prevent overlap
plt.tight_layout()

# Or manually adjust
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Add padding
plt.margins(0.1)
```

### Multiple Charts
```python
# Clear grid layout
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Dashboard Title', fontsize=16, fontweight='bold')

# Consistent styling across subplots
for ax in axes.flat:
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
```

## Interactivity (for dashboards)

### Plotly Example
```python
import plotly.express as px

# Interactive scatter
fig = px.scatter(df, x='x', y='y', color='category',
                hover_data=['name', 'value'],
                title='Interactive Scatter Plot')
fig.show()

# Interactive time series
fig = px.line(df, x='date', y='value', 
             title='Interactive Time Series')
fig.update_xaxes(rangeslider_visible=True)
fig.show()
```

## Accessibility

### Make Charts Accessible
1. **Alt text**: Provide text description of chart
2. **Color**: Don't rely solely on color
3. **Patterns**: Use patterns in addition to colors
4. **Text size**: Minimum 11-12pt for body text
5. **Contrast**: WCAG AA standard (4.5:1 minimum)

```python
# Add patterns to bars
bars = plt.bar(categories, values, color=['red', 'blue', 'green'])
bars[0].set_hatch('//')
bars[1].set_hatch('\\\\')
bars[2].set_hatch('xx')
```

## Common Mistakes to Avoid

### ❌ DON'T
1. Use 3D charts (distort perception)
2. Use dual y-axes (confusing)
3. Start bar charts at non-zero
4. Use too many colors
5. Create chartjunk
6. Use pie charts for more than 5 categories
7. Make text too small
8. Use rainbow color schemes for categories
9. Overload with data
10. Forget to label axes

### ✅ DO
1. Keep it simple
2. Use consistent colors
3. Label clearly
4. Show data clearly
5. Remove clutter
6. Use appropriate chart types
7. Consider your audience
8. Tell a story
9. Test readability
10. Provide context

## Publication-Ready Template

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication style
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.2)

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot data
ax.plot(x, y, linewidth=2, color='#2E86AB', label='Data')

# Customize
ax.set_xlabel('X Axis Label', fontsize=14)
ax.set_ylabel('Y Axis Label', fontsize=14)
ax.set_title('Publication-Ready Chart', fontsize=16, fontweight='bold', pad=20)
ax.legend(frameon=False, fontsize=12)
ax.grid(True, alpha=0.3, linestyle='--')

# Remove top and right spines
sns.despine()

# Save high quality
plt.tight_layout()
plt.savefig('figure.pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Storytelling with Data

### Structure Your Visualization
1. **Context**: What is being shown?
2. **Insight**: What's the key finding?
3. **Action**: What should viewer do?

### Effective Titles
```python
# ❌ Weak: "Sales Data"
# ✅ Strong: "Sales Increased 45% in Q4 2023"

# ❌ Weak: "Temperature Graph"
# ✅ Strong: "Global Temperatures Rising Fastest in 1,000 Years"
```

### Guide the Viewer
```python
# Use visual hierarchy
plt.title('Main Finding: Sales Up 45%', fontsize=16, fontweight='bold')
plt.annotate('Record high', xy=(peak_x, peak_y), 
            xytext=(peak_x-1, peak_y+5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, color='red', fontweight='bold')
```

## Checklist for Every Visualization

- [ ] Chart type appropriate for data and message
- [ ] All axes labeled with units
- [ ] Title clearly states the insight
- [ ] Legend present (if needed) and clear
- [ ] Colors are meaningful and accessible
- [ ] Text is readable (size, contrast)
- [ ] No chartjunk or unnecessary elements
- [ ] Data source noted (if applicable)
- [ ] Scale is appropriate and not misleading
- [ ] Tested with audience or colleagues

---
[← Back to Main](../README.md)
