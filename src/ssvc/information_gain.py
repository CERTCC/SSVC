import pandas as pd
import numpy as np
import io

# Data provided by the user in CSV format
data_csv = """
"Exploitation","Agentic Impact Level","Systemic Impact","Action"
"None","Low","Contained","Track"
"None","Low","Significant","Track"
"None","Low","Critical","Track"
"None","Medium","Contained","Track"
"None","Medium","Significant","Track"
"None","Medium","Critical","Track*"
"None","High","Contained","Track"
"None","High","Significant","Track*"
"None","High","Critical","Attend"
"Public PoC","Low","Contained","Track"
"Public PoC","Low","Significant","Track*"
"Public PoC","Low","Critical","Track"
"Public PoC","Medium","Contained","Track"
"Public PoC","Medium","Significant","Track*"
"Public PoC","Medium","Critical","Attend"
"Public PoC","High","Contained","Attend"
"Public PoC","High","Significant","Attend"
"Public PoC","High","Critical","Act"
"Active","Low","Contained","Track"
"Active","Low","Significant","Track*"
"Active","Low","Critical","Attend"
"Active","Medium","Contained","Attend"
"Active","Medium","Significant","Act"
"Active","Medium","Critical","Act"
"Active","High","Contained","Attend"
"Active","High","Significant","Act"
"Active","High","Critical","Act"
"""

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(io.StringIO(data_csv))

# Define the target variable and features
target = 'Action'
features = df.columns.drop(target)

# Function to calculate entropy
def calculate_entropy(dataframe, target_col):
    """Calculates the entropy of the target column in a DataFrame."""
    class_counts = dataframe[target_col].value_counts()
    total_count = len(dataframe)
    entropy = 0
    for count in class_counts:
        p = count / total_count
        entropy -= p * np.log2(p)
    return entropy

# Function to calculate Information Gain
def calculate_information_gain(dataframe, feature_col, target_col):
    """Calculates the Information Gain for a feature."""
    # Calculate the entropy of the entire dataset
    total_entropy = calculate_entropy(dataframe, target_col)

    # Calculate the weighted average entropy of the feature
    weighted_entropy = 0
    for value in dataframe[feature_col].unique():
        subset = dataframe[dataframe[feature_col] == value]
        subset_entropy = calculate_entropy(subset, target_col)
        subset_weight = len(subset) / len(dataframe)
        weighted_entropy += subset_weight * subset_entropy

    # Calculate Information Gain
    information_gain = total_entropy - weighted_entropy
    return information_gain

# Calculate and print the entropy of the main dataset
entropy_main = calculate_entropy(df, target)
print(f"Entropy of the entire dataset: {entropy_main:.4f}\n")

# Calculate and print the Information Gain for each feature
print("Information Gain for each feature:")
for feature in features:
    ig = calculate_information_gain(df, feature, target)
    print(f"- {feature}: {ig:.4f}")
