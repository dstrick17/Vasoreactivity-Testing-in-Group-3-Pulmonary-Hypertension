import pandas as pd
from scipy.stats import ttest_rel

file_path = "C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx"
df = pd.read_excel(file_path)

# Performing paired t-tests
results = {}

# List of parameters to test
parameters = ['mPAP', 'PCWP', 'CO', 'CI', 'PVR']

for param in parameters:
    # Compute the t-test for the pair
    stat, p_value = ttest_rel(df[f'Post NO {param}'], df[param])
    results[param] = (stat, p_value)

# Print the results
for param, result in results.items():
    stat, p_value = result
    print(f"Paired T-test result for {param}:")
    print(f" T-statistic: {stat:.3f}, P-value: {p_value:.3f}")
