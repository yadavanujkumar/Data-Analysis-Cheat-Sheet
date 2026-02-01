"""
Complete Data Analysis Workflow Example
========================================

This example demonstrates a full data analysis workflow including:
- Data loading and exploration
- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Model training and evaluation
- Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Set random seed for reproducibility
np.random.seed(42)

# Set plotting style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

print("=" * 60)
print("DATA ANALYSIS WORKFLOW EXAMPLE")
print("=" * 60)

# ============================================================================
# 1. GENERATE SAMPLE DATA
# ============================================================================
print("\n1. Generating sample dataset...")

n_samples = 1000

# Create sample dataset
data = {
    'age': np.random.randint(18, 70, n_samples),
    'income': np.random.normal(50000, 20000, n_samples),
    'education_years': np.random.randint(10, 20, n_samples),
    'work_experience': np.random.randint(0, 30, n_samples),
    'category': np.random.choice(['A', 'B', 'C'], n_samples),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], n_samples)
}

# Create target variable (purchase decision)
purchase_probability = (
    0.01 * data['age'] +
    0.00001 * data['income'] +
    0.05 * data['education_years'] +
    0.02 * data['work_experience'] +
    np.random.normal(0, 0.1, n_samples)
)
purchase_probability = 1 / (1 + np.exp(-purchase_probability))  # Sigmoid
data['purchased'] = (purchase_probability > 0.5).astype(int)

# Introduce some missing values
data['income'][np.random.choice(n_samples, 50, replace=False)] = np.nan
data['work_experience'][np.random.choice(n_samples, 30, replace=False)] = np.nan

df = pd.DataFrame(data)

print(f"Dataset created with {len(df)} rows and {len(df.columns)} columns")

# ============================================================================
# 2. INITIAL DATA EXPLORATION
# ============================================================================
print("\n2. Initial Data Exploration")
print("-" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isna().sum())

# ============================================================================
# 3. DATA CLEANING
# ============================================================================
print("\n3. Data Cleaning")
print("-" * 60)

# Handle missing values
print(f"\nBefore cleaning: {len(df)} rows")

# Impute missing values
df['income'].fillna(df['income'].median(), inplace=True)
df['work_experience'].fillna(df['work_experience'].median(), inplace=True)

print(f"After cleaning: {len(df)} rows")
print(f"Missing values remaining: {df.isna().sum().sum()}")

# ============================================================================
# 4. EXPLORATORY DATA ANALYSIS
# ============================================================================
print("\n4. Exploratory Data Analysis")
print("-" * 60)

# Target variable distribution
print(f"\nTarget Distribution:")
print(df['purchased'].value_counts())
print(f"\nPurchase Rate: {df['purchased'].mean():.2%}")

# Correlation analysis
print("\nCorrelation with target:")
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlations = df[numeric_cols].corr()['purchased'].sort_values(ascending=False)
print(correlations)

# Visualizations
print("\nGenerating visualizations...")

# 1. Target distribution
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
df['purchased'].value_counts().plot(kind='bar', color=['#3498db', '#e74c3c'])
plt.title('Purchase Distribution')
plt.xlabel('Purchased')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'], rotation=0)

# 2. Age distribution by purchase
plt.subplot(2, 2, 2)
df.boxplot(column='age', by='purchased', ax=plt.gca())
plt.title('Age by Purchase Decision')
plt.suptitle('')
plt.xlabel('Purchased')
plt.ylabel('Age')

# 3. Income distribution
plt.subplot(2, 2, 3)
plt.hist(df['income'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Income Distribution')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')

# 4. Correlation heatmap
plt.subplot(2, 2, 4)
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
           center=0, square=True, linewidths=1)
plt.title('Correlation Matrix')

plt.tight_layout()
plt.savefig('eda_visualizations.png', dpi=300, bbox_inches='tight')
print("Saved: eda_visualizations.png")

# ============================================================================
# 5. FEATURE ENGINEERING
# ============================================================================
print("\n5. Feature Engineering")
print("-" * 60)

# Create new features
df['income_per_year_education'] = df['income'] / df['education_years']
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 50, 100], 
                         labels=['Young', 'Middle', 'Senior'])

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=['category', 'city', 'age_group'], 
                            drop_first=True)

print(f"Features after engineering: {len(df_encoded.columns)}")
print(f"New features: {[col for col in df_encoded.columns if col not in df.columns]}")

# ============================================================================
# 6. PREPARE DATA FOR MODELING
# ============================================================================
print("\n6. Preparing Data for Modeling")
print("-" * 60)

# Separate features and target
X = df_encoded.drop('purchased', axis=1)
y = df_encoded['purchased']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set: {len(X_train)} samples")
print(f"Test set: {len(X_test)} samples")

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================================
# 7. MODEL TRAINING
# ============================================================================
print("\n7. Model Training")
print("-" * 60)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
print("Training Random Forest...")
model.fit(X_train_scaled, y_train)
print("Training complete!")

# ============================================================================
# 8. MODEL EVALUATION
# ============================================================================
print("\n8. Model Evaluation")
print("-" * 60)

# Make predictions
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# Calculate metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred, 
                          target_names=['Not Purchased', 'Purchased']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# ROC AUC
roc_auc = roc_auc_score(y_test, y_proba)
print(f"\nROC AUC Score: {roc_auc:.4f}")

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 10 Important Features:")
print(feature_importance.head(10))

# ============================================================================
# 9. VISUALIZE RESULTS
# ============================================================================
print("\n9. Creating Result Visualizations")
print("-" * 60)

plt.figure(figsize=(14, 5))

# Confusion Matrix
plt.subplot(1, 3, 1)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
           xticklabels=['No', 'Yes'], 
           yticklabels=['No', 'Yes'])
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')

# Feature Importance
plt.subplot(1, 3, 2)
top_features = feature_importance.head(10)
plt.barh(range(len(top_features)), top_features['importance'])
plt.yticks(range(len(top_features)), top_features['feature'])
plt.xlabel('Importance')
plt.title('Top 10 Feature Importance')
plt.gca().invert_yaxis()

# ROC Curve
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)

plt.subplot(1, 3, 3)
plt.plot(fpr, tpr, linewidth=2, label=f'ROC (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('model_evaluation.png', dpi=300, bbox_inches='tight')
print("Saved: model_evaluation.png")

# ============================================================================
# 10. SUMMARY
# ============================================================================
print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

print("\nKey Findings:")
print(f"1. Dataset: {len(df)} samples analyzed")
print(f"2. Purchase Rate: {y.mean():.2%}")
print(f"3. Model Performance: ROC AUC = {roc_auc:.4f}")
print(f"4. Top Feature: {feature_importance.iloc[0]['feature']}")
print(f"\nGenerated Visualizations:")
print("- eda_visualizations.png")
print("- model_evaluation.png")

print("\n" + "=" * 60)
print("Example workflow completed successfully!")
print("=" * 60)
