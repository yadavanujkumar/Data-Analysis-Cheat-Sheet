# NumPy Cheat Sheet 🔢

NumPy is the fundamental package for numerical computing in Python.

## Installation
```bash
pip install numpy
```

## Importing
```python
import numpy as np
```

## Creating Arrays

### From Lists
```python
np.array([1, 2, 3])              # 1D array
np.array([[1, 2], [3, 4]])       # 2D array
np.array([1, 2, 3], dtype=float) # Specify data type
```

### Special Arrays
```python
np.zeros((3, 4))                 # Array of zeros
np.ones((2, 3))                  # Array of ones
np.full((2, 3), 7)               # Array filled with 7
np.eye(3)                        # Identity matrix
np.empty((2, 3))                 # Uninitialized array
```

### Ranges
```python
np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)             # 5 evenly spaced values from 0 to 1
np.logspace(0, 2, 5)             # 5 log-spaced values from 10^0 to 10^2
```

### Random Arrays
```python
np.random.random((2, 3))         # Random floats [0, 1)
np.random.randint(0, 10, (2, 3)) # Random integers
np.random.randn(2, 3)            # Standard normal distribution
np.random.choice([1, 2, 3], 5)   # Random choice with replacement
np.random.seed(42)               # Set random seed
```

## Array Properties

```python
arr.shape                        # Dimensions
arr.size                         # Total number of elements
arr.ndim                         # Number of dimensions
arr.dtype                        # Data type
arr.itemsize                     # Size of each element in bytes
arr.nbytes                       # Total bytes consumed
```

## Array Operations

### Basic Math
```python
arr + 5                          # Add scalar
arr * 2                          # Multiply by scalar
arr ** 2                         # Power
arr1 + arr2                      # Element-wise addition
arr1 * arr2                      # Element-wise multiplication
arr1 / arr2                      # Element-wise division
```

### Mathematical Functions
```python
np.sqrt(arr)                     # Square root
np.exp(arr)                      # Exponential
np.log(arr)                      # Natural log
np.log10(arr)                    # Base 10 log
np.sin(arr)                      # Sine
np.cos(arr)                      # Cosine
np.abs(arr)                      # Absolute value
np.round(arr, 2)                 # Round to 2 decimals
```

### Aggregation Functions
```python
arr.sum()                        # Sum all elements
arr.mean()                       # Mean
arr.std()                        # Standard deviation
arr.var()                        # Variance
arr.min()                        # Minimum
arr.max()                        # Maximum
arr.argmin()                     # Index of minimum
arr.argmax()                     # Index of maximum
arr.cumsum()                     # Cumulative sum
arr.cumprod()                    # Cumulative product
```

### Statistics
```python
np.median(arr)                   # Median
np.percentile(arr, 25)           # 25th percentile
np.corrcoef(arr1, arr2)          # Correlation coefficient
np.cov(arr1, arr2)               # Covariance
```

## Indexing and Slicing

### Basic Indexing
```python
arr[0]                           # First element
arr[-1]                          # Last element
arr[1:4]                         # Elements 1 to 3
arr[::2]                         # Every other element
arr[::-1]                        # Reverse array
```

### 2D Array Indexing
```python
arr[0, 1]                        # Element at row 0, column 1
arr[0, :]                        # First row
arr[:, 1]                        # Second column
arr[0:2, 1:3]                    # Subarray
```

### Boolean Indexing
```python
arr[arr > 5]                     # Elements greater than 5
arr[arr % 2 == 0]                # Even elements
arr[(arr > 5) & (arr < 10)]      # Multiple conditions
```

### Fancy Indexing
```python
arr[[0, 2, 4]]                   # Select specific indices
arr[[0, 1], [1, 2]]              # Select specific elements
```

## Reshaping Arrays

```python
arr.reshape(3, 4)                # Reshape to 3x4
arr.reshape(-1, 1)               # Reshape to column vector
arr.ravel()                      # Flatten to 1D
arr.flatten()                    # Flatten to 1D (copy)
arr.T                            # Transpose
arr.transpose()                  # Transpose
arr.resize((2, 3))               # Resize in-place
```

## Stacking and Splitting

### Stacking
```python
np.vstack([arr1, arr2])          # Vertical stack
np.hstack([arr1, arr2])          # Horizontal stack
np.dstack([arr1, arr2])          # Depth stack
np.concatenate([arr1, arr2])     # Concatenate along axis
np.stack([arr1, arr2], axis=0)   # Stack along new axis
```

### Splitting
```python
np.split(arr, 3)                 # Split into 3 equal parts
np.vsplit(arr, 2)                # Vertical split
np.hsplit(arr, 2)                # Horizontal split
```

## Broadcasting

Broadcasting allows operations on arrays of different shapes:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + np.array([10, 20, 30])     # Adds [10, 20, 30] to each row
arr + np.array([[10], [20]])     # Adds column vector to array
```

## Linear Algebra

```python
# Matrix multiplication
np.dot(A, B)                     # Dot product
A @ B                            # Matrix multiplication (Python 3.5+)
np.matmul(A, B)                  # Matrix multiplication

