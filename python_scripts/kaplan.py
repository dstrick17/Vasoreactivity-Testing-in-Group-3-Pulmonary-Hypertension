import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
# Set the font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df["event_occurred"] = df["Death"].astype(str).apply(lambda x: 1 if x == 'Yes' else 0)

# Create dataframes based on conditions
conditions = [
    ('PVR', 6.3), # Median PVR
    ('mPAP', 35), # Median mPAP
    ('∆ PVR', 1.2), # Median ∆ PVR
    ('∆ mPAP', 5) # Median ∆ mPAP
]

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
fig.suptitle('Kaplan-Meier Curves Evaluating the Effects of PVR and mPAP on Survival', fontsize=16)

# Labels for the subplots
labels = ['A', 'B', 'C', 'D']

# x = axes[i//2, i%2] selects the subplot location. i//2 = row, i%2 = column
for i, (variable, median) in enumerate(conditions):
    ax = axes[i//2, i%2]
    df_low = df[df[variable] <= median]
    df_high = df[df[variable] > median]

    kmf_low = KaplanMeierFitter()
    kmf_high = KaplanMeierFitter()

    kmf_low.fit(df_low["Time in months"], event_observed=df_low["event_occurred"], label=f'{variable} <= {median} (n={len(df_low)})')
    kmf_high.fit(df_high["Time in months"], event_observed=df_high["event_occurred"], label=f'{variable} > {median} (n={len(df_high)})')

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

    ax.set_xlabel('Time in Months')
    ax.set_ylabel('Survival Probability')
    ax.text(0.7, 0.7, f'Log-rank p-value: {results.p_value:.4f}', transform=ax.transAxes, ha='center', va='center', color='red', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the layout

# Save the figure with high resolution (600 dpi for line tone)
fig.savefig("kaplan_meier_curves.jpg", dpi=600, format='jpeg', bbox_inches='tight')

plt.show()