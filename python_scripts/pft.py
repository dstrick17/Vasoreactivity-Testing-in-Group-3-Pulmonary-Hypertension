import pandas as pd

file_path = "PATH-TO-YOUR-XML-FILE"
df = pd.read_excel(file_path)

# Filter rows where "Days between PFT and cath" is less than 90
df_filtered = df[df["Days between PFT and cath"] < 90]

# Split the data into three groups based on the type of lung disease
group_Total = df_filtered[df_filtered["type of lung disease"].isin(["Obstructive", "Restrictive", "Combined"])]
group_Obstructive = df_filtered[df_filtered["type of lung disease"] == "Obstructive"]
group_Restrictive = df_filtered[df_filtered["type of lung disease"] == "Restrictive"]
group_Combined = df_filtered[df_filtered["type of lung disease"] == "Combined"]

# Define columns of interest
columns_of_interest = [
    "FVC (L)", "FVC (%)", "FeV1 (L)", "FEV1 (%)", 
    "FeV1/FVC", "TLC (L)", "TLC (%)", "DLCO (L)", "DLCO (%)" 
]

# Define a function to calculate stats
def calculate_stats(group):
    stats = {}
    for col in columns_of_interest:
        # Trim the column name to remove extra spaces for display
        col_name = col.strip()
        sample_size = group[col].count()
        median = round(group[col].median(), 2)  # Median
        q1 = round(group[col].quantile(0.25), 2)  # First quartile
        q3 = round(group[col].quantile(0.75), 2)  # Third quartile
        iqr = round(q3 - q1, 2)  # Interquartile range
        stats[col_name] = f"n={sample_size}, Median [IQR]: {median} [{q1}, {q3}]"
    return stats

# Calculate stats for each group
stats_Total = calculate_stats(group_Total)
stats_Obstructive = calculate_stats(group_Obstructive)
stats_Restrictive = calculate_stats(group_Restrictive)
stats_Combined = calculate_stats(group_Combined)

# Create a DataFrame from the stats for easier comparison
stats_df = pd.DataFrame([stats_Total, stats_Obstructive, stats_Restrictive, stats_Combined], index=['Total', 'Obstructive', 'Restrictive', 'Combined']).transpose()

# Print the formatted DataFrame with aligned columns
print(stats_df.to_string(index=True, justify='center'))