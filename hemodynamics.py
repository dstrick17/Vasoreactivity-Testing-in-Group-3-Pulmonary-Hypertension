import pandas as pd

file_path = "C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx"
df = pd.read_excel(file_path)
 # To display all columns
pd.set_option('display.max_columns', None) 

columns_of_interest = [
    "Age At Cath", "RAP", "RVSP", "RVDP", "mPAP", "PCWP", "CO", "CI", "PVR", 
    "Post NO mPAP", "Post NO PCWP", "Post NO CO", "Post NO CI", "Post NO PVR (dynes-sec/cm5)", 
    "Post NO PVR", "∆ mPAP", "∆ PCWP", "∆ CO", "∆ CI", "∆ PVR", 'BNP level (pg/ml)'
]
# Make lists called "Data" to store the results
data = []

# loop through each column and collect the mean, sample size and standard deviation
for column in columns_of_interest:
    if column in df.columns:
        mean_value = df[column].mean()
        std_dev = df[column].std()
        sample_size = df[column].count()

        data.append([column, sample_size, mean_value, std_dev])
    else:
        data.append([column, 0 , None, None])

# Create DataFrame to neatly display in a tabluar format
results_df = pd.DataFrame(data, columns=["Column", "Sample Size", "Mean", "Standard Deviation"])

print(results_df)