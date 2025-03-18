import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import rasterio
from rasterio.plot import show


import json

import os


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


# File paths
base_path = 'Nepal_Climate_change/nepal_climate_data/'
precip_2020_file = os.path.join(base_path, 'nepal_precipitation_2020.tif')
precip_2050_file = os.path.join(base_path, 'nepal_precipitation_2050.tif')
admin_file = os.path.join(base_path, 'nepal_admin_regions.gpkg')

# Load administrative boundaries
admin_regions = gpd.read_file(admin_file)

# Visualizing Precipitation Data (2020) with Admin Boundaries
plt.figure(figsize=(10, 6))
with rasterio.open(precip_2020_file) as precip_2020:
    show(precip_2020, cmap='Blues', title='Precipitation Trends in Nepal (2020)')
    admin_regions.boundary.plot(ax=plt.gca(), color='black', linewidth=0.7)

# Visualizing Future Precipitation Data (2050) with Admin Boundaries
plt.figure(figsize=(10, 6))
with rasterio.open(precip_2050_file) as precip_2050:
    show(precip_2050, cmap='Purples', title='Precipitation Projections for Nepal (2050)')
    admin_regions.boundary.plot(ax=plt.gca(), color='black', linewidth=0.7)

plt.show()


# Load Temperature Data (2020)
with rasterio.open(os.path.join(base_path, 'nepal_temperature_2020.tif')) as temp_2020:
    temperature_data = temp_2020.read(1)  # Read as array

# Flatten data for easier visualization (remove NaN values)
temperature_flattened = temperature_data[~np.isnan(temperature_data)]

# Histogram for Temperature Distribution
plt.figure(figsize=(8, 5))
sns.histplot(temperature_flattened, bins=30, kde=True)
plt.title('Temperature Distribution in Nepal (2020)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Boxplot for Outlier Analysis
plt.figure(figsize=(6, 4))
sns.boxplot(temperature_flattened)
plt.title('Temperature Data Outliers (2020)')
plt.show()



# Extract Precipitation Data as Array
with rasterio.open(precip_2020_file) as precip_2020:
    precip_data_2020 = precip_2020.read(1)

# Flatten data and convert to DataFrame
precip_df = pd.DataFrame({
    'Precipitation': precip_data_2020.flatten()
}).dropna()

# Boxplot to Visualize Precipitation Patterns
plt.figure(figsize=(8, 5))
sns.boxplot(data=precip_df)
plt.title('Precipitation Data Distribution (2020)')
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()





# Combine Temperature and Precipitation Data into DataFrame
combined_df = pd.DataFrame({
    'Temperature': temperature_flattened,
    'Precipitation': precip_data_2020.flatten()
}).dropna()

# Scatterplot to Show Correlation
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Temperature', y='Precipitation', data=combined_df)
plt.title('Temperature vs Precipitation in Nepal (2020)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()



# Compute Basic Statistics for Temperature and Precipitation
print("\n--- Basic Statistics ---")
print(f"Temperature - Mean: {np.mean(temperature_flattened):.2f} °C, "
      f"Min: {np.min(temperature_flattened):.2f} °C, "
      f"Max: {np.max(temperature_flattened):.2f} °C")

print(f"Precipitation - Mean: {np.mean(precip_data_2020):.2f} mm, "
      f"Min: {np.min(precip_data_2020):.2f} mm, "
      f"Max: {np.max(precip_data_2020):.2f} mm")
