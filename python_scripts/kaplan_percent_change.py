
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

# Convert time from days to months
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if x == 'Yes' else 0)

# Create dataframes based on median conditions
conditions = [
    ('% ∆ PVR', 21.06), # Median % ∆ PVR
    ('% ∆ mPAP', 14.71) # Median % ∆ mPAP
]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # Create a 1x2 subplot grid
fig.suptitle('Kaplan-Meier Curves Evaluating the Effects of Median percent change in PVR and median percent change mPAP on Survival', fontsize=20)

# Labels for the subplots
labels = ['A', 'B']

# Loop through the conditions and plot only the median-based graphs
for i, (variable, threshold) in enumerate(conditions):
    ax = axes[i]
    df_low = df[df[variable] <= threshold]
    df_high = df[df[variable] > threshold]

    kmf_low = KaplanMeierFitter()
    kmf_high = KaplanMeierFitter()

    kmf_low.fit(df_low["Time in months"], event_observed=df_low["event_occurred"], label=f'{variable} <= {threshold} (n={len(df_low)})')
    kmf_high.fit(df_high["Time in months"], event_observed=df_high["event_occurred"], label=f'{variable} > {threshold} (n={len(df_high)})')

    kmf_low.plot(ax=ax)
    kmf_high.plot(ax=ax)

    # Perform log-rank test
    results = logrank_test(
        durations_A=df_low["Time in months"],
        event_observed_A=df_low["event_occurred"],
        durations_B=df_high["Time in months"],
        event_observed_B=df_high["event_occurred"]
    )

    # Label each subplot
    ax.text(0.01, 0.95, labels[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

    ax.set_xlabel('Time in Months', fontsize=14)
    ax.set_ylabel('Survival Probability', fontsize=14)
    ax.text(0.8, 0.8, f'Log-rank p-value: {results.p_value:.4f}', transform=ax.transAxes, ha='center', va='center', color='red', fontsize=16)
    ax.legend(fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the layout
plt.show()