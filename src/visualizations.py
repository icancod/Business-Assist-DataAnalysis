"""
Data Visualization Module
Provides visualization functions for business data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, Tuple


# Set default style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def plot_revenue_trend(data: pd.DataFrame, 
                      date_column: str = 'date',
                      revenue_column: str = 'revenue',
                      title: str = 'Revenue Trend Over Time',
                      save_path: Optional[str] = None) -> None:
    """Plot revenue trend over time."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    df = data.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)
    
    ax.plot(df[date_column], df[revenue_column], marker='o', linewidth=2)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Revenue ($)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_segment_comparison(data: pd.DataFrame,
                           segment_column: str,
                           metric_column: str = 'revenue',
                           title: str = 'Performance by Segment',
                           save_path: Optional[str] = None) -> None:
    """Create bar chart comparing metrics across segments."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    segment_data = data.groupby(segment_column)[metric_column].sum().sort_values(ascending=False)
    
    colors = sns.color_palette("husl", len(segment_data))
    ax.bar(range(len(segment_data)), segment_data.values, color=colors)
    ax.set_xticks(range(len(segment_data)))
    ax.set_xticklabels(segment_data.index, rotation=45, ha='right')
    ax.set_ylabel(f'Total {metric_column.title()}', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # Add value labels on bars
    for i, v in enumerate(segment_data.values):
        ax.text(i, v, f'${v:,.0f}', ha='center', va='bottom')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_distribution(data: pd.DataFrame,
                     column: str,
                     title: str = 'Distribution',
                     save_path: Optional[str] = None) -> None:
    """Plot distribution of a metric."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    ax1.hist(data[column], bins=30, edgecolor='black', alpha=0.7)
    ax1.set_xlabel(column.title(), fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_title(f'{title} - Histogram', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Box plot
    ax2.boxplot(data[column], vert=True)
    ax2.set_ylabel(column.title(), fontsize=12)
    ax2.set_title(f'{title} - Box Plot', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def plot_correlation_heatmap(data: pd.DataFrame,
                            columns: Optional[list] = None,
                            title: str = 'Correlation Heatmap',
                            save_path: Optional[str] = None) -> None:
    """Create correlation heatmap for numeric columns."""
    if columns is None:
        # Select only numeric columns
        numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
        data_to_plot = data[numeric_cols]
    else:
        data_to_plot = data[columns]
    
    corr_matrix = data_to_plot.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                fmt='.2f', ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def create_dashboard(data: pd.DataFrame,
                    date_column: str = 'date',
                    revenue_column: str = 'revenue',
                    segment_column: Optional[str] = None,
                    save_path: Optional[str] = None) -> None:
    """Create a comprehensive dashboard with multiple visualizations."""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # Revenue trend
    ax1 = fig.add_subplot(gs[0, :])
    df_sorted = data.copy()
    df_sorted[date_column] = pd.to_datetime(df_sorted[date_column])
    df_sorted = df_sorted.sort_values(date_column)
    ax1.plot(df_sorted[date_column], df_sorted[revenue_column], marker='o', linewidth=2, color='#2E86AB')
    ax1.set_title('Revenue Trend', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Revenue ($)')
    ax1.grid(True, alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    
    # Revenue distribution
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.hist(data[revenue_column], bins=20, edgecolor='black', alpha=0.7, color='#A23B72')
    ax2.set_title('Revenue Distribution', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Revenue ($)')
    ax2.set_ylabel('Frequency')
    ax2.grid(True, alpha=0.3)
    
    # Box plot
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.boxplot(data[revenue_column], vert=True)
    ax3.set_title('Revenue Box Plot', fontsize=13, fontweight='bold')
    ax3.set_ylabel('Revenue ($)')
    ax3.grid(True, alpha=0.3)
    
    # Segment comparison (if segment column provided)
    if segment_column and segment_column in data.columns:
        ax4 = fig.add_subplot(gs[2, :])
        segment_data = data.groupby(segment_column)[revenue_column].sum().sort_values(ascending=False)
        colors = sns.color_palette("Set2", len(segment_data))
        ax4.bar(range(len(segment_data)), segment_data.values, color=colors)
        ax4.set_xticks(range(len(segment_data)))
        ax4.set_xticklabels(segment_data.index, rotation=45, ha='right')
        ax4.set_title('Revenue by Segment', fontsize=13, fontweight='bold')
        ax4.set_ylabel('Total Revenue ($)')
        ax4.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle('Business Analytics Dashboard', fontsize=16, fontweight='bold', y=0.995)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
