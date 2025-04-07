import pandas as pd

# Load the dataset
file_path = "PATH-TO-YOUR-XML-FILE"
df = pd.read_excel(file_path)

# Ensure the data does not contain NaN values in the relevant column
df = df.dropna(subset=['∆ PCWP'])  # Adjust column name as necessary

# Define the threshold for significant increase in PCWP
threshold_increase = 2  # Example threshold in mmHg

# Count the number of patients with a significant increase in PCWP
significant_increase_count = df[df['∆ PCWP'] > threshold_increase].shape[0]

# Calculate descriptive statistics
mean_change = df['∆ PCWP'].mean()
std_change = df['∆ PCWP'].std()
median_change = df['∆ PCWP'].median()
q1_change = df['∆ PCWP'].quantile(0.25)
q3_change = df['∆ PCWP'].quantile(0.75)
max_change = df['∆ PCWP'].max()

# Print the results
print(f'Number of patients with a significant increase in PCWP during iNO testing: {significant_increase_count}')
print(f'Mean change in PCWP: {mean_change:.2f} ± {std_change:.2f}')
print(f'Median change in PCWP: {median_change:.2f} [{q1_change:.2f}, {q3_change:.2f}]')
print(f'Maximum change in PCWP: {max_change:.2f}')