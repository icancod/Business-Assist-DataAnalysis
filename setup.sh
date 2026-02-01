#!/bin/bash
# Quick Start Script for Business Assist Data Analysis

echo "=================================="
echo "Business Buddy Data Analysis Setup"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "Error: Python is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null
then
    PYTHON_CMD="python"
fi

echo "Using Python: $PYTHON_CMD"
echo ""

# Install dependencies
echo "Installing dependencies..."
$PYTHON_CMD -m pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

echo ""

# Generate sample data
echo "Generating sample data..."
$PYTHON_CMD src/generate_sample_data.py

if [ $? -eq 0 ]; then
    echo "✓ Sample data generated successfully"
else
    echo "✗ Failed to generate sample data"
    exit 1
fi

echo ""
echo "=================================="
echo "Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "  1. Run example analysis: $PYTHON_CMD analysis/example_analysis.py"
echo "  2. Open Jupyter notebook: jupyter notebook notebooks/interactive_analysis.ipynb"
echo "  3. Or add your own data to data/raw/ and start analyzing!"
echo ""
