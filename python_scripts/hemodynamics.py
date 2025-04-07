import pandas as pd

file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)

df.loc[df['Days between 6MWT and cath'] >= 90, '6MWD (meters)'] = None

# To display all columns
pd.set_option('display.max_columns', None)

columns_of_interest = [
    "Age At Cath", "RAP", "RVSP", "RVDP", "mPAP", "PCWP", "CO", "CI", "PVR", 
    "Post NO mPAP", "Post NO PCWP", "Post NO CO", "Post NO CI", "Post NO PVR",
    "∆ mPAP", "∆ PCWP", "∆ CO", "∆ CI", "∆ PVR", 'BNP level (pg/ml)', '6MWD (meters)', 'LVEF (%)'
]

# Data list to store the results
data = []

# Loop through each column and collect the median, IQR
for column in columns_of_interest:
    if column in df.columns:
        median_value = df[column].median()
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        sample_size = df[column].count()

        data.append([column, sample_size, f"{median_value:.2f} [{q1:.2f}, {q3:.2f}]"])
    else:
        data.append([column, 0, None])

# Create DataFrame to neatly display in a tabular format
results_df = pd.DataFrame(data, columns=["Column", "Sample Size", "Median [IQR]"])

print(results_df)