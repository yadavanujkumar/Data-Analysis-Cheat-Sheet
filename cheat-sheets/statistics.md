# Statistics Cheat Sheet 📈

Essential statistical concepts and methods for data analysis.

## Descriptive Statistics

### Central Tendency
```python
import numpy as np
import scipy.stats as stats

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
mode = stats.mode(data)

# Weighted mean
weighted_mean = np.average(data, weights=weights)
```

### Dispersion
```python
# Variance
variance = np.var(data)

# Standard deviation
std = np.std(data)

# Range
data_range = np.max(data) - np.min(data)

# Interquartile range (IQR)
q75, q25 = np.percentile(data, [75, 25])
iqr = q75 - q25

# Mean absolute deviation
mad = np.mean(np.abs(data - np.mean(data)))
```

### Distribution Shape
```python
# Skewness (asymmetry)
skewness = stats.skew(data)
# Negative: left-skewed, Positive: right-skewed

# Kurtosis (tailedness)
kurtosis = stats.kurtosis(data)
# High: heavy tails, Low: light tails
```

### Quantiles and Percentiles
```python
# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75)

# Custom percentiles
p95 = np.percentile(data, 95)
p99 = np.percentile(data, 99)

# Quantile function
quantile = np.quantile(data, [0.25, 0.5, 0.75])
```

## Probability Distributions

### Normal Distribution
```python
from scipy.stats import norm

# PDF (Probability Density Function)
pdf = norm.pdf(x, loc=mean, scale=std)

# CDF (Cumulative Distribution Function)
cdf = norm.cdf(x, loc=mean, scale=std)

# Inverse CDF (Quantile function)
quantile = norm.ppf(0.95, loc=mean, scale=std)

# Generate random samples
samples = norm.rvs(loc=mean, scale=std, size=1000)

# Z-score
z_score = (x - mean) / std
```

### Other Distributions
```python
from scipy.stats import (uniform, expon, poisson, 
                         binom, bernoulli, chi2, t)

# Uniform distribution
uniform.pdf(x, loc=0, scale=1)

# Exponential distribution
expon.pdf(x, scale=1/lambda_)

# Poisson distribution
poisson.pmf(k, mu=lambda_)

# Binomial distribution
binom.pmf(k, n=trials, p=prob)

# Chi-squared distribution
chi2.pdf(x, df=degrees_of_freedom)

# t-distribution
t.pdf(x, df=degrees_of_freedom)
```

## Hypothesis Testing

### One-Sample Tests

#### t-test
```python
# One-sample t-test (compare mean to a value)
t_stat, p_value = stats.ttest_1samp(data, popmean=expected_mean)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
```

#### Z-test
```python
from statsmodels.stats.weightstats import ztest

z_stat, p_value = ztest(data, value=expected_mean)
```

### Two-Sample Tests

#### Independent t-test
```python
# Compare means of two independent groups
t_stat, p_value = stats.ttest_ind(group1, group2)

# With equal variances assumption
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=True)

# Without equal variances (Welch's t-test)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
```

#### Paired t-test
```python
# Compare means of paired samples
t_stat, p_value = stats.ttest_rel(before, after)
```

#### Mann-Whitney U Test (Non-parametric)
```python
# Non-parametric alternative to independent t-test
u_stat, p_value = stats.mannwhitneyu(group1, group2)
```

#### Wilcoxon Signed-Rank Test
```python
# Non-parametric alternative to paired t-test
w_stat, p_value = stats.wilcoxon(before, after)
```

### Multiple Group Tests

#### ANOVA (Analysis of Variance)
```python
# One-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)
```

#### Kruskal-Wallis Test
```python
# Non-parametric alternative to one-way ANOVA
h_stat, p_value = stats.kruskal(group1, group2, group3)
```

### Categorical Data Tests

#### Chi-Square Test
```python
# Chi-square test for independence
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

# Chi-square goodness of fit
chi2_stat, p_value = stats.chisquare(observed, expected)
```

#### Fisher's Exact Test
```python
# For 2x2 contingency tables
odds_ratio, p_value = stats.fisher_exact(table_2x2)
```

## Correlation and Association

### Pearson Correlation
```python
# Linear correlation (-1 to 1)
corr, p_value = stats.pearsonr(x, y)
```

### Spearman Correlation
```python
# Rank-based correlation (non-parametric)
rho, p_value = stats.spearmanr(x, y)
```

### Kendall Tau
```python
# Another rank-based correlation
tau, p_value = stats.kendalltau(x, y)
```

### Correlation Matrix
```python
import pandas as pd

df = pd.DataFrame(data)
correlation_matrix = df.corr()

# With p-values
from scipy.stats import pearsonr

def calculate_pvalues(df):
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = pearsonr(df[r], df[c])[1]
    return pvalues

pvalues = calculate_pvalues(df)
```

## Confidence Intervals

### Mean Confidence Interval
```python
from scipy import stats

# For normal distribution
confidence_level = 0.95
mean = np.mean(data)
sem = stats.sem(data)  # Standard error of mean
interval = stats.t.interval(confidence_level, len(data)-1, 
                           loc=mean, scale=sem)
```

### Proportion Confidence Interval
```python
from statsmodels.stats.proportion import proportion_confint

lower, upper = proportion_confint(successes, trials, 
                                  alpha=0.05, method='normal')
```

## Effect Size

### Cohen's d
```python
def cohens_d(group1, group2):
    """Calculate Cohen's d for effect size"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

# Interpretation: 0.2 = small, 0.5 = medium, 0.8 = large
```

