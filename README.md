# The Jupyter code for all work in this paper can be found in "all_code.ipynb"
# The figures in the manuscript and supplement can be found in this repository

# Vasoreactivity in Group 3 Pulmonary Hypertension

## Overview
This repository contains a series of Python scripts designed to analyze the impact of vasoreactivity testing on the prognosis of patients with Group 3 pulmonary hypertension. Vasoreactivity testing is a crucial diagnostic tool that may help predict patient outcomes and guide treatment decisions.

## Project Structure
The project consists of 16 Python scripts, each serving a unique purpose in the data analysis pipeline. Three of these scripts generate visualizations to aid in interpreting the data. The data was collected from a de-identified excel sheet built during a study approved by the Tufts Medical Center Institutional Review Board (IRB# 00004908) Titled “A Prospective study of Vasoreactivity and Mortality in WHO Group 3 Pulmonary Hypertension”. As a non-interventional study, it was not entered into clinicaltrials.gov.

### Code

#### Tables


1. **hemodynamics.py**
   - **Description**: Calculates the sample size, mean, and standard deviations for all hemodynamic parameters measured in the study. This ouptuts the data in table 2 in the manuscript.

2. **pft.py**
   - **Description**: Generates a table showing the sample size, mean, and standard deviation of certain pulmonary function test parameters divided into four groups based upon different lung diseases. This ouptuts the data in table 3 in the manuscript.

#### Regression Analysis

3. **cox-univariate.py**
   - **Description**: This is a univariate Cox proportional hazards models were applied to each potential predictor to assess its individual association with mortality.This ouptuts the data in first part of table 4 in the manuscript.

   
4. **cox-stepwise.py**
   - **Description**: Variables demonstrating a p-value of less than 0.10 in these univariate analyses as well as variables considered relevant by clinical expertise including age, sex, and mPAP, were selected for further evaluation. Subsequently, we constructed a multivariate Cox proportional hazards model incorporating these selected variables. A backward stepwise elimination process was implemented to systematically remove variables if their association with the outcome, adjusted for the presence of other variables in the model, resulted in a p-value greater than 0.10. This ouptuts the data in second part of table 4 in the manuscript.

#### Kaplan-Meier Curves

5. **kaplan.py**
   - **Description**: We employed Kaplan-Meier survival analysis to investigate the impact of change in PVR and change in mPAP during iNO challenge as well as baseline PVR and baseline mPAP on survival outcomes within our dataset. Two distinct groups were then created based on the median of change in PVR and mPAP or the median baseline PVR and baseline mPAP. A log rank test was used to statistically compare the survival distributions between the two groups.
   - **Generates Image- Manuscript Figure 1**: Kaplan-Meier estimates survival of two groups of patients in this cohort illustrating the estimated survival probabilities over time (in months). Graph A divides the subjects into two groups based on median baseline PVR of 6.3 wood units. Graph B divides the subjects into two groups based on median baseline mPAP of 35 mm HG. Graph C divides the subjects into two groups based on median reduction in PVR during iNO challenge of 1.2 Wood units. Graph D divides the subjects into two groups based on median reduction in mPAP during iNO challenge of 5 mm HG. Only graph C showed a statistical significance in the survival between the two groups demonstrating that subjects with a greater reduction in PVR during iNO challenge were at an increased risk of mortality than subjects with a lower reduction in PVR. Of note, the average baseline PVR of subjects in the reduction of PVR by more than the median was 9.0 wood units, while the average baseline PVR of subjects in the reduction of PVR by the median or less was only 5.4 wood units. 

6. **kaplan_5_wood_units.py**
   - **Description**: We conducted additional analyses using a threshold of 5 Wood Units to differentiate between mild/moderate and severe PH. Below, we analyzed the survival outcomes between patients with baseline PVR above and below this threshold and included Kaplan-Meier curves for these subgroups in our supplementary materials.
   - **Generates Image- Supplement Figure 2**: There is not a statistically significant difference in survival outcomes between the two groups (p-value of 0.33), suggesting that this particular PVR threshold does not markedly influence prognosis in our cohort of Group 3 PH patients. 

7. **kaplan_percent_change.py**
   - **Description**: We created two additional Kaplan-Meier curves that stratify patients based on the median percent decrease in PVR (21.06%) and mPAP (14.10%). 
   - **Generates Image- Supplement Figure 1**: Our results reveal that the correlation between a higher percentage reduction in PVR and mortality risk was more pronounced, albeit the association showed a weaker correlation (p-value = 0.073) than with absolute decreases. Conversely, the analysis using percent reduction in mPAP did not show a significant correlation (p-value = 0.57).   

#### Linear Regression

8. **linear.py**
   - **Description**: Compares the relationship between baseline pulmonary vascular resistance and the reduction in pulmonary vascular resistance for patients in this study.
   - **Generates Image- Manuscript Figure 2**: Creates a linear regression of baseline PVR in wood units (PVR) compared to reduction in PVR in wood units during inhaled nitric oxide challenge (∆ PVR) with a coefficient of 0.43 and an R-squared value of 0.66.   

#### Scatter Plots

9. **scatter.py**
   - **Description**: Provides a statistical summary of the dataset, including mean, median, and standard deviation calculations.
   - **Generates Image- Manuscript Figure 2**: This scatter plot provides a visual representation of the distribution of survival times relative to mPAP and PVR. Graph A displays the correlation between Baseline PVR and survival for each subject. Graph B displays the correlation between Baseline mPAP and survival for each subject. Graph C displays the correlation between the reduction in PVR during iNO challenge and survival for each subject. Graph D displays the correlation between the reduction in mPAP during iNO challenge and survival for each subject. The pearson correlation coefficient is presented on each graph. 


#### Statistical considerations

10. **paired_t_tests.py**
   - **Description**: Performs paired t-tests to compare pre- and post-test measurements to evaluate the change in hemodynamics from baseline to hemodynamics during inhaled nitric oxide challenge."Post NO" before each parameter means that value was measured during iNO challenge.


11. **mann-whitney.py**
   - **Description**: This test starts by segregating patients into groups based on "∆ PVR" values, and assessing the distribution normality within each group via the Shapiro-Wilk test. Depending on the normality results, the script then chooses between a t-test and a Mann-Whitney U test to statistically compare the PVR between groups with low and high reductions. The outcome explains whether changes in PVR after vasoreactivity testing differ significantly between these groups.

12. **distribution.py**
   - **Description**: Performs a normality test on each numerical column of a dataset to determine the appropriate statistical measures for describing the data. 

#### Additional Analysis

13. **pcwp_vs_pvr.py**
   - **Description**: This script calculates and compares changes in pulmonary vascular resistance (PVR), pulmonary capillary wedge pressure (PCWP), mean pulmonary arterial pressure (mPAP), and cardiac output (CO) between two distinct groups based on their response to the treatment.
14. **significant_pcwp.py**
   - **Description**: This script indicates how many patients experienced a significant increase in PAWP during iNO testing, suggesting latent left heart failure. It also displayes the mean, median and maximum change in PCWP seen in this study.

15. **pwcp_histogram.py**
   - **Description**: This histogram illustrates the distribution of changes in PCWP during iNO testing. 
   **Generates Image- Supplement Figure 3**: This histogram illustrates the change in PCWP for each subject in the study.

16. **vasoreactive.py**
   - **Description**: This code outputs a table demonstrating the demographics, echocardiogram data, pulmonary function test, and hemodynamic parameters for each of the 3 vasoreactive subjects. 

## Requirements
To run these scripts, you will need Python 3.x and the following libraries:
- pandas
- matplotlib
- scipy
- sklearn
- lifelines
