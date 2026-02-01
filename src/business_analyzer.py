"""
Business Metrics Analyzer
Provides analysis capabilities for business data including sales, revenue, and customer metrics.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any


class BusinessMetricsAnalyzer:
    """Analyze business metrics and KPIs."""
    
    def __init__(self, data: pd.DataFrame):
        """Initialize with business data."""
        self.data = data
        
    def calculate_revenue_metrics(self) -> Dict[str, float]:
        """Calculate revenue-related metrics."""
        if 'revenue' not in self.data.columns:
            raise ValueError("Data must contain 'revenue' column")
            
        metrics = {
            'total_revenue': self.data['revenue'].sum(),
            'average_revenue': self.data['revenue'].mean(),
            'median_revenue': self.data['revenue'].median(),
            'revenue_std': self.data['revenue'].std(),
            'min_revenue': self.data['revenue'].min(),
            'max_revenue': self.data['revenue'].max()
        }
        return metrics
    
    def calculate_growth_rate(self, date_column: str = 'date', 
                             value_column: str = 'revenue',
                             period: str = 'ME') -> pd.DataFrame:
        """Calculate growth rate over time.
        
        Args:
            date_column: Column name containing dates
            value_column: Column name containing values to analyze
            period: Resampling period ('ME' for month-end, 'QE' for quarter-end, 'YE' for year-end)
        """
        df = self.data.copy()
        df[date_column] = pd.to_datetime(df[date_column])
        df = df.set_index(date_column)
        
        # Resample by period
        resampled = df[value_column].resample(period).sum()
        growth_rate = resampled.pct_change() * 100
        
        result = pd.DataFrame({
            'value': resampled,
            'growth_rate': growth_rate
        })
        return result
    
    def segment_analysis(self, segment_column: str, 
                        metric_column: str = 'revenue') -> pd.DataFrame:
        """Analyze metrics by business segment."""
        if segment_column not in self.data.columns:
            raise ValueError(f"Column '{segment_column}' not found in data")
            
        segment_stats = self.data.groupby(segment_column).agg({
            metric_column: ['sum', 'mean', 'count', 'std']
        }).round(2)
        
        # Calculate percentage contribution
        total = self.data[metric_column].sum()
        segment_stats[('percentage', '')] = (
            self.data.groupby(segment_column)[metric_column].sum() / total * 100
        ).round(2)
        
        return segment_stats
    
    def top_performers(self, metric_column: str = 'revenue', 
                       top_n: int = 10) -> pd.DataFrame:
        """Identify top performing records."""
        return self.data.nlargest(top_n, metric_column)
    
    def calculate_customer_metrics(self) -> Dict[str, Any]:
        """Calculate customer-related metrics."""
        required_cols = ['customer_id']
        if not all(col in self.data.columns for col in required_cols):
            raise ValueError("Data must contain 'customer_id' column")
            
        metrics = {
            'total_customers': self.data['customer_id'].nunique(),
            'transactions_per_customer': self.data.groupby('customer_id').size().mean()
        }
        
        if 'revenue' in self.data.columns:
            metrics['revenue_per_customer'] = (
                self.data.groupby('customer_id')['revenue'].sum().mean()
            )
            
        return metrics


def load_business_data(filepath: str) -> pd.DataFrame:
    """Load business data from CSV or Excel file."""
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")


def generate_summary_report(analyzer: BusinessMetricsAnalyzer) -> str:
    """Generate a text summary report of business metrics."""
    report = ["Business Metrics Summary Report", "=" * 50, ""]
    
    try:
        revenue_metrics = analyzer.calculate_revenue_metrics()
        report.append("Revenue Metrics:")
        report.append(f"  Total Revenue: ${revenue_metrics['total_revenue']:,.2f}")
        report.append(f"  Average Revenue: ${revenue_metrics['average_revenue']:,.2f}")
        report.append(f"  Median Revenue: ${revenue_metrics['median_revenue']:,.2f}")
        report.append(f"  Revenue Range: ${revenue_metrics['min_revenue']:,.2f} - ${revenue_metrics['max_revenue']:,.2f}")
        report.append("")
    except (ValueError, KeyError):
        report.append("Revenue metrics not available.")
        report.append("")
    
    try:
        customer_metrics = analyzer.calculate_customer_metrics()
        report.append("Customer Metrics:")
        report.append(f"  Total Customers: {customer_metrics['total_customers']:,}")
        report.append(f"  Avg Transactions/Customer: {customer_metrics['transactions_per_customer']:.2f}")
        if 'revenue_per_customer' in customer_metrics:
            report.append(f"  Revenue per Customer: ${customer_metrics['revenue_per_customer']:,.2f}")
        report.append("")
    except (ValueError, KeyError):
        report.append("Customer metrics not available.")
        report.append("")
    
    return "\n".join(report)
