# Business-Assist-DataAnalysis

This is the data analysis toolkit to support the Business Buddy project. It provides comprehensive tools for analyzing business metrics, visualizing data, and generating insights.

## 📊 Features

- **Business Metrics Analysis**: Calculate revenue, profit, customer metrics, and KPIs
- **Data Visualization**: Generate professional charts and dashboards
- **Segment Analysis**: Analyze performance by product category, region, or custom segments
- **Growth Analysis**: Track growth rates over time
- **Interactive Notebooks**: Jupyter notebooks for exploratory analysis
- **Sample Data**: Pre-generated sample data for testing and demonstration

## 🚀 Quick Start

### Quick Setup (Recommended)

**Unix/Linux/MacOS:**
```bash
bash setup.sh
```

**Windows:**
```bash
python setup.py
```

This will automatically:
- Install all required dependencies
- Generate sample data for testing
- Set up the project structure

### Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/icancod/Business-Assist-DataAnalysis.git
cd Business-Assist-DataAnalysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Generate Sample Data

```bash
python src/generate_sample_data.py
```

This creates sample sales and customer data in the `data/sample/` directory.

### Run Example Analysis

```bash
python analysis/example_analysis.py
```

This will:
- Load sample sales data
- Calculate business metrics
- Generate visualizations
- Save outputs to the `outputs/` directory

### Interactive Analysis with Jupyter

```bash
jupyter notebook notebooks/interactive_analysis.ipynb
```

## 📁 Project Structure

```
Business-Assist-DataAnalysis/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── data/                              # Data directory
│   ├── sample/                        # Sample data files
│   │   ├── sales_data.csv
│   │   └── customer_data.csv
│   └── raw/                           # Your raw data (gitignored)
│
├── src/                               # Source code
│   ├── business_analyzer.py           # Business metrics analysis
│   ├── visualizations.py              # Visualization functions
│   └── generate_sample_data.py        # Sample data generator
│
├── analysis/                          # Analysis scripts
│   └── example_analysis.py            # Example analysis workflow
│
├── notebooks/                         # Jupyter notebooks
│   └── interactive_analysis.ipynb     # Interactive analysis notebook
│
└── outputs/                           # Generated visualizations
    └── .gitkeep
```

## 🔧 Usage

### Loading Your Own Data

```python
from src.business_analyzer import BusinessMetricsAnalyzer, load_business_data

# Load data from CSV or Excel
data = load_business_data('path/to/your/data.csv')

# Initialize analyzer
analyzer = BusinessMetricsAnalyzer(data)
```

### Calculating Metrics

```python
# Revenue metrics
revenue_metrics = analyzer.calculate_revenue_metrics()
print(f"Total Revenue: ${revenue_metrics['total_revenue']:,.2f}")

# Customer metrics
customer_metrics = analyzer.calculate_customer_metrics()
print(f"Total Customers: {customer_metrics['total_customers']}")

# Segment analysis
segment_stats = analyzer.segment_analysis('product_category', 'revenue')
print(segment_stats)
```

### Creating Visualizations

```python
from src.visualizations import plot_revenue_trend, plot_segment_comparison, create_dashboard

# Revenue trend
plot_revenue_trend(data, 'date', 'revenue', save_path='revenue_trend.png')

# Segment comparison
plot_segment_comparison(data, 'product_category', 'revenue', save_path='category_comparison.png')

# Comprehensive dashboard
create_dashboard(data, 'date', 'revenue', 'product_category', save_path='dashboard.png')
```

## 📋 Data Requirements

Your data should be in CSV or Excel format with the following columns (minimum):

**For Revenue Analysis:**
- `date`: Transaction date
- `revenue`: Revenue amount
- Additional columns as needed (customer_id, product_category, region, etc.)

**For Customer Analysis:**
- `customer_id`: Unique customer identifier
- `revenue`: Revenue per transaction (optional)

## 🎨 Visualization Examples

The toolkit generates several types of visualizations:

1. **Revenue Trends**: Line charts showing revenue over time
2. **Segment Comparisons**: Bar charts comparing metrics across categories
3. **Distribution Plots**: Histograms and box plots for metric distributions
4. **Correlation Heatmaps**: Showing relationships between numeric variables
5. **Comprehensive Dashboards**: Multi-panel views combining multiple visualizations

## 🧪 Running Tests

```bash
# Generate sample data first
python src/generate_sample_data.py

# Run example analysis
python analysis/example_analysis.py
```

## 📊 Sample Data Schema

### Sales Data
- `transaction_id`: Unique transaction identifier
- `date`: Transaction date
- `customer_id`: Customer identifier
- `product_category`: Product category (Electronics, Clothing, Food, Home, Books)
- `region`: Geographic region (North, South, East, West)
- `revenue`: Transaction revenue
- `cost`: Transaction cost
- `quantity`: Number of items
- `profit`: Calculated profit (revenue - cost)

### Customer Data
- `customer_id`: Unique customer identifier
- `customer_name`: Customer name
- `segment`: Customer segment (Premium, Standard, Basic)
- `signup_date`: Customer signup date
- `country`: Customer country
- `lifetime_value`: Customer lifetime value

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Business Buddy** - Empowering businesses with data-driven insights
