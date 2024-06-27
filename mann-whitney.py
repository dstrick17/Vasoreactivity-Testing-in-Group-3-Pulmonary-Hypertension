import pandas as pd
from scipy import stats

df = pd.read_excel("C:\\Users\\danst\\codedan\\group3\\group3_data.xlsx")

# Drop rows with NaN values in relevant columns
df = df.dropna(subset=["Time from start date to end date (days)", "∆ PVR"])

# Assuming 'PVR' is the column with the PVR values
df_low_delta_pvr = df[df['∆ PVR'] <= 1.2]
df_high_delta_pvr = df[df['∆ PVR'] > 1.2]

# Normality test
stat, p_low = stats.shapiro(df_low_delta_pvr['PVR'])
stat, p_high = stats.shapiro(df_high_delta_pvr['PVR'])

print(f"Normality test for Low Delta PVR Group: p = {p_low:.3f}")
print(f"Normality test for High Delta PVR Group: p = {p_high:.3f}")

# Perform t-test or Mann-Whitney U test based on normality test results
if p_low > 0.05 and p_high > 0.05:
    # Both groups are normally distributed
    t_stat, p_value = stats.ttest_ind(df_low_delta_pvr['PVR'], df_high_delta_pvr['PVR'])
    print(f"t-test p-value: {p_value:.3f}")
else:
    # Use non-parametric test if any group does not follow normal distribution
    u_stat, p_value = stats.mannwhitneyu(df_low_delta_pvr['PVR'], df_high_delta_pvr['PVR'])
    print(f"Mann-Whitney U test p-value: {p_value:.3f}")
