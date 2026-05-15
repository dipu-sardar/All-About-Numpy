import pandas as pd
import numpy as np

# =========================
# Load Dataset
# =========================
df = pd.read_csv('/Users/dipusardar/DIPU/Programming/Numpy/z_employee_dataset/dipu.csv')

print("First 5 Rows:\n")
print(df.head())

# =========================
# Check Missing Values
# =========================
print("\nMissing Values in Each Column:\n")
print(df.isnull().sum())

# =========================
# Replace Infinite Values
# =========================
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# =========================
# Fill Missing Salary Values
# =========================
if 'Salary (INR)' in df.columns:
    salary_mean = df['Salary (INR)'].mean()
    df['Salary (INR)'] = df['Salary (INR)'].fillna(salary_mean)

# =========================
# Fill Missing Performance Rating
# =========================
if 'Performance Rating' in df.columns:
    performance_median = df['Performance Rating'].median()
    df['Performance Rating'] = df['Performance Rating'].fillna(performance_median)

# =========================
# Fill Remaining Numeric Missing Values
# =========================
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# =========================
# Remove Duplicate Records
# =========================
df.drop_duplicates(inplace=True)

# =========================
# Replace Negative Salary Values
# =========================
if 'Salary (INR)' in df.columns:
    
    # Recalculate mean salary
    salary_mean = df['Salary (INR)'].mean()

    # Replace negative salary
    df['Salary (INR)'] = np.where(
        df['Salary (INR)'] < 0,
        salary_mean,
        df['Salary (INR)']
    )

# =========================
# Remove Salary Outliers
# =========================
if 'Salary (INR)' in df.columns:

    salary_mean = df['Salary (INR)'].mean()
    salary_std = df['Salary (INR)'].std()

    lower_bound = salary_mean - (3 * salary_std)
    upper_bound = salary_mean + (3 * salary_std)

    df = df[
        (df['Salary (INR)'] >= lower_bound) &
        (df['Salary (INR)'] <= upper_bound)
    ]

# =========================
# Save Cleaned Dataset
# =========================
df.to_csv(
    '/Users/dipusardar/DIPU/Programming/Numpy/z_employee_dataset/dipu_cleaned.csv',
    index=False
)

print("\n✅ Data Cleaning Completed!")
print('Cleaned file saved as "dipu_cleaned.csv"')