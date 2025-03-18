import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns


import rasterio
from rasterio.plot import show


import json


# print("All required libraries are installed and working correctly.")

# Load administrative boundary data
file_path = 'Nepal_Climate_change/nepal_climate_data/nepal_admin_regions.gpkg'

# Read the GIS data
climate_data = gpd.read_file(file_path)

# Display the first few rows to inspect the data
print(climate_data.head())

# Inspect dataset structure
print(climate_data.info())

# Check column names to identify key climate variables
print(climate_data.columns)


# Load Precipitation Data (2020)
file_path = 'Nepal_Climate_change/nepal_climate_data/nepal_precipitation_2020.tif'

# Read the raster data
with rasterio.open(file_path) as precip_2020:
    plt.figure(figsize=(8, 6))
    show(precip_2020, cmap='Blues', title='Precipitation Trends in Nepal (2020)')

plt.show()


# Load metadata
with open('Nepal_Climate_change/nepal_climate_data/metadata.json') as file:
    metadata = json.load(file)

# Display metadata content
print(json.dumps(metadata, indent=4))