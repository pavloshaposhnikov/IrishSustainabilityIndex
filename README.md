# Irish Cities Sustainability Index

A simple data analysis project comparing sustainability metrics across Irish cities.

**By:** Shaposhnikov Pavlo  
**Student ID:** 22370072@studentmail.ul.ie  
**Program:** Final Year Economics & Finance  
**Purpose:** Application for Trinity College Dublin Master's Program in Statistics and Sustainability

## Overview

This project analyzes sustainability in 10 Irish cities using four key metrics:
- **Air Quality**: PM2.5 levels from EPA Ireland
- **Green Spaces**: Percentage of city area that's green
- **Public Transport**: Transport accessibility scores
- **Waste Management**: Recycling rates from local authorities

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the analysis:**
```bash
python main.py
```

3. **View results:**
- Results will be displayed in the terminal
- HTML report will be created in `docs/` folder

## Project Structure

```
├── main.py                 # Main script to run everything
├── src/                    # Source code
│   ├── data_collector.py   # Collects data from Irish sources
│   ├── show_results.py     # Displays results and creates HTML
│   └── setup.py           # Setup script
├── data/                   # Data files (JSON format)
├── results/                # Analysis results (CSV, JSON)
├── docs/                   # Documentation and reports
│   ├── realistic_project_story.md
│   └── *.html reports
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Methodology

1. **Data Collection**: Gather data from Irish government sources
2. **Normalization**: Convert all metrics to 0-100 scale
3. **Weighting**: Equal weights (25% each pillar)
4. **Aggregation**: Simple average of normalized scores
5. **Ranking**: Sort cities by composite score

## Results

The analysis reveals interesting patterns:
- **Galway** ranks highest (58.4/100) with balanced performance
- **Dublin** ranks lowest (25.0/100) because of the lack of data
- **Smaller cities** often outperform larger ones

## Data Sources

- **EPA Ireland**: Air quality monitoring data
- **OpenStreetMap**: Green space calculations
- **Irish Transport Authorities**: Public transport data
- **Local Authorities**: Waste management statistics

**Key Learning Outcomes:**
- Python programming from scratch
- Data collection and cleaning
- Basic statistical analysis
- Data visualization
- Reproducible research practices

## Limitations

- Uses simplified methodology (equal weighting)
- Basic statistical methods (no advanced ML)
- Limited to available data sources
- Focus on Irish cities only

## Future Improvements

- More sophisticated weighting methods
- Additional sustainability metrics
- International comparisons
- Interactive visualizations
- Machine learning approaches

## Contact

**Email:** 22370072@studentmail.ul.ie  
**University:** University of Limerick  
**Program:** Economics & Finance (Final Year)

---
