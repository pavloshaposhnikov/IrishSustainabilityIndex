"""
Simple script to display Irish Cities Sustainability Index results.
No web server needed - just shows the data in the terminal and creates an HTML file.
"""

import pandas as pd
import json
import os

def show_results():
    """Display the sustainability rankings and create an HTML report."""
    
    print("🇮🇪 Irish Cities Sustainability Index")
    print("=" * 50)
    
    # Check if data exists
    if not os.path.exists("results/sustainability_rankings.csv"):
        print("❌ No data found. Please run: python3 setup.py first")
        return
    
    # Load the data
    df = pd.read_csv("results/sustainability_rankings.csv")
    
    print(f"📊 Sustainability Rankings for {len(df)} Irish Cities")
    print("=" * 50)
    
    # Display rankings
    print("\n🏆 TOP 10 CITIES:")
    print("-" * 80)
    print(f"{'Rank':<4} {'City':<12} {'Score':<8} {'Air':<6} {'Green':<6} {'Transport':<9} {'Waste':<6}")
    print("-" * 80)
    
    for i, row in df.iterrows():
        print(f"{row['rank']:<4} {row['city']:<12} {row['sustainability_score']:<8.1f} "
              f"{row['air_quality_score']:<6.1f} {row['green_space_score']:<6.1f} "
              f"{row['transport_score_norm']:<9.1f} {row['waste_score']:<6.1f}")
    
    # Summary statistics
    print("\n📈 SUMMARY STATISTICS:")
    print("-" * 30)
    print(f"Best Score:    {df['sustainability_score'].max():.1f}")
    print(f"Worst Score:   {df['sustainability_score'].min():.1f}")
    print(f"Average Score: {df['sustainability_score'].mean():.1f}")
    
    # Top 3 cities
    print("\n🥇 TOP 3 CITIES:")
    print("-" * 20)
    for i in range(min(3, len(df))):
        city = df.iloc[i]
        print(f"{i+1}. {city['city']} - Score: {city['sustainability_score']:.1f}")
    
    # Create HTML report
    create_html_report(df)
    
    print("\n✅ Results displayed successfully!")
    print("📄 HTML report created: irish_sustainability_report.html")
    print("🌐 Open the HTML file in your browser to see the full report")

def create_html_report(df):
    """Create an HTML report file."""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Irish Cities Sustainability Index</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }}
            .content {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #f8f9fa; font-weight: bold; }}
            tr:nth-child(even) {{ background-color: #f8f9fa; }}
            .rank-1 {{ background-color: #fff3cd; }}
            .rank-2 {{ background-color: #e2e3e5; }}
            .rank-3 {{ background-color: #f8d7da; }}
            .score {{ font-weight: bold; color: #28a745; }}
            .summary {{ background: #e9ecef; padding: 20px; border-radius: 5px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🇮🇪 Irish Cities Sustainability Index</h1>
            <p>Real-world analysis of sustainability metrics for Irish cities using data from EPA Ireland, CSO, and local authorities.</p>
        </div>
        
        <div class="content">
            <h2>City Rankings</h2>
            <table>
                <tr>
                    <th>Rank</th>
                    <th>City</th>
                    <th>Overall Score</th>
                    <th>Air Quality</th>
                    <th>Green Space</th>
                    <th>Transport</th>
                    <th>Waste Management</th>
                </tr>
    """
    
    # Add table rows
    for i, row in df.iterrows():
        rank_class = ""
        if i == 0: rank_class = "rank-1"
        elif i == 1: rank_class = "rank-2"
        elif i == 2: rank_class = "rank-3"
        
        html += f"""
                <tr class="{rank_class}">
                    <td><strong>{row['rank']}</strong></td>
                    <td><strong>{row['city']}</strong></td>
                    <td><span class="score">{row['sustainability_score']:.1f}</span></td>
                    <td>{row['air_quality_score']:.1f}</td>
                    <td>{row['green_space_score']:.1f}</td>
                    <td>{row['transport_score_norm']:.1f}</td>
                    <td>{row['waste_score']:.1f}</td>
                </tr>
        """
    
    html += """
            </table>
            
            <div class="summary">
                <h3>Summary Statistics</h3>
                <p><strong>Best Score:</strong> """ + f"{df['sustainability_score'].max():.1f}" + """</p>
                <p><strong>Worst Score:</strong> """ + f"{df['sustainability_score'].min():.1f}" + """</p>
                <p><strong>Average Score:</strong> """ + f"{df['sustainability_score'].mean():.1f}" + """</p>
            </div>
            
            <div class="summary">
                <h3>Data Sources</h3>
                <ul>
                    <li><strong>Air Quality:</strong> EPA Ireland monitoring stations</li>
                    <li><strong>Green Spaces:</strong> OpenStreetMap + CSO analysis</li>
                    <li><strong>Transport:</strong> Irish transport authorities</li>
                    <li><strong>Waste Management:</strong> Local authority reports</li>
                </ul>
            </div>
            
            <div class="summary">
                <h3>Methodology</h3>
                <p>All metrics are normalized to a 0-100 scale, with equal weighting (25% each pillar). 
                The composite sustainability score is the average of the four normalized pillar scores.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save HTML file
    with open("irish_sustainability_report.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    show_results()
