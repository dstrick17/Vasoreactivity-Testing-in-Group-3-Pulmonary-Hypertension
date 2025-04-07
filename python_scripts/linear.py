import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
# Set the font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

file_path = "YOUR-PATH-TO-XML-FILE"
df = pd.read_excel(file_path)

# Drop rows with NaN values in the duration column
df = df.dropna(subset=["Time from start date to end date (days)"])

# Select the relevant columns for the analysis
X = df[['PVR']]
y = df['∆ PVR']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Print the coefficients of the linear regression model
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R-squared:", r2_score(y, model.predict(X)))

# Visualize the regression line
plt.scatter(X, y, color='black', label='Data Points')
plt.plot(X, model.predict(X), color='blue', linewidth=3, label='Regression Line')

plt.title('Baseline PVR vs Reduction in PVR during vasoreactivity testing')
plt.xlabel('Baseline PVR (Wood Units)')
plt.ylabel('Reduction in PVR (Wood Units)')
plt.legend()

# Save the figure with high resolution (1200 DPI)
plt.savefig("linear.jpg", dpi=1200, format='jpeg', bbox_inches='tight')

plt.show()