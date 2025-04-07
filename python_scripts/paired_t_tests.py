import pandas as pd
from scipy.stats import ttest_rel

file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)

# Ensure the data does not contain NaN values in the columns of interest
df = df.dropna(subset=['mPAP', 'Post NO mPAP', 'PCWP', 'Post NO PCWP', 'CO', 'Post NO CO', 'CI', 'Post NO CI', 'PVR', 'Post NO PVR'])

# Performing paired t-tests
results = {}

# List of parameters to test
parameters = ['mPAP', 'PCWP', 'CO', 'CI', 'PVR']

for param in parameters:
    # Compute the t-test for the pair
    stat, p_value = ttest_rel(df[f'Post NO {param}'], df[param])
    results[param] = (stat, p_value)

# Print the results in a formatted table
print(f"{'Parameter':<15} {'T-statistic':<15} {'P-value':<15}")
print("="*45)
for param, result in results.items():
    stat, p_value = result
    print(f"{param:<15} {stat:<15.3f} {p_value:<15.3f}")