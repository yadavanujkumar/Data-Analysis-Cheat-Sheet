# Model Evaluation Cheat Sheet 📊

Comprehensive guide to evaluating machine learning models.

## Classification Metrics

### Confusion Matrix
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Visualize
disp = ConfusionMatrixDisplay(confusion_matrix=cm, 
                              display_labels=['Class 0', 'Class 1'])
disp.plot()
plt.show()

# Manual calculation
TN, FP, FN, TP = cm.ravel()
```

### Binary Classification Metrics

#### Accuracy
```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_true, y_pred)
# accuracy = (TP + TN) / (TP + TN + FP + FN)
```

#### Precision
```python
from sklearn.metrics import precision_score

precision = precision_score(y_true, y_pred)
# precision = TP / (TP + FP)
# "Of predicted positives, how many are actually positive?"
```

#### Recall (Sensitivity, TPR)
```python
from sklearn.metrics import recall_score

recall = recall_score(y_true, y_pred)
# recall = TP / (TP + FN)
# "Of actual positives, how many did we catch?"
```

#### Specificity (TNR)
```python
specificity = TN / (TN + FP)
# "Of actual negatives, how many did we correctly identify?"
```

#### F1 Score
```python
from sklearn.metrics import f1_score

f1 = f1_score(y_true, y_pred)
# f1 = 2 * (precision * recall) / (precision + recall)
# Harmonic mean of precision and recall
```

#### F-beta Score
```python
from sklearn.metrics import fbeta_score

# β < 1: emphasize precision
# β > 1: emphasize recall
f2 = fbeta_score(y_true, y_pred, beta=2)
```

### Multi-class Metrics
```python
from sklearn.metrics import classification_report

# Comprehensive report
report = classification_report(y_true, y_pred)
print(report)

# Average methods for multi-class
precision_micro = precision_score(y_true, y_pred, average='micro')
precision_macro = precision_score(y_true, y_pred, average='macro')
precision_weighted = precision_score(y_true, y_pred, average='weighted')

# 'micro': Calculate globally
# 'macro': Calculate per class, then average
# 'weighted': Weighted average by support
```

### Probability-Based Metrics

#### ROC Curve and AUC
```python
from sklearn.metrics import roc_curve, roc_auc_score, auc

# Get probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_true, y_proba)

# Calculate AUC
roc_auc = roc_auc_score(y_true, y_proba)
# or
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Interpretation:
# AUC = 1.0: Perfect classifier
# AUC = 0.5: Random classifier
# AUC < 0.5: Worse than random
```

#### Precision-Recall Curve
```python
from sklearn.metrics import precision_recall_curve, average_precision_score

# Calculate PR curve
precision, recall, thresholds = precision_recall_curve(y_true, y_proba)

# Average precision
ap = average_precision_score(y_true, y_proba)

# Plot PR curve
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, label=f'PR Curve (AP = {ap:.2f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()

# Use when: Imbalanced classes
```

#### Log Loss
```python
from sklearn.metrics import log_loss

logloss = log_loss(y_true, y_proba)
# Lower is better, 0 is perfect
```

### Threshold Tuning
```python
# Find optimal threshold
from sklearn.metrics import f1_score

thresholds = np.arange(0, 1, 0.01)
f1_scores = []

for threshold in thresholds:
    y_pred_threshold = (y_proba >= threshold).astype(int)
    f1_scores.append(f1_score(y_true, y_pred_threshold))

optimal_threshold = thresholds[np.argmax(f1_scores)]
print(f"Optimal threshold: {optimal_threshold:.2f}")

# Plot
plt.plot(thresholds, f1_scores)
plt.xlabel('Threshold')
plt.ylabel('F1 Score')
plt.title('F1 Score vs Threshold')
plt.axvline(optimal_threshold, color='r', linestyle='--')
plt.show()
```

## Regression Metrics

### Mean Absolute Error (MAE)
```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_true, y_pred)
# mae = mean(|y_true - y_pred|)
# Same units as target variable
```

### Mean Squared Error (MSE)
```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_true, y_pred)
# mse = mean((y_true - y_pred)²)
```

### Root Mean Squared Error (RMSE)
```python
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
# Same units as target variable
# Penalizes large errors more than MAE
```

### Mean Absolute Percentage Error (MAPE)
```python
from sklearn.metrics import mean_absolute_percentage_error

mape = mean_absolute_percentage_error(y_true, y_pred)
# mape = mean(|y_true - y_pred| / |y_true|) * 100
# Expressed as percentage
```

### R-squared (R²)
```python
from sklearn.metrics import r2_score

r2 = r2_score(y_true, y_pred)
# r2 = 1 - (SS_res / SS_tot)
# Range: (-∞, 1], where 1 is perfect
# Proportion of variance explained
```

### Adjusted R-squared
```python
def adjusted_r2(r2, n, p):
    """
    n: number of samples
    p: number of features
    """
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

adj_r2 = adjusted_r2(r2, len(y_true), X.shape[1])
```

### Residual Analysis
```python
# Calculate residuals
residuals = y_true - y_pred

# Plot residuals
plt.figure(figsize=(12, 4))

# Residuals vs Predicted
plt.subplot(1, 3, 1)
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted')

# Histogram of residuals
plt.subplot(1, 3, 2)
plt.hist(residuals, bins=30, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')

# Q-Q plot
plt.subplot(1, 3, 3)
from scipy import stats
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot')

plt.tight_layout()
plt.show()
```

## Clustering Metrics

### Silhouette Score
```python
from sklearn.metrics import silhouette_score, silhouette_samples

# Overall score
score = silhouette_score(X, labels)
# Range: [-1, 1], higher is better
# ~1: well-separated clusters
# ~0: overlapping clusters
# <0: wrong cluster assignment

# Per-sample scores
sample_scores = silhouette_samples(X, labels)
```

### Davies-Bouldin Index
```python
from sklearn.metrics import davies_bouldin_score

score = davies_bouldin_score(X, labels)
# Lower is better, 0 is perfect
```

### Calinski-Harabasz Index
```python
from sklearn.metrics import calinski_harabasz_score

score = calinski_harabasz_score(X, labels)
# Higher is better
```

### Elbow Method (for K-means)
```python
from sklearn.cluster import KMeans

inertias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
```

## Cross-Validation

### K-Fold Cross-Validation
```python
from sklearn.model_selection import cross_val_score, cross_validate

# Single metric
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Multiple metrics
scoring = {
    'accuracy': 'accuracy',
    'precision': 'precision',
    'recall': 'recall',
    'f1': 'f1'
}
scores = cross_validate(model, X, y, cv=5, scoring=scoring)

for metric, values in scores.items():
    if metric.startswith('test_'):
        print(f"{metric[5:]}: {values.mean():.3f} (+/- {values.std():.3f})")
```

### Stratified K-Fold
```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    
    model.fit(X_train, y_train)
    score = model.score(X_val, y_val)
    print(f"Fold {fold + 1}: {score:.3f}")
```

### Time Series Cross-Validation
```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)

for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    
    model.fit(X_train, y_train)
    score = model.score(X_val, y_val)
    print(f"Fold {fold + 1}: {score:.3f}")
```

## Model Comparison

### Compare Multiple Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

results = {}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    results[name] = {
        'mean': scores.mean(),
        'std': scores.std(),
        'scores': scores
    }
    print(f"{name}: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Visualize
plt.figure(figsize=(10, 6))
models_list = list(results.keys())
means = [results[m]['mean'] for m in models_list]
stds = [results[m]['std'] for m in models_list]

plt.bar(models_list, means, yerr=stds, capsize=5)
plt.ylabel('Accuracy')
plt.title('Model Comparison')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Statistical Significance Testing
```python
from scipy.stats import ttest_rel

# Paired t-test to compare two models
model1_scores = cross_val_score(model1, X, y, cv=10)
model2_scores = cross_val_score(model2, X, y, cv=10)

t_stat, p_value = ttest_rel(model1_scores, model2_scores)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Significant difference between models")
else:
    print("No significant difference between models")
```

## Learning Curves

### Plot Learning Curves
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
val_mean = val_scores.mean(axis=1)
val_std = val_scores.std(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training score')
plt.plot(train_sizes, val_mean, label='Validation score')
plt.fill_between(train_sizes, train_mean - train_std, 
                 train_mean + train_std, alpha=0.1)
plt.fill_between(train_sizes, val_mean - val_std, 
                 val_mean + val_std, alpha=0.1)
plt.xlabel('Training Set Size')
plt.ylabel('Accuracy')
plt.title('Learning Curves')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Bias-Variance Tradeoff

### Diagnosis
```python
# High bias (underfitting):
# - Low training score
# - Low validation score
# - Small gap between training and validation

# High variance (overfitting):
# - High training score
# - Low validation score
# - Large gap between training and validation

# Good fit:
# - High training score
# - High validation score
# - Small gap
```

## Model Calibration

### Calibration Curve
```python
from sklearn.calibration import calibration_curve, CalibrationDisplay

# Plot calibration curve
disp = CalibrationDisplay.from_estimator(
    model, X_test, y_test, n_bins=10
)
plt.title('Calibration Curve')
plt.show()

# Interpretation:
# Perfect calibration: curve follows diagonal
# Above diagonal: model underestimates probabilities
# Below diagonal: model overestimates probabilities
```

### Brier Score
```python
from sklearn.metrics import brier_score_loss

brier = brier_score_loss(y_true, y_proba)
# Lower is better, 0 is perfect
# Measures accuracy of probabilistic predictions
```

## Feature Importance

### For Tree-Based Models
```python
# Feature importance
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.bar(range(len(importances)), importances[indices])
plt.xticks(range(len(importances)), 
          [feature_names[i] for i in indices], 
          rotation=45, ha='right')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
```

### Permutation Importance
```python
from sklearn.inspection import permutation_importance

result = permutation_importance(model, X_test, y_test, 
                               n_repeats=10, random_state=42)

sorted_idx = result.importances_mean.argsort()[::-1]

plt.figure(figsize=(10, 6))
plt.barh(range(len(sorted_idx)), result.importances_mean[sorted_idx])
plt.yticks(range(len(sorted_idx)), 
          [feature_names[i] for i in sorted_idx])
plt.xlabel('Permutation Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
```

## Quick Reference

| Metric | Use Case | Better When |
|--------|----------|-------------|
| Accuracy | Balanced classes | Higher |
| Precision | Cost of false positives high | Higher |
| Recall | Cost of false negatives high | Higher |
| F1 Score | Balance precision & recall | Higher |
| ROC AUC | Overall performance | Higher (max 1.0) |
| MAE | Robust to outliers | Lower |
| RMSE | Penalize large errors | Lower |
| R² | Variance explained | Higher (max 1.0) |
| Silhouette | Cluster separation | Higher (max 1.0) |

---
[← Back to Main](../README.md)
