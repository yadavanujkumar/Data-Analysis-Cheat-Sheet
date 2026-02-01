# Probability Cheat Sheet 🎲

Essential probability concepts for data analysis.

## Basic Concepts

### Probability Basics
```python
import numpy as np
from scipy import stats

# Probability of event A
P_A = favorable_outcomes / total_outcomes

# Complement: P(not A) = 1 - P(A)
P_not_A = 1 - P_A
```

### Rules of Probability

#### Addition Rule
```python
# For mutually exclusive events
P_A_or_B = P_A + P_B

# For non-mutually exclusive events
P_A_or_B = P_A + P_B - P_A_and_B
```

#### Multiplication Rule
```python
# For independent events
P_A_and_B = P_A * P_B

# For dependent events
P_A_and_B = P_A * P_B_given_A
```

#### Conditional Probability
```python
# P(A|B) = P(A and B) / P(B)
P_A_given_B = P_A_and_B / P_B
```

#### Bayes' Theorem
```python
# P(A|B) = P(B|A) * P(A) / P(B)
P_A_given_B = (P_B_given_A * P_A) / P_B

# Example: Medical test
sensitivity = 0.95      # P(positive|disease)
specificity = 0.90      # P(negative|no disease)
prevalence = 0.01       # P(disease)

# P(disease|positive)
P_disease_given_positive = (sensitivity * prevalence) / (
    sensitivity * prevalence + (1 - specificity) * (1 - prevalence)
)
```

## Discrete Probability Distributions

### Bernoulli Distribution
```python
from scipy.stats import bernoulli

p = 0.3  # Probability of success

# PMF (Probability Mass Function)
pmf_0 = bernoulli.pmf(0, p)  # P(X=0)
pmf_1 = bernoulli.pmf(1, p)  # P(X=1)

# Generate random samples
samples = bernoulli.rvs(p, size=1000)

# Mean and variance
mean = p
variance = p * (1 - p)
```

### Binomial Distribution
```python
from scipy.stats import binom

n = 10  # Number of trials
p = 0.3  # Probability of success

# PMF
pmf = binom.pmf(k, n, p)  # P(X=k)

# CDF (Cumulative Distribution Function)
cdf = binom.cdf(k, n, p)  # P(X<=k)

# Generate random samples
samples = binom.rvs(n, p, size=1000)

# Mean and variance
mean = n * p
variance = n * p * (1 - p)

# Example: P(X >= 5) in 10 trials with p=0.3
prob = 1 - binom.cdf(4, 10, 0.3)
```

### Poisson Distribution
```python
from scipy.stats import poisson

lambda_ = 5  # Average rate

# PMF
pmf = poisson.pmf(k, lambda_)  # P(X=k)

# CDF
cdf = poisson.cdf(k, lambda_)  # P(X<=k)

# Generate random samples
samples = poisson.rvs(lambda_, size=1000)

# Mean and variance
mean = lambda_
variance = lambda_

# Example: Events per hour
# If average is 5 events/hour, what's P(exactly 3 events)?
prob = poisson.pmf(3, 5)
```

### Geometric Distribution
```python
from scipy.stats import geom

p = 0.3  # Probability of success

# PMF (number of trials until first success)
pmf = geom.pmf(k, p)

# CDF
cdf = geom.cdf(k, p)

# Generate random samples
samples = geom.rvs(p, size=1000)

# Mean and variance
mean = 1 / p
variance = (1 - p) / (p ** 2)
```

## Continuous Probability Distributions

### Uniform Distribution
```python
from scipy.stats import uniform

a, b = 0, 10  # Range [a, b]

# PDF (Probability Density Function)
pdf = uniform.pdf(x, loc=a, scale=b-a)

# CDF
cdf = uniform.cdf(x, loc=a, scale=b-a)

# Generate random samples
samples = uniform.rvs(loc=a, scale=b-a, size=1000)

# Mean and variance
mean = (a + b) / 2
variance = ((b - a) ** 2) / 12
```

### Normal (Gaussian) Distribution
```python
from scipy.stats import norm

mu = 0      # Mean
sigma = 1   # Standard deviation

# PDF
pdf = norm.pdf(x, loc=mu, scale=sigma)

# CDF
cdf = norm.cdf(x, loc=mu, scale=sigma)

# Inverse CDF (quantile function)
quantile = norm.ppf(0.95, loc=mu, scale=sigma)

# Generate random samples
samples = norm.rvs(loc=mu, scale=sigma, size=1000)

# Z-score
z = (x - mu) / sigma

# Empirical Rule (68-95-99.7)
# ~68% within 1 std: [mu-sigma, mu+sigma]
# ~95% within 2 std: [mu-2*sigma, mu+2*sigma]
# ~99.7% within 3 std: [mu-3*sigma, mu+3*sigma]
```

### Exponential Distribution
```python
from scipy.stats import expon

lambda_ = 2  # Rate parameter

# PDF
pdf = expon.pdf(x, scale=1/lambda_)

# CDF
cdf = expon.cdf(x, scale=1/lambda_)

# Generate random samples
samples = expon.rvs(scale=1/lambda_, size=1000)

# Mean and variance
mean = 1 / lambda_
variance = 1 / (lambda_ ** 2)

# Memoryless property: P(X > s+t | X > s) = P(X > t)
```

### Chi-Squared Distribution
```python
from scipy.stats import chi2

df = 5  # Degrees of freedom

# PDF
pdf = chi2.pdf(x, df)

# CDF
cdf = chi2.cdf(x, df)

# Critical value
critical_value = chi2.ppf(0.95, df)

# Generate random samples
samples = chi2.rvs(df, size=1000)

# Mean and variance
mean = df
variance = 2 * df
```

