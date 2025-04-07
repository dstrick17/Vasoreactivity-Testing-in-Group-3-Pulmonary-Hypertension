import pandas as pd
import matplotlib.pyplot as plt
# Set the font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Load the dataset
file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)


# Sort the DataFrame by ∆ PCWP in ascending order
df_sorted = df.sort_values(by='∆ PCWP', ascending=True).reset_index(drop=True)

# Create a vertical bar plot
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted.index, df_sorted['∆ PCWP'], color=['blue' if x > 0 else 'darkred' for x in df_sorted['∆ PCWP']], alpha=0.7, edgecolor='black')

# Add titles and labels
plt.title('Change in PCWP for Each Study Subject', fontsize=16)
plt.xlabel('Study Subject Ordered by ∆ PCWP', fontsize=14)
plt.ylabel('Change in PCWP (mmHg)', fontsize=14)

# Draw a horizontal line at zero for reference
plt.axhline(y=0, color='black', linewidth=1.5, linestyle='--')

# Show grid
plt.grid(axis='y', alpha=0.75)

# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()

# Show the plot
plt.show()