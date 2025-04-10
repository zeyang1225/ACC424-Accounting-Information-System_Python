#def analyze_benfords_law(numbers):
    # Extract first digits
    first_digits = [int(str(abs(num))[0]) for num in numbers if num != 0]

    # Calculate Actual Frequencies
    digit_counts = pd.Series(first_digits).value_counts().sort_index()
    actual_frequencies = digit_counts / len(first_digits)

    # Define Benford's Expected Frequencies
    expected_frequencies = pd.Series({
        1: 0.301, 2: 0.176, 3: 0.125, 4: 0.097,
        5: 0.079, 6: 0.067, 7: 0.058, 8: 0.051, 9: 0.046
    })

    # Compare Actual and Expected Frequencies
    comparison = pd.DataFrame({
        'Actual': actual_frequencies,
        'Expected': expected_frequencies,
        'Difference': abs(actual_frequencies - expected_frequencies)
    })

    return comparison

if __name__ == "__main__":
    sample_data = [
        1234, 2345, 3456, 1478, 1599, 1788,
        2876, 3981, 1002, 1234, 5438, 1123
    ]
    results = analyze_benfords_law(sample_data)
    print("Benford's Law Analysis Results:")
    print(results)

    # Check for Significant Deviations
    significant_deviations = results[results['Difference'] > 0.05]
    if not significant_deviations.empty:
        print("\nSignificant deviations found for digits:")
        for index, row in significant_deviations.iterrows():
            print(f"Digit {index}: Expected {row['Expected']:.3f}, Actual {row['Actual']:.3f}")


            import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class ARAgingAnalysis:
    def __init__(self, as_of_date=None):
        """Initialize AR Aging Analysis with analysis date"""
        self.as_of_date = pd.to_datetime(as_of_date) if as_of_date else pd.Timestamp.now()
        self.risk_rates = {
            'Current': 0.005,  # 0.5%
            '1-30': 0.02,      # 2%
            '31-60': 0.05,     # 5%
            '61-90': 0.10,     # 10%
            'Over 90': 0.25    # 25%
        }

    def assign_aging_bucket(self, days_outstanding):
        """Assign aging bucket based on days outstanding"""
        if days_outstanding <= 0:
            return 'Current'
        elif days_outstanding <= 30:
            return '1-30'
        elif days_outstanding <= 60:
            return '31-60'
        elif days_outstanding <= 90:
            return '61-90'
        else:
            return 'Over 90'

    def analyze_receivables(self, data):
        """Analyze accounts receivable data"""
        df = data.copy()
        df['invoice_date'] = pd.to_datetime(df['invoice_date'])
        df['due_date'] = pd.to_datetime(df['due_date'])
        df['days_outstanding'] = (self.as_of_date - df['due_date']).dt.days
        df['balance'] = df['amount'] - df['payments']
        df['aging_bucket'] = df['days_outstanding'].apply(self.assign_aging_bucket)
        return self.calculate_metrics(df)

    def calculate_metrics(self, df):
        """Calculate key metrics"""
        bucket_totals = df.groupby('aging_bucket')['balance'].sum()
        total_receivables = bucket_totals.sum()
        bucket_percentages = (bucket_totals / total_receivables * 100).round(2)
        avg_collection_period = ((df['days_outstanding'] * df['balance']).sum() / df['balance'].sum()).round(2)
        bad_debt_estimate = sum(bucket_totals[bucket] * self.risk_rates.get(bucket, 0) for bucket in bucket_totals.index)
        
        return {
            'detailed_aging': df,
            'bucket_totals': bucket_totals,
            'bucket_percentages': bucket_percentages,
            'avg_collection_period': avg_collection_period,
            'bad_debt_estimate': bad_debt_estimate,
            'total_receivables': total_receivables
        }

    def visualize_aging(self, results):
        """Visualize aging data"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        results['bucket_percentages'].plot(
            kind='pie', autopct='%1.1f%%', ax=ax1, title='AR Aging Distribution'
        )
        results['bucket_totals'].plot(
            kind='bar', ax=ax2, title='AR Aging Amounts', color='skyblue'
        )
        plt.show()

if __name__ == "__main__":
    sample_data = pd.DataFrame({
        'invoice_date': ['2024-01-01', '2024-01-15', '2023-12-01', '2023-11-15'],
        'due_date': ['2024-02-01', '2024-02-15', '2024-01-01', '2023-12-15'],
        'customer': ['CustomerA', 'CustomerB', 'CustomerC', 'CustomerA'],
        'amount': [1000.00, 2000.00, 1500.00, 3000.00],
        'payments': [0.00, 1000.00, 500.00, 0.00]
    })
    analyzer = ARAgingAnalysis(as_of_date='2024-02-15')
    results = analyzer.analyze_receivables(sample_data)
    print(f"Total Receivables: ${results['total_receivables']:.2f}")
    analyzer.visualize_aging(results)



    import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Create financial data
data = {
    "Year": [2020, 2021, 2022, 2023],
    "Revenue": [180000, 120000, 150000, 180000],
    "GrossProfit": [40000, 48000, 60000, 72000],
    "CurrentAssets": [50000, 55000, 60000, 65000],
    "CurrentLiabilities": [25000, 30000, 35000, 40000],
    "NetIncome": [10000, 14400, 22500, 32400]
}
df = pd.DataFrame(data)

# Calculate financial ratios
df['Gross Profit Margin'] = (df['GrossProfit'] / df['Revenue']) * 100
df['Current Ratio'] = df['CurrentAssets'] / df['CurrentLiabilities']
df['Net Profit Margin'] = (df['NetIncome'] / df['Revenue']) * 100
print(df[['Year', 'Gross Profit Margin', 'Current Ratio', 'Net Profit Margin']])

# Static visualizations
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Gross Profit Margin', data=df, marker='o')
plt.title('Gross Profit Margin Over Time')
plt.xlabel('Year')
plt.ylabel('Gross Profit Margin (%)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Current Ratio', data=df, marker='o', color='red')
plt.title('Current Ratio Over Time')
plt.xlabel('Year')
plt.ylabel('Current Ratio')
plt.grid(True)
plt.show()

# Interactive visualizations
fig = px.line(df, x='Year', y='Gross Profit Margin', title='Gross Profit Margin Over Time')
fig.show()

fig = px.bar(df, x='Year', y='Current Ratio', title='Current Ratio Over Time')
fig.show()

# Predictive analysis
X = df[['Year']]
y = df['Gross Profit Margin']
model = LinearRegression()
model.fit(X, y)
future_years = np.array([[2024], [2025], [2026]])
predictions = model.predict(future_years)
print("Predicted Gross Profit Margins for 2024-2026:")
for year, prediction in zip(future_years, predictions):
    print(f"{year[0]}: {prediction:.2f}%")


    import pandas as pd

# Sample data
data = {
    "Transaction ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Date": ["2023-03-01", "2023-03-02", "2023-03-03", "2023-03-04", "2023-03-05", "March 1, 2023"],
    "Amount": [100, 200, 150, 5000, 100000, 50],
    "Customer Name": ["Alice", "Bob", "Charlie", None, "Eve", "Frank"],
    "Region": ["West", "North", "South", "East", "East", None]
}
df = pd.DataFrame(data)

# Find missing values in 'Customer Name'
missing_values = df[df["Customer Name"].isnull()]
print("Rows with missing 'Customer Name':")
print(missing_values)

# Find duplicate Transaction IDs
duplicates = df[df.duplicated("Transaction ID", keep=False)]
print("Duplicate Transactions:")
print(duplicates)

# Find outliers in 'Amount'
outliers = df[(df["Amount"] < 100) | (df["Amount"] > 10000)]
print("Outliers:")
print(outliers)

# Check for incorrect date formats
incorrect_dates = df[-pd.to_datetime(df["Date"], errors="coerce").notna()]
print("Rows with incorrect date formats:")
print(incorrect_dates)


import pandas as pd

# Sample transaction data
sample_transactions = [
    {'TransactionID': 1001, 'TransactionDate': '2023-01-15', 'UserID': 'U001',
     'VendorID': 'V100', 'InvoiceNumber': 'INV001', 'TransactionAmount': 5000.00,
     'ApproverID': 'U005', 'PaymentMethod': 'ACH', 'AccountCode': '5010'},
    {'TransactionID': 1002, 'TransactionDate': '2023-01-16', 'UserID': 'U002',
     'VendorID': 'V200', 'InvoiceNumber': 'INV002', 'TransactionAmount': 12500.00,
     'ApproverID': 'U006', 'PaymentMethod': 'Check', 'AccountCode': '5020'},
    {'TransactionID': 1003, 'TransactionDate': '2023-01-16', 'UserID': 'U003',
     'VendorID': 'V100', 'InvoiceNumber': 'INV003', 'TransactionAmount': 3200.50,
     'ApproverID': 'U005', 'PaymentMethod': 'ACH', 'AccountCode': '5010'},
    {'TransactionID': 1004, 'TransactionDate': '2023-01-17', 'UserID': 'U001',
     'VendorID': 'V300', 'InvoiceNumber': 'INV004', 'TransactionAmount': 7800.75,
     'ApproverID': 'U006', 'PaymentMethod': 'Wire', 'AccountCode': '5030'},
    {'TransactionID': 1005, 'TransactionDate': '2023-01-18', 'UserID': 'U004',
     'VendorID': 'V200', 'InvoiceNumber': 'INV005', 'TransactionAmount': 15000.00,
     'ApproverID': 'U007', 'PaymentMethod': 'Check', 'AccountCode': '5020'},
    {'TransactionID': 1006, 'TransactionDate': '2023-01-18', 'UserID': 'U002',
     'VendorID': 'V100', 'InvoiceNumber': 'INV001', 'TransactionAmount': 5000.00,
     'ApproverID': 'U002', 'PaymentMethod': 'ACH', 'AccountCode': '5010'}
]
transactions = pd.DataFrame(sample_transactions)
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

# Transaction Limit Check
limit_exceptions = transactions[
    (transactions['TransactionAmount'] > 10000) &
    (transactions['ApproverID'].isna())
]
print("\nTransactions Over $10k Without Approval:")
print(limit_exceptions[['TransactionID', 'UserID', 'TransactionAmount']])

# Segregation of Duties (SoD) Check
activity_log = pd.DataFrame([
    {'UserID': 'U001', 'Action': 'CreateVendor', 'ActivityTimestamp': '2023-01-10 09:15:00'},
    {'UserID': 'U002', 'Action': 'Approve Payment', 'ActivityTimestamp': '2023-01-18 14:30:00'}
])
activity_log['ActivityTimestamp'] = pd.to_datetime(activity_log['ActivityTimestamp'])

sod_violations = pd.merge(
    transactions,
    activity_log,
    on='UserID',
    how='inner'
)
sod_violations = sod_violations[
    sod_violations['Action'].str.contains('Approve')
]
print("\nSoD Violations (User Initiated & Approved):")
print(sod_violations[['TransactionID', 'UserID', 'Action']])

# Data Validation Check
missing_data = transactions[
    transactions['InvoiceNumber'].isna() |
    transactions['VendorID'].isna()
]
print("\nTransactions with Missing Data:")
print(missing_data[['TransactionID', 'InvoiceNumber', 'VendorID']])


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

# Time Series Forecasting
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=365)
trend = 0.001 * np.arange(len(dates))
noise = np.random.normal(0, 0.5, len(dates))
prices = 100 + trend + noise.cumsum()
df = pd.DataFrame({"Price": prices}, index=dates)
df.plot(title="Simulated Stock Prices")
plt.show()

# Feature Engineering
df["Returns"] = df["Price"].pct_change()
df["MA_10"] = df["Price"].rolling(10).mean()
df["Volatility"] = df["Returns"].rolling(20).std() * np.sqrt(252)

# ARIMA Forecasting
model = ARIMA(df["Price"].dropna(), order=(2,1,1))
results = model.fit()
forecast = results.forecast(steps=5)
print("5-Day Forecast:")
print(forecast)

# Customer Segmentation
data = np.column_stack([
    np.random.lognormal(mean=3, sigma=0.5, size=100),  # Account Balance
    np.random.poisson(lam=10, size=100)                # Transactions/month
])
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
labels = kmeans.labels_

# Fraud Detection
normal_tx = np.random.normal(loc=50, scale=10, size=90)
fraud_tx = np.random.uniform(low=500, high=5000, size=10)
transactions = np.concatenate([normal_tx, fraud_tx]).reshape(-1, 1)
clf = IsolationForest(contamination=0.1)
fraud_pred = clf.fit_predict(transactions)
print("\nFraud Detection Results (1=Normal, -1=Fraud):")
print(fraud_pred)


