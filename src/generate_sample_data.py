"""
Generate sample business data for demonstration and testing.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sample_sales_data(n_records: int = 500) -> pd.DataFrame:
    """Generate sample sales transaction data."""
    np.random.seed(42)
    
    # Generate dates over the last year
    start_date = datetime.now() - timedelta(days=365)
    dates = [start_date + timedelta(days=x) for x in range(365)]
    
    # Generate data
    data = {
        'transaction_id': range(1, n_records + 1),
        'date': np.random.choice(dates, n_records),
        'customer_id': np.random.randint(1001, 1201, n_records),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Home', 'Books'], n_records),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
        'revenue': np.random.gamma(2, 50, n_records).round(2),
        'cost': np.random.gamma(2, 30, n_records).round(2),
        'quantity': np.random.randint(1, 10, n_records)
    }
    
    df = pd.DataFrame(data)
    
    # Calculate profit
    df['profit'] = (df['revenue'] - df['cost']).round(2)
    
    # Ensure positive values
    df['revenue'] = df['revenue'].abs()
    df['cost'] = df['cost'].abs()
    df['profit'] = (df['revenue'] - df['cost']).round(2)
    
    return df


def generate_customer_data(n_customers: int = 200) -> pd.DataFrame:
    """Generate sample customer data."""
    np.random.seed(42)
    
    data = {
        'customer_id': range(1001, 1001 + n_customers),
        'customer_name': [f'Customer_{i}' for i in range(1001, 1001 + n_customers)],
        'segment': np.random.choice(['Premium', 'Standard', 'Basic'], n_customers, p=[0.2, 0.5, 0.3]),
        'signup_date': pd.date_range(start='2020-01-01', periods=n_customers, freq='D'),
        'country': np.random.choice(['USA', 'UK', 'Canada', 'Australia', 'Germany'], n_customers),
        'lifetime_value': np.random.gamma(3, 200, n_customers).round(2)
    }
    
    df = pd.DataFrame(data)
    df['lifetime_value'] = df['lifetime_value'].abs()
    
    return df


def save_sample_data():
    """Generate and save sample data to CSV files."""
    # Generate sales data
    sales_df = generate_sample_sales_data(500)
    sales_df.to_csv('data/sample/sales_data.csv', index=False)
    print(f"Generated sales data: {len(sales_df)} records")
    print(f"Saved to: data/sample/sales_data.csv")
    
    # Generate customer data
    customer_df = generate_customer_data(200)
    customer_df.to_csv('data/sample/customer_data.csv', index=False)
    print(f"\nGenerated customer data: {len(customer_df)} records")
    print(f"Saved to: data/sample/customer_data.csv")
    
    # Print sample of sales data
    print("\n" + "="*50)
    print("Sample Sales Data (first 5 rows):")
    print("="*50)
    print(sales_df.head())
    
    print("\n" + "="*50)
    print("Sample Customer Data (first 5 rows):")
    print("="*50)
    print(customer_df.head())


if __name__ == '__main__':
    save_sample_data()
