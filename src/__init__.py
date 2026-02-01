"""
Business Assist Data Analysis Package

This package provides tools for business data analysis including:
- Business metrics calculation
- Data visualization
- Sample data generation
"""

__version__ = "1.0.0"
__author__ = "Business Buddy Team"

from .business_analyzer import BusinessMetricsAnalyzer, load_business_data, generate_summary_report
from .visualizations import (
    plot_revenue_trend,
    plot_segment_comparison,
    plot_distribution,
    plot_correlation_heatmap,
    create_dashboard
)

__all__ = [
    'BusinessMetricsAnalyzer',
    'load_business_data',
    'generate_summary_report',
    'plot_revenue_trend',
    'plot_segment_comparison',
    'plot_distribution',
    'plot_correlation_heatmap',
    'create_dashboard'
]
