import rasterio
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Set interactive backend
import matplotlib.pyplot as plt


# Open the TIFF file
tiff_path = "./../S2_indices_v5_median_0601_0901.tiff"
with rasterio.open(tiff_path) as src:
    # Print metadata
    print("Tiff Bounds:", src.bounds)
    print("CRS:", src.crs)
    print("Width, Height:", src.width, src.height)
    print("Number of bands:", src.count)

    # Read the first band (assuming it's a single-band raster or NDVI index)
    band1 = src.read(1)

# Plot the raster data
plt.figure(figsize=(10, 6))
plt.imshow(band1, cmap='RdYlGn', interpolation='nearest')
plt.colorbar(label="Value")
plt.title("TIFF Visualization")
plt.xlabel("Pixel Column")
plt.ylabel("Pixel Row")
plt.show()

# Plot a histogram of NDVI values
plt.figure(figsize=(8, 5))
plt.hist(band1.flatten(), bins=50, color='green', alpha=0.7)
plt.title("Histogram of Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid()
plt.show()
