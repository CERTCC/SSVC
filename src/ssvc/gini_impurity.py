import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Fit a decision tree to the data
clf = DecisionTreeClassifier(criterion="gini", max_depth=2, random_state=42)
clf.fit(X, y)

# Function to calculate Gini impurity for a split
def gini_impurity(feature_column, target):
    total_samples = len(target)
    unique_values = np.unique(feature_column)

    gini = 0.0
    for value in unique_values:
        indices = feature_column == value
        subset = target[indices]
        size = len(subset)
        
        if size == 0:
            continue
        
        # Calculate probability of each class in the subset
        _, counts = np.unique(subset, return_counts=True)
        probabilities = counts / size
        
        # Calculate Gini impurity for the subset
        gini_subset = 1 - np.sum(probabilities**2)
        gini += (size / total_samples) * gini_subset

    return gini

# Example: Calculate Gini impurity for the first feature (sepal length)
first_feature_column = X[:, 0]
gini = gini_impurity(first_feature_column, y)

print("Gini Impurity for the first feature (sepal length):", gini)

# Alternatively, feature importance from the decision tree can hint at splits
print("Feature importances from decision tree:", clf.feature_importances_)

