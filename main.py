"""
Irish Cities Sustainability Index
Main script to run the analysis

By: Shaposhnikov Pavlo
Final Year Economics & Finance Student
"""

import sys
import os

# Add src to path so we can import our modules
sys.path.append('src')

from data_collector import IrishDataCollector
from show_results import show_results

def main():
    """Main function to run the sustainability analysis."""
    print("🇮🇪 Irish Cities Sustainability Index")
    print("=" * 50)
    print("By: Shaposhnikov Pavlo")
    print("Final Year Economics & Finance Student")
    print("=" * 50)
    
    # Check if data already exists
    if os.path.exists("data/all_data.json"):
        print("📊 Data already exists. Running analysis...")
        show_results()
    else:
        print("📊 Collecting data first...")
        collector = IrishDataCollector()
        collector.collect_all_data()
        
        print("\n🧮 Running analysis...")
        show_results()

if __name__ == "__main__":
    main()
