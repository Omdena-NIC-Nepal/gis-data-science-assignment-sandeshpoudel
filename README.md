# GIS Data Science for Climate in Nepal

## Objective
This project analyzes climate data for Nepal using GIS data science techniques to visualize precipitation and temperature trends.

## Setup Instructions
1. Clone the repository for assignment:
git clone https://github.com/Omdena-NIC-Nepal/gis-data-science-assignment-sandeshpoudel.git

## for Data
https://github.com/Desmondonam/Nepal_Climate_change.git

2. Install the required dependencies:
pip install pandas geopandas matplotlib seaborn rasterio


## Data Sources
- **Administrative Boundaries**: `nepal_admin_regions.gpkg`
- **Precipitation Data**: `nepal_precipitation_2020.tif`, `nepal_precipitation_2050.tif`
- **Temperature Data**: `nepal_temperature_2020.tif`
- **Metadata**: `metadata.json`

## Visualizations
1. **Precipitation Trends Map (2020)**
2. **Precipitation Trends Map (2050)**
3. **Temperature Distribution Histogram**
4. **Boxplots for Outlier Analysis**
5. **Correlation Plot Between Temperature and Precipitation**

## Insights
- **Rising precipitation trends** are projected in certain regions by 2050.
- Temperature data shows notable **outliers**, indicating extreme weather conditions.
- Correlation analysis suggests that **higher temperatures tend to align with lower precipitation rates** in some regions.

## How to Run
Run the Python script in your terminal or IDE:

python gis_climate_analysis.py


## Results and Analysis
- Mean Temperature (2020): X°C
- Mean Precipitation (2020): Y mm


