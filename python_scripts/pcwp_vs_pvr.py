import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset
file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)

# Ensure the data does not contain NaN values in the relevant columns
df = df.dropna(subset=['PVR', 'Post NO PVR', 'PCWP', 'Post NO PCWP', 'mPAP', 'Post NO mPAP', 'CO', 'Post NO CO'])

# Step 1: Calculate the change in PVR, PCWP, mPAP, and CO
df['PVR_change'] = df['Post NO PVR'] - df['PVR']
df['PCWP_change'] = df['Post NO PCWP'] - df['PCWP']
df['mPAP_change'] = df['Post NO mPAP'] - df['mPAP']
df['CO_change'] = df['Post NO CO'] - df['CO']

# Step 2: Define the groups based on the absolute median drop in PVR
median_pvr_change = df['PVR_change'].median()
group_high_drop = df[df['PVR_change'] <= median_pvr_change]  # More negative values
group_low_drop = df[df['PVR_change'] > median_pvr_change]    # Less negative or positive values

# Step 3: Calculate the mean change in PVR, PCWP, mPAP, and CO for both groups
mean_pvr_change_high = group_high_drop['PVR_change'].mean()
mean_pvr_change_low = group_low_drop['PVR_change'].mean()
mean_pcwp_change_high = group_high_drop['PCWP_change'].mean()
mean_pcwp_change_low = group_low_drop['PCWP_change'].mean()
mean_mpap_change_high = group_high_drop['mPAP_change'].mean()
mean_mpap_change_low = group_low_drop['mPAP_change'].mean()
mean_co_change_high = group_high_drop['CO_change'].mean()
mean_co_change_low = group_low_drop['CO_change'].mean()

# Step 4: Perform t-tests for each parameter
t_test_pvr = ttest_ind(group_high_drop['PVR_change'], group_low_drop['PVR_change'], equal_var=False)
t_test_pcwp = ttest_ind(group_high_drop['PCWP_change'], group_low_drop['PCWP_change'], equal_var=False)
t_test_mpap = ttest_ind(group_high_drop['mPAP_change'], group_low_drop['mPAP_change'], equal_var=False)
t_test_co = ttest_ind(group_high_drop['CO_change'], group_low_drop['CO_change'], equal_var=False)

# Step 5: Print the results in a formatted table
print(f"{'Group':<20} {'Mean PVR Change (units)':<30} {'Mean PCWP Change (units)':<30} {'Mean mPAP Change (units)':<30} {'Mean CO Change (units)':<30}")
print("="*160)
print(f"{'High Change Group':<20} {mean_pvr_change_high:<30.2f} {mean_pcwp_change_high:<30.2f} {mean_mpap_change_high:<30.2f} {mean_co_change_high:<30.2f}")
print(f"{'Low Change Group':<20} {mean_pvr_change_low:<30.2f} {mean_pcwp_change_low:<30.2f} {mean_mpap_change_low:<30.2f} {mean_co_change_low:<30.2f}")

# Step 6: Print t-test results
print("\nT-Test Results:")
print(f"{'Parameter':<20} {'T-statistic':<20} {'P-value':<20}")
print("="*60)
print(f"{'PVR Change':<20} {t_test_pvr.statistic:<20.4f} {t_test_pvr.pvalue:<20.4f}")
print(f"{'PCWP Change':<20} {t_test_pcwp.statistic:<20.4f} {t_test_pcwp.pvalue:<20.4f}")
print(f"{'mPAP Change':<20} {t_test_mpap.statistic:<20.4f} {t_test_mpap.pvalue:<20.4f}")
print(f"{'CO Change':<20} {t_test_co.statistic:<20.4f} {t_test_co.pvalue:<20.4f}")