### R-squared
```python
from sklearn.metrics import r2_score

r_squared = r2_score(y_true, y_pred)
```

## Power Analysis

```python
from statsmodels.stats.power import ttest_power

# Calculate statistical power
power = ttest_power(effect_size=0.5, nobs=100, alpha=0.05)

# Calculate required sample size
from statsmodels.stats.power import tt_ind_solve_power

n = tt_ind_solve_power(effect_size=0.5, alpha=0.05, 
                       power=0.8, ratio=1)
```

## Normality Tests

### Shapiro-Wilk Test
```python
stat, p_value = stats.shapiro(data)
# If p < 0.05, data is likely not normal
```

### Kolmogorov-Smirnov Test
```python
stat, p_value = stats.kstest(data, 'norm')
```

### Anderson-Darling Test
```python
result = stats.anderson(data, dist='norm')
# Check result.statistic against result.critical_values
```

### Q-Q Plot (Visual)
```python
import matplotlib.pyplot as plt

stats.probplot(data, dist="norm", plot=plt)
plt.show()
```

## Variance Tests

### Levene's Test (Equal Variances)
```python
stat, p_value = stats.levene(group1, group2)
```

### Bartlett's Test (Equal Variances)
```python
stat, p_value = stats.bartlett(group1, group2, group3)
```

### F-Test (Variance Ratio)
```python
f_stat = np.var(group1, ddof=1) / np.var(group2, ddof=1)
p_value = 1 - stats.f.cdf(f_stat, len(group1)-1, len(group2)-1)
```

## Regression Analysis

### Linear Regression
```python
from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(x, y)

# R-squared
r_squared = r_value ** 2
```

### Multiple Regression
```python
import statsmodels.api as sm

X = sm.add_constant(X)  # Add intercept
model = sm.OLS(y, X).fit()

print(model.summary())
print(f"R-squared: {model.rsquared}")
print(f"Coefficients: {model.params}")
print(f"P-values: {model.pvalues}")
```

## Bootstrap Methods

### Bootstrap Confidence Interval
```python
from scipy.stats import bootstrap

def statistic(data):
    return np.mean(data)

rng = np.random.default_rng()
res = bootstrap((data,), statistic, n_resamples=10000, 
               confidence_level=0.95, random_state=rng)

ci_low, ci_high = res.confidence_interval
```

### Manual Bootstrap
```python
def bootstrap_ci(data, func, n_bootstrap=10000, ci=0.95):
    """Calculate bootstrap confidence interval"""
    bootstrap_samples = []
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_samples.append(func(sample))
    
    alpha = (1 - ci) / 2
    lower = np.percentile(bootstrap_samples, alpha * 100)
    upper = np.percentile(bootstrap_samples, (1 - alpha) * 100)
    return lower, upper

# Example
lower, upper = bootstrap_ci(data, np.mean)
```

## Multiple Testing Correction

### Bonferroni Correction
```python
from statsmodels.stats.multitest import multipletests

# Adjust p-values
reject, pvals_corrected, _, _ = multipletests(pvalues, 
                                              method='bonferroni')
```

### False Discovery Rate (FDR)
```python
reject, pvals_corrected, _, _ = multipletests(pvalues, 
                                              method='fdr_bh')
```

## Outlier Detection

### Z-Score Method
```python
z_scores = np.abs(stats.zscore(data))
outliers = data[z_scores > 3]
```

### IQR Method
```python
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data[(data < lower_bound) | (data > upper_bound)]
```

### Modified Z-Score (MAD)
```python
def modified_z_score(data):
    median = np.median(data)
    mad = np.median(np.abs(data - median))
    modified_z = 0.6745 * (data - median) / mad
    return modified_z

outliers = data[np.abs(modified_z_score(data)) > 3.5]
```

## Common Statistical Patterns

### Standardization (Z-score)
```python
standardized = (data - np.mean(data)) / np.std(data)
```

### Normalization (Min-Max)
```python
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
```

### Rate Calculation with CI
```python
successes = 45
trials = 100
rate = successes / trials
ci = proportion_confint(successes, trials, alpha=0.05)
```

## Key Concepts

### P-value Interpretation
- **p < 0.001**: Very strong evidence against null hypothesis
- **p < 0.01**: Strong evidence against null hypothesis  
- **p < 0.05**: Moderate evidence against null hypothesis (common threshold)
- **p ≥ 0.05**: Insufficient evidence to reject null hypothesis

### Statistical Power
- **Power = 1 - β** (where β is Type II error rate)
- Typically aim for power ≥ 0.80 (80%)
- Higher power = better chance of detecting true effect

### Effect Size Guidelines (Cohen's d)
- **Small**: 0.2
- **Medium**: 0.5
- **Large**: 0.8

## Quick Reference

| Test | When to Use | Python Code |
|------|-------------|-------------|
| t-test (1 sample) | Compare mean to value | `stats.ttest_1samp()` |
| t-test (2 sample) | Compare two means | `stats.ttest_ind()` |
| Paired t-test | Compare paired samples | `stats.ttest_rel()` |
| ANOVA | Compare 3+ groups | `stats.f_oneway()` |
| Chi-square | Test independence | `stats.chi2_contingency()` |
| Pearson correlation | Linear relationship | `stats.pearsonr()` |
| Spearman correlation | Monotonic relationship | `stats.spearmanr()` |
| Shapiro-Wilk | Test normality | `stats.shapiro()` |
| Mann-Whitney U | Non-parametric 2 groups | `stats.mannwhitneyu()` |
| Kruskal-Wallis | Non-parametric 3+ groups | `stats.kruskal()` |

---
[← Back to Main](../README.md)
