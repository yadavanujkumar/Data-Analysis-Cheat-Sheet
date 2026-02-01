# Matplotlib Cheat Sheet 📊

Matplotlib is the foundational plotting library for Python.

## Installation
```bash
pip install matplotlib
```

## Importing
```python
import matplotlib.pyplot as plt
import numpy as np
```

## Basic Plotting

### Line Plot
```python
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

# With labels
plt.plot(x, y, label='Line 1')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My Plot')
plt.legend()
plt.show()
```

### Multiple Lines
```python
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')
plt.legend()
plt.show()
```

### Scatter Plot
```python
plt.scatter(x, y)
plt.show()

# With customization
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.show()
```

### Bar Plot
```python
# Vertical bars
plt.bar(categories, values)
plt.show()

# Horizontal bars
plt.barh(categories, values)
plt.show()

# Grouped bars
width = 0.35
plt.bar(x - width/2, values1, width, label='Group 1')
plt.bar(x + width/2, values2, width, label='Group 2')
plt.legend()
plt.show()
```

### Histogram
```python
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.show()

# With customization
plt.hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Box Plot
```python
plt.boxplot([data1, data2, data3])
plt.show()

# Horizontal
plt.boxplot([data1, data2], vert=False)
plt.show()
```

### Pie Chart
```python
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()
```

## Figure and Axes

### Object-Oriented Interface
```python
# Recommended approach
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('My Plot')
plt.show()
```

### Multiple Subplots
```python
# 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data)
plt.tight_layout()
plt.show()
```

### Custom Layout
```python
fig = plt.figure(figsize=(12, 6))
ax1 = plt.subplot(2, 2, 1)  # 2 rows, 2 cols, position 1
ax2 = plt.subplot(2, 2, (2, 4))  # Span positions 2 and 4
plt.show()
```

## Customization

### Line Styles
```python
plt.plot(x, y, linestyle='-')   # solid
plt.plot(x, y, linestyle='--')  # dashed
plt.plot(x, y, linestyle='-.')  # dash-dot
plt.plot(x, y, linestyle=':')   # dotted
plt.plot(x, y, linewidth=2)     # Line width
```

### Colors
```python
# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='blue')

# Hex colors
plt.plot(x, y, color='#FF5733')

# RGB tuples
plt.plot(x, y, color=(0.1, 0.2, 0.5))

# Colormaps
scatter = plt.scatter(x, y, c=values, cmap='viridis')
plt.colorbar(scatter)
```

### Markers
```python
plt.plot(x, y, marker='o')      # Circle
plt.plot(x, y, marker='s')      # Square
plt.plot(x, y, marker='^')      # Triangle
plt.plot(x, y, marker='*')      # Star
plt.plot(x, y, marker='D')      # Diamond
plt.plot(x, y, markersize=10)   # Marker size
```

### Combined Style
```python
plt.plot(x, y, 'ro-', linewidth=2, markersize=8)  # Red circles with solid line
plt.plot(x, y, 'b--^', linewidth=1.5)             # Blue triangles with dashed line
```

### Axis Limits
```python
plt.xlim(0, 10)
plt.ylim(-5, 5)

# Or
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
```

### Axis Scale
```python
plt.xscale('log')
plt.yscale('log')

# Or
ax.set_xscale('log')
ax.set_yscale('log')
```

### Grid
```python
plt.grid(True)
plt.grid(True, linestyle='--', alpha=0.5)

# Or
ax.grid(True, which='both', linestyle='--', alpha=0.7)
```

### Ticks
```python
# Set specific tick locations
plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks(np.arange(-5, 6, 1))

# Set tick labels
plt.xticks([0, 1, 2], ['Low', 'Medium', 'High'])

# Rotate labels
plt.xticks(rotation=45)
```

## Advanced Plotting

### Error Bars
```python
plt.errorbar(x, y, yerr=errors, fmt='o-', capsize=5)
plt.show()
```

### Fill Between
```python
plt.plot(x, y)
plt.fill_between(x, y, alpha=0.3)
plt.show()

# Fill between two lines
plt.fill_between(x, y1, y2, alpha=0.3)
plt.show()
```

### Heatmap
```python
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
```

### Contour Plot
```python
plt.contour(X, Y, Z)
plt.colorbar()
plt.show()

