import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_excel("YOUR-PATH-TO-XML-FILE")

# Drop rows with any NaN values in the dataframe to simplify the example
df = df.dropna()

# Select only numerical columns for normality testing
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Dictionary to hold the normality test results
normality_results = {}

for column in numerical_cols:
    # Perform Shapiro-Wilk test
    stat, p_value = stats.shapiro(df[column])
    normality_results[column] = p_value

    # Check normality
    if p_value > 0.05:
        print(f"Normal distribution for {column}: Mean ± SD should be used.")
    else:
        print(f"Non-normal distribution for {column}: Median [IQR] should be used.")

# Optionally, display the p-values for review
print("P-values from Shapiro-Wilk tests:", normality_results)