# Matrix operations
np.linalg.inv(A)                 # Inverse
np.linalg.det(A)                 # Determinant
np.linalg.eig(A)                 # Eigenvalues and eigenvectors
np.linalg.svd(A)                 # Singular value decomposition
np.linalg.qr(A)                  # QR decomposition
np.trace(A)                      # Trace

# Solving systems
np.linalg.solve(A, b)            # Solve Ax = b
np.linalg.lstsq(A, b)            # Least squares solution
```

## Searching and Sorting

```python
np.sort(arr)                     # Sort array
np.argsort(arr)                  # Indices that would sort array
np.where(arr > 5)                # Indices where condition is true
np.where(arr > 5, 1, 0)          # Replace values based on condition
np.searchsorted(arr, 5)          # Find index to insert value
np.unique(arr)                   # Unique values
np.unique(arr, return_counts=True) # Unique values with counts
```

## Array Manipulation

```python
np.append(arr, [4, 5, 6])        # Append elements
np.insert(arr, 1, 5)             # Insert at position
np.delete(arr, 1)                # Delete at position
np.repeat(arr, 3)                # Repeat each element 3 times
np.tile(arr, 3)                  # Repeat entire array 3 times
np.flip(arr)                     # Reverse array
np.roll(arr, 2)                  # Shift elements
```

## Logical Operations

```python
np.logical_and(arr1, arr2)       # Element-wise AND
np.logical_or(arr1, arr2)        # Element-wise OR
np.logical_not(arr)              # Element-wise NOT
np.all(arr > 0)                  # Check if all elements > 0
np.any(arr > 0)                  # Check if any element > 0
np.isnan(arr)                    # Check for NaN
np.isinf(arr)                    # Check for infinity
```

## Set Operations

```python
np.union1d(arr1, arr2)           # Union
np.intersect1d(arr1, arr2)       # Intersection
np.setdiff1d(arr1, arr2)         # Difference
np.in1d(arr1, arr2)              # Test membership
```

## Advanced Operations

### Vectorize Functions
```python
def my_func(x):
    return x ** 2 + 2 * x + 1

vectorized = np.vectorize(my_func)
vectorized(arr)
```

### Apply Along Axis
```python
np.apply_along_axis(np.mean, 0, arr)  # Apply mean along columns
np.apply_along_axis(np.sum, 1, arr)   # Apply sum along rows
```

### Meshgrid (for plotting)
```python
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 5)
X, Y = np.meshgrid(x, y)
```

## Memory and Performance

### Views vs Copies
```python
arr_view = arr[:]                # View (shares memory)
arr_copy = arr.copy()            # Copy (separate memory)
arr_view.base is arr             # Check if view
```

### Memory Layout
```python
arr.flags                        # Memory layout info
arr.strides                      # Bytes to step in each dimension
```

## Data Types

```python
np.int8, np.int16, np.int32, np.int64
np.uint8, np.uint16, np.uint32, np.uint64
np.float16, np.float32, np.float64
np.complex64, np.complex128
np.bool_
```

### Type Conversion
```python
arr.astype(np.float32)           # Convert to float32
arr.astype(int)                  # Convert to int
```

## File I/O

```python
# Save/Load single array
np.save('array.npy', arr)
arr = np.load('array.npy')

# Save/Load multiple arrays
np.savez('arrays.npz', a=arr1, b=arr2)
data = np.load('arrays.npz')
arr1 = data['a']

# Text files
np.savetxt('array.txt', arr)
arr = np.loadtxt('array.txt')
np.genfromtxt('data.csv', delimiter=',')
```

## Performance Tips

1. **Use vectorized operations** instead of Python loops
2. **Preallocate arrays** when possible
3. **Use in-place operations** to save memory
4. **Choose appropriate data types** (smaller types use less memory)
5. **Use NumPy functions** instead of Python built-ins
6. **Avoid unnecessary copies** by using views

## Common Patterns

### Normalize Array
```python
normalized = (arr - arr.mean()) / arr.std()
```

### Min-Max Scaling
```python
scaled = (arr - arr.min()) / (arr.max() - arr.min())
```

### Moving Average
```python
window = 3
moving_avg = np.convolve(arr, np.ones(window)/window, mode='valid')
```

### Distance Matrix
```python
from scipy.spatial.distance import pdist, squareform
distances = squareform(pdist(arr, 'euclidean'))
```

## Quick Reference

| Operation | Code |
|-----------|------|
| Create array | `np.array([1, 2, 3])` |
| Zeros | `np.zeros((3, 4))` |
| Ones | `np.ones((3, 4))` |
| Range | `np.arange(0, 10, 2)` |
| Random | `np.random.random((2, 3))` |
| Shape | `arr.shape` |
| Sum | `arr.sum()` |
| Mean | `arr.mean()` |
| Reshape | `arr.reshape(3, 4)` |
| Transpose | `arr.T` |
| Matrix multiply | `A @ B` |
| Save | `np.save('file.npy', arr)` |

---
[← Back to Main](../README.md)
