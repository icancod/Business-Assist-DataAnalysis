"""
Quick Setup Script for Business Assist Data Analysis
Cross-platform setup for Windows, macOS, and Linux
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Run a command and print status."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        if e.stderr:
            print(e.stderr)
        return False


def main():
    """Run the setup process."""
    print("=" * 50)
    print("Business Buddy Data Analysis Setup")
    print("=" * 50)
    
    # Check Python version
    python_version = sys.version_info
    print(f"\nPython version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)
    
    # Install dependencies
    if not run_command(
        f"{sys.executable} -m pip install -q -r requirements.txt",
        "Installing dependencies"
    ):
        sys.exit(1)
    
    # Generate sample data
    if not run_command(
        f"{sys.executable} src/generate_sample_data.py",
        "Generating sample data"
    ):
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("Setup Complete!")
    print("=" * 50)
    print("\nNext steps:")
    print(f"  1. Run example analysis: {sys.executable} analysis/example_analysis.py")
    print(f"  2. Open Jupyter notebook: jupyter notebook notebooks/interactive_analysis.ipynb")
    print("  3. Or add your own data to data/raw/ and start analyzing!")
    print()


if __name__ == "__main__":
    main()
