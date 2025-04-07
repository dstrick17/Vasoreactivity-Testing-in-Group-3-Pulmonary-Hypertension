import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
# Set the font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

file_path = "PATH-TO-YOUR-XML-FILE"
df = pd.read_excel(file_path)

# Drop rows with NaN values in the relevant columns
df = df.dropna(subset=["Time from start date to end date (days)", "∆ mPAP", "∆ PVR", "mPAP", "PVR"])

# Convert time from days to months (using average days in a month)
df["Time in months"] = df["Time from start date to end date (days)"] / 30.44

# Identify censored data
df['censored'] = df['Death'] == 'No'

# Set up the matplotlib figure

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
fig.suptitle('Scatter Plots Comparing Various Parameters with Survival Time', fontsize=16)

# Function to plot data and annotate with correlation coefficient and labels A, B, C, D
def plot_data(ax, x, y, xlabel, ylabel, label):
    # Non-censored data
    ax.scatter(df.loc[~df['censored'], x], df.loc[~df['censored'], y], color='blue', label='Subject who experienced mortality before the study end date')
    # Censored data
    ax.scatter(df.loc[df['censored'], x], df.loc[df['censored'], y], color='red', label='Subject who did not experience mortality before the study end date', alpha=0.6)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Calculate and annotate Pearson correlation
    correlation, _ = pearsonr(df[x], df[y])
    ax.text(0.65, 0.95, f'Pearson r: {correlation:.2f}', transform=ax.transAxes, fontsize=12, verticalalignment='top')

    # Label the plot as A, B, C, or D
    ax.text(0.01, 0.98, label, transform=ax.transAxes, fontsize=14, fontweight='bold', verticalalignment='top')

# Scatter plot for PVR
plot_data(axes[0, 0], "PVR", "Time in months", 'Baseline PVR (Wood units)', 'Survival Time (Months)', 'A')

# Scatter plot for mPAP
plot_data(axes[0, 1], "mPAP", "Time in months", 'Baseline mPAP (mmHg)', 'Survival Time (Months)', 'B')

# Scatter plot for ∆ PVR
plot_data(axes[1, 0], "∆ PVR", "Time in months", 'Reduction in PVR during iNO challenge (Wood units)', 'Survival Time (Months)', 'C')

# Scatter plot for ∆ mPAP
plot_data(axes[1, 1], "∆ mPAP", "Time in months", 'Reduction in mPAP during iNO challenge (mmHg)', 'Survival Time (Months)', 'D')

# Add a single legend outside of the subplots
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2, bbox_to_anchor=(0.5, 0.01), fontsize=9.5)

# Adjust layout to reduce white space
plt.subplots_adjust(left=0.08, right=0.98, top=0.92, bottom=0.15, hspace=0.3, wspace=0.2)

# Save the figure with high resolution (1200 dpi for line tone)
fig.savefig("scatter_plots.jpg", dpi=1200, format='jpeg', bbox_inches='tight')

# Show the plot
plt.show()