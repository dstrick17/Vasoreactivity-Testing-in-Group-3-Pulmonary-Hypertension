import pandas as pd
from lifelines import CoxPHFitter

# Ensure all columns in table are displayed
pd.set_option('display.max_columns', None)

file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["BNP level (pg/ml)"])

# Check for leading or trailing whitespace and remove it
df.columns = df.columns.str.strip()

# Adjust 'Age At Cath' to reflect a 10-year increase
df['Age At Cath (10-Year Increase)'] = df['Age At Cath'] / 10

# Adjust 'BNP level (pg/ml)' to reflect a 50 pg/ml increase
df['BNP level (50 pg/ml Increase)'] = df['BNP level (pg/ml)'] / 50

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if 'Yes' in x else (0 if 'No' in x else -1))

# One-hot encode the 'Sex' variable
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# Select the relevant columns for the initial analysis, including covariates
initial_vars = ['Time from start date to end date (days)', 'event_occurred', 'Age At Cath (10-Year Increase)', 'Sex_M', 
                'mPAP', 'CO', 'CI', 'PVR', '∆ PVR', 'BNP level (50 pg/ml Increase)']

# Create a Cox Proportional Hazard model for the initial analysis
cph_initial = CoxPHFitter()

# Perform backward stepwise elimination based on likelihood-ratio test statistics
while True:
    cph_initial.fit(df[initial_vars], duration_col="Time from start date to end date (days)", event_col="event_occurred")
    cph_summary = cph_initial.summary
    p_values = cph_summary['p']
    # Get the variable with the highest p-value
    max_p_value = p_values.max()
    # Check if the p-value exceeds the removal criterion (0.10)
    if max_p_value > 0.10:
        var_to_remove = p_values.idxmax()
        initial_vars.remove(var_to_remove)
    else:
        break


# Create a DataFrame from the summary
summary_df = pd.DataFrame(cph_initial.summary)

# Print the summary of the final multivariate model
print("Final Multivariate Model Summary:")
# print(cph_summary)

# Set the index to the variable names for better readability
summary_df.index = initial_vars[2:]  # Adjust this based on your variable selection

# Print the formatted summary DataFrame with aligned columns
print(summary_df.to_string(index=True, justify='center'))