# Filled contours
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.show()
```

### 3D Plotting
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

### Violin Plot
```python
parts = plt.violinplot([data1, data2, data3])
plt.show()
```

### Step Plot
```python
plt.step(x, y, where='mid')
plt.show()
```

### Stem Plot
```python
plt.stem(x, y)
plt.show()
```

## Annotations and Text

### Add Text
```python
plt.text(x, y, 'Text here', fontsize=12, color='red')
plt.show()
```

### Annotate
```python
plt.plot(x, y)
plt.annotate('Peak', xy=(peak_x, peak_y), 
             xytext=(peak_x+1, peak_y+1),
             arrowprops=dict(arrowstyle='->', color='red'))
plt.show()
```

### Axis Labels with LaTeX
```python
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta^2$')
plt.title(r'$\frac{1}{x}$')
plt.show()
```

## Styling

### Style Sheets
```python
# Available styles
print(plt.style.available)

# Use a style
plt.style.use('seaborn-v0_8')
plt.style.use('ggplot')
plt.style.use('dark_background')
```

### Figure Size and DPI
```python
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(x, y)
plt.show()

# Or
fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
```

### Font Properties
```python
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
```

### Legend Customization
```python
plt.legend(loc='upper right')  # Location
plt.legend(loc='best')          # Auto-place
plt.legend(ncol=2)              # Multiple columns
plt.legend(frameon=False)       # No frame
plt.legend(fontsize=10)         # Font size
```

## Saving Figures

```python
# Save as PNG
plt.savefig('figure.png', dpi=300, bbox_inches='tight')

# Save as PDF (vector)
plt.savefig('figure.pdf', bbox_inches='tight')

# Save as SVG
plt.savefig('figure.svg', bbox_inches='tight')

# Multiple formats
for fmt in ['png', 'pdf', 'svg']:
    plt.savefig(f'figure.{fmt}', bbox_inches='tight')
```

## Interactive Features

```python
# Interactive mode
plt.ion()   # Turn on
plt.ioff()  # Turn off

# Show plot without blocking
plt.show(block=False)

# Pause execution
plt.pause(2)  # Pause for 2 seconds

# Clear figure
plt.clf()

# Clear axes
plt.cla()

# Close figure
plt.close()

# Close all figures
plt.close('all')
```

## Common Patterns

### Side-by-Side Comparison
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1)
ax1.set_title('Plot 1')
ax2.plot(x, y2)
ax2.set_title('Plot 2')
plt.tight_layout()
plt.show()
```

### Shared Axes
```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(x, y1)
ax2.plot(x, y2)
plt.show()
```

### Inset Plot
```python
fig, ax = plt.subplots()
ax.plot(x, y)

# Create inset
axins = ax.inset_axes([0.6, 0.6, 0.35, 0.35])
axins.plot(x, y)
axins.set_xlim(5, 7)
axins.set_ylim(2, 4)
plt.show()
```

### Twin Axes
```python
fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'b-')
ax1.set_ylabel('Y1', color='b')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Y2', color='r')

plt.show()
```

## Performance Tips

1. **Use object-oriented interface** for complex plots
2. **Avoid plt.show() in loops** - create all plots then show
3. **Use blitting** for animations
4. **Close figures** when done to free memory
5. **Use appropriate backends** for non-interactive environments

## Quick Reference

| Plot Type | Code |
|-----------|------|
| Line | `plt.plot(x, y)` |
| Scatter | `plt.scatter(x, y)` |
| Bar | `plt.bar(x, y)` |
| Histogram | `plt.hist(data)` |
| Box | `plt.boxplot(data)` |
| Pie | `plt.pie(sizes)` |
| Subplots | `fig, ax = plt.subplots(2, 2)` |
| Grid | `plt.grid(True)` |
| Legend | `plt.legend()` |
| Save | `plt.savefig('file.png')` |

## Common Colormaps

- **Sequential**: `viridis`, `plasma`, `inferno`, `magma`, `cividis`
- **Diverging**: `RdBu`, `RdYlBu`, `coolwarm`, `seismic`
- **Qualitative**: `tab10`, `tab20`, `Set1`, `Set2`, `Pastel1`
- **Other**: `jet`, `rainbow`, `hot`, `cool`, `gray`

---
[← Back to Main](../README.md)
