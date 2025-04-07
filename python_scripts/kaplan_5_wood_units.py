import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# Set the font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Load the dataset
df = pd.read_excel("YOUR-PATH-TO-XML-FILE")

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if x == 'Yes' else 0)

# Define the threshold for PVR
threshold = 5

# Create dataframes based on the threshold of 5 wood units for PVR (greater than or equal to)
df_low = df[df['PVR'] < threshold]  # PVR < 5
df_high = df[df['PVR'] >= threshold]  # PVR >= 5

# Create Kaplan-Meier Fitter objects
kmf_low = KaplanMeierFitter()
kmf_high = KaplanMeierFitter()

# Fit the model for both groups
kmf_low.fit(df_low["Time in months"], event_observed=df_low["event_occurred"], label=f'PVR < 5 wood units (n={len(df_low)})')
kmf_high.fit(df_high["Time in months"], event_observed=df_high["event_occurred"], label=f'PVR >= 5 wood units (n={len(df_high)})')

# Perform log-rank test
results = logrank_test(
    durations_A=df_low["Time in months"],
    event_observed_A=df_low["event_occurred"],
    durations_B=df_high["Time in months"],
    event_observed_B=df_high["event_occurred"]
)

# Plot the Kaplan-Meier curves
plt.figure(figsize=(10, 6))
kmf_low.plot()
kmf_high.plot()

# Add titles and labels
plt.title('Kaplan-Meier Curves Evaluating Survival Based on Baseline PVR', fontsize=16)
plt.xlabel('Time in Months', fontsize=14)
plt.ylabel('Survival Probability', fontsize=14)

# Remove the vertical line indicating the threshold
# plt.axvline(x=threshold, color='red', linestyle='--', label='Threshold: 5 wood units')  # This line is removed

# Add a legend
plt.legend(fontsize=14)


# Move the p-value to the right of the graph
plt.text(0.70, 0.8, f'Log-rank p-value: {results.p_value:.4f}', fontsize=16, color='red', transform=plt.gca().transAxes)

# Show the plot
plt.tight_layout()
plt.show()