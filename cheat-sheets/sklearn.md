# Scikit-learn Machine Learning Cheat Sheet 🤖

Essential machine learning operations using scikit-learn.

## Installation
```bash
pip install scikit-learn
```

## Importing
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

## Data Preparation

### Train-Test Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Stratified split (for classification)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

### Feature Scaling
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standardization (mean=0, std=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Min-Max Scaling (0 to 1)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Robust Scaling (robust to outliers)
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

## Supervised Learning

### Linear Regression
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
print(f"Score: {model.score(X_test, y_test)}")
```

### Ridge Regression (L2)
```python
from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Lasso Regression (L1)
```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Logistic Regression
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)  # Probabilities
```

### Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

# Classification
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Regression
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Random Forest
```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Classification
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Feature importance
importance = model.feature_importances_
```

### Gradient Boosting
```python
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor

model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, 
                                   max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Support Vector Machine (SVM)
```python
from sklearn.svm import SVC, SVR

# Classification
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Regression
model = SVR(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### K-Nearest Neighbors
```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# Classification
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Regression
model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Naive Bayes
```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB

# Gaussian (continuous features)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Multinomial (count features)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

## Unsupervised Learning

### K-Means Clustering
```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=42)
clusters = model.fit_predict(X)
centers = model.cluster_centers_

# Inertia (within-cluster sum of squares)
inertia = model.inertia_
```

### Hierarchical Clustering
```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3, linkage='ward')
clusters = model.fit_predict(X)
```

### DBSCAN
```python
from sklearn.cluster import DBSCAN

model = DBSCAN(eps=0.5, min_samples=5)
clusters = model.fit_predict(X)
```

### Principal Component Analysis (PCA)
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Explained variance
print(f"Explained variance: {pca.explained_variance_ratio_}")
print(f"Total variance: {pca.explained_variance_ratio_.sum()}")
```

### t-SNE
```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)
```

## Model Evaluation

### Classification Metrics
```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report,
                             roc_auc_score, roc_curve)

# Basic metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Classification report
report = classification_report(y_test, y_pred)
print(report)

# ROC AUC
auc = roc_auc_score(y_test, y_proba[:, 1])
fpr, tpr, thresholds = roc_curve(y_test, y_proba[:, 1])
```

### Regression Metrics
```python
from sklearn.metrics import (mean_squared_error, mean_absolute_error, 
                             r2_score, mean_absolute_percentage_error)

# MSE and RMSE
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# MAE
mae = mean_absolute_error(y_test, y_pred)

# R-squared
r2 = r2_score(y_test, y_pred)

# MAPE
mape = mean_absolute_percentage_error(y_test, y_pred)
```

### Cross-Validation
```python
from sklearn.model_selection import cross_val_score, cross_validate

# Simple cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")

# Multiple metrics
scoring = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(model, X, y, cv=5, scoring=scoring)
```

### K-Fold Cross-Validation
```python
from sklearn.model_selection import KFold, StratifiedKFold

# K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in kf.split(X):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

# Stratified K-Fold (for classification)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
```

## Hyperparameter Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

best_model = grid_search.best_estimator_
```

### Random Search
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 10),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions,
    n_iter=100,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train, y_train)
print(f"Best parameters: {random_search.best_params_}")
```

## Pipelines

### Simple Pipeline
```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

### Pipeline with Feature Selection
```python
from sklearn.feature_selection import SelectKBest, f_classif

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('feature_selection', SelectKBest(f_classif, k=10)),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```

### ColumnTransformer
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

numeric_features = ['age', 'income']
categorical_features = ['gender', 'occupation']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
```

## Feature Engineering

### Polynomial Features
```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
```

### Feature Selection
```python
from sklearn.feature_selection import (SelectKBest, f_classif, 
                                       RFE, SelectFromModel)

# Select K best features
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Recursive Feature Elimination
selector = RFE(estimator=RandomForestClassifier(), n_features_to_select=10)
X_selected = selector.fit_transform(X, y)

# Model-based selection
selector = SelectFromModel(RandomForestClassifier(), threshold='median')
X_selected = selector.fit_transform(X, y)
```

## Handling Imbalanced Data

### Resampling
```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Oversampling (SMOTE)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Undersampling
under = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = under.fit_resample(X_train, y_train)
```

### Class Weights
```python
# Many sklearn models support class_weight parameter
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)
```

## Model Persistence

### Save Model
```python
import joblib

# Save
joblib.dump(model, 'model.pkl')

# Load
model = joblib.load('model.pkl')
```

### Using Pickle
```python
import pickle

# Save
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
```

## Ensemble Methods

### Voting Classifier
```python
from sklearn.ensemble import VotingClassifier

clf1 = LogisticRegression()
clf2 = RandomForestClassifier()
clf3 = GradientBoostingClassifier()

voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('rf', clf2), ('gb', clf3)],
    voting='soft'  # or 'hard'
)
voting_clf.fit(X_train, y_train)
```

### Stacking
```python
from sklearn.ensemble import StackingClassifier

estimators = [
    ('rf', RandomForestClassifier()),
    ('gb', GradientBoostingClassifier())
]

stacking_clf = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)
stacking_clf.fit(X_train, y_train)
```

## Common Workflow

### Complete Classification Pipeline
```python
# 1. Load and prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 3. Define hyperparameters
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, None]
}

# 4. Grid search with cross-validation
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# 5. Evaluate
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")

# 6. Save model
joblib.dump(best_model, 'best_model.pkl')
```

## Quick Reference

| Task | Code |
|------|------|
| Train-test split | `train_test_split(X, y, test_size=0.2)` |
| Standardize | `StandardScaler().fit_transform(X)` |
| Linear Regression | `LinearRegression().fit(X, y)` |
| Logistic Regression | `LogisticRegression().fit(X, y)` |
| Random Forest | `RandomForestClassifier().fit(X, y)` |
| K-Means | `KMeans(n_clusters=3).fit(X)` |
| PCA | `PCA(n_components=2).fit_transform(X)` |
| Cross-validation | `cross_val_score(model, X, y, cv=5)` |
| Grid search | `GridSearchCV(model, params, cv=5)` |
| Save model | `joblib.dump(model, 'file.pkl')` |

---
[← Back to Main](../README.md)