### t-Distribution
```python
from scipy.stats import t

df = 10  # Degrees of freedom

# PDF
pdf = t.pdf(x, df)

# CDF
cdf = t.cdf(x, df)

# Critical value (two-tailed)
alpha = 0.05
critical_value = t.ppf(1 - alpha/2, df)

# Generate random samples
samples = t.rvs(df, size=1000)

# Note: As df → ∞, t-distribution → normal distribution
```

### F-Distribution
```python
from scipy.stats import f

dfn = 5   # Numerator degrees of freedom
dfd = 10  # Denominator degrees of freedom

# PDF
pdf = f.pdf(x, dfn, dfd)

# CDF
cdf = f.cdf(x, dfn, dfd)

# Critical value
critical_value = f.ppf(0.95, dfn, dfd)

# Generate random samples
samples = f.rvs(dfn, dfd, size=1000)
```

## Expected Value and Variance

### Expected Value
```python
# Discrete: E[X] = Σ x * P(X=x)
expected_value = np.sum(values * probabilities)

# For distribution
expected_value = distribution.mean()
```

### Variance
```python
# Var(X) = E[(X - μ)²] = E[X²] - (E[X])²
variance = distribution.var()

# Standard deviation
std_dev = np.sqrt(variance)
```

### Properties
```python
# E[aX + b] = a*E[X] + b
# Var(aX + b) = a²*Var(X)

# For independent X and Y:
# E[X + Y] = E[X] + E[Y]
# Var(X + Y) = Var(X) + Var(Y)
```

## Joint and Marginal Distributions

### Joint Probability
```python
# P(X=x, Y=y)
joint_prob = joint_distribution[x, y]

# From data
joint_prob_table = pd.crosstab(df['X'], df['Y'], normalize='all')
```

### Marginal Probability
```python
# P(X=x) = Σ P(X=x, Y=y) for all y
marginal_X = joint_distribution.sum(axis=1)
marginal_Y = joint_distribution.sum(axis=0)
```

### Independence
```python
# X and Y are independent if P(X,Y) = P(X)*P(Y)
is_independent = np.allclose(
    joint_distribution,
    np.outer(marginal_X, marginal_Y)
)
```

### Covariance and Correlation
```python
# Covariance: Cov(X,Y) = E[(X-μx)(Y-μy)]
covariance = np.cov(X, Y)[0, 1]

# Correlation: ρ = Cov(X,Y) / (σx * σy)
correlation = np.corrcoef(X, Y)[0, 1]

# Properties:
# -1 ≤ ρ ≤ 1
# ρ = 0: uncorrelated (not necessarily independent)
# ρ = ±1: perfect linear relationship
```

## Law of Large Numbers

```python
# Sample mean converges to expected value as n → ∞
np.random.seed(42)
n_samples = [10, 100, 1000, 10000, 100000]
true_mean = 0.3

for n in n_samples:
    samples = np.random.binomial(1, true_mean, n)
    sample_mean = np.mean(samples)
    print(f"n={n:6d}: sample mean = {sample_mean:.4f}")
```

## Central Limit Theorem

```python
# Distribution of sample means approaches normal as n increases
# Regardless of original distribution

# Example: Uniform distribution samples
n_samples = 1000
sample_size = 30

sample_means = []
for _ in range(n_samples):
    sample = np.random.uniform(0, 1, sample_size)
    sample_means.append(np.mean(sample))

# Sample means are approximately normal
plt.hist(sample_means, bins=50, density=True, alpha=0.7)
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.title('Distribution of Sample Means (CLT)')

# Overlay normal distribution
mu = np.mean(sample_means)
sigma = np.std(sample_means)
x = np.linspace(min(sample_means), max(sample_means), 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
plt.show()
```

## Monte Carlo Simulation

```python
def monte_carlo_simulation(n_simulations=10000):
    """Estimate probability using Monte Carlo method"""
    
    # Example: Estimate π using random points
    inside_circle = 0
    
    for _ in range(n_simulations):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    pi_estimate = 4 * inside_circle / n_simulations
    return pi_estimate

pi_est = monte_carlo_simulation(100000)
print(f"π estimate: {pi_est:.4f}")
print(f"True π: {np.pi:.4f}")
```

## Common Probability Calculations

### Confidence Intervals
```python
from scipy import stats

# For mean (known std)
confidence = 0.95
z_critical = stats.norm.ppf((1 + confidence) / 2)
margin_error = z_critical * (sigma / np.sqrt(n))
ci = (sample_mean - margin_error, sample_mean + margin_error)

# For mean (unknown std)
t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)
margin_error = t_critical * (sample_std / np.sqrt(n))
ci = (sample_mean - margin_error, sample_mean + margin_error)
```

### Probability of Range
```python
# P(a < X < b)
prob = distribution.cdf(b) - distribution.cdf(a)

# P(X > a)
prob = 1 - distribution.cdf(a)

# P(X < a)
prob = distribution.cdf(a)
```

## Quick Reference

| Distribution | Parameters | Mean | Variance |
|-------------|------------|------|----------|
| Bernoulli | p | p | p(1-p) |
| Binomial | n, p | np | np(1-p) |
| Poisson | λ | λ | λ |
| Geometric | p | 1/p | (1-p)/p² |
| Uniform | a, b | (a+b)/2 | (b-a)²/12 |
| Normal | μ, σ | μ | σ² |
| Exponential | λ | 1/λ | 1/λ² |
| Chi-squared | df | df | 2·df |

---
[← Back to Main](../README.md)
