import rasterio

with rasterio.open("./../S2_NDVI.tiff") as src:
    print("NDVI Tiff Bounds:", src.bounds)
    print("CRS:", src.crs)
