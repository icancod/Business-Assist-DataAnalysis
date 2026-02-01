"""
Example analysis script demonstrating the use of business analysis tools.
"""

import sys
sys.path.append('src')

from business_analyzer import BusinessMetricsAnalyzer, load_business_data, generate_summary_report
from visualizations import plot_revenue_trend, plot_segment_comparison, create_dashboard
import pandas as pd


def main():
    """Run example business analysis."""
    print("="*60)
    print("Business Buddy - Data Analysis Example")
    print("="*60)
    print()
    
    # Load sample data
    print("Loading sample sales data...")
    data = load_business_data('data/sample/sales_data.csv')
    print(f"Loaded {len(data)} records")
    print()
    
    # Initialize analyzer
    analyzer = BusinessMetricsAnalyzer(data)
    
    # Generate and print summary report
    print(generate_summary_report(analyzer))
    
    # Calculate revenue metrics
    print("\nDetailed Revenue Analysis:")
    print("-" * 40)
    revenue_metrics = analyzer.calculate_revenue_metrics()
    for metric, value in revenue_metrics.items():
        print(f"{metric.replace('_', ' ').title()}: ${value:,.2f}")
    
    # Segment analysis by product category
    print("\n\nSegment Analysis by Product Category:")
    print("-" * 40)
    segment_stats = analyzer.segment_analysis('product_category', 'revenue')
    print(segment_stats)
    
    # Segment analysis by region
    print("\n\nSegment Analysis by Region:")
    print("-" * 40)
    region_stats = analyzer.segment_analysis('region', 'revenue')
    print(region_stats)
    
    # Top performers
    print("\n\nTop 10 Transactions by Revenue:")
    print("-" * 40)
    top_10 = analyzer.top_performers('revenue', 10)
    print(top_10[['transaction_id', 'date', 'product_category', 'revenue', 'profit']])
    
    # Growth rate analysis
    print("\n\nMonthly Growth Rate:")
    print("-" * 40)
    growth = analyzer.calculate_growth_rate('date', 'revenue', 'ME')
    print(growth.tail(12))  # Last 12 months
    
    # Create visualizations
    print("\n\nGenerating visualizations...")
    print("Note: Close each plot window to continue...")
    
    # Revenue trend plot
    monthly_data = data.copy()
    monthly_data['date'] = pd.to_datetime(monthly_data['date'])
    monthly_revenue = monthly_data.groupby(monthly_data['date'].dt.to_period('M')).agg({
        'revenue': 'sum'
    }).reset_index()
    monthly_revenue['date'] = monthly_revenue['date'].dt.to_timestamp()
    
    plot_revenue_trend(monthly_revenue, 'date', 'revenue', 
                      'Monthly Revenue Trend',
                      'outputs/revenue_trend.png')
    
    # Segment comparison
    plot_segment_comparison(data, 'product_category', 'revenue',
                          'Revenue by Product Category',
                          'outputs/category_comparison.png')
    
    # Create comprehensive dashboard
    create_dashboard(data, 'date', 'revenue', 'product_category',
                    'outputs/dashboard.png')
    
    print("\nAnalysis complete!")
    print("Visualizations saved to 'outputs/' directory")
    print("="*60)


if __name__ == '__main__':
    main()
