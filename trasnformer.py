import gdal
import numpy as np

# Load the two TIFF files
tif1 = gdal.Open(r'E:\上课资料\kongjainfenxi_gdb\kongjianfenxi_lsy_mission\newlocation\guess14rereend.tif')
tif2 = gdal.Open(r'E:\上课资料\kongjainfenxi_gdb\kongjianfenxi_lsy_mission\newlocation\2020100REEND.tif')

# Get the raster bands as arrays
land_use1 = tif1.GetRasterBand(1).ReadAsArray().astype(np.float32)
land_use2 = tif2.GetRasterBand(1).ReadAsArray().astype(np.float32)

# Create an output array for the transition map
transition_map = np.zeros_like(land_use1, dtype=np.float32)

# Define a function to combine values from the two arrays
def combine_values(value1, value2):
    value1 *= 10  # 将第一个数组中的值乘以10
    return value1 + value2

# Iterate over each pixel and combine values from the two arrays
for i in range(land_use1.shape[0]):
    for j in range(land_use1.shape[1]):
        transition_map[i, j] = combine_values(land_use1[i, j], land_use2[i, j])

# Save the transition map to a new TIFF file
driver = gdal.GetDriverByName('GTiff')
output_tif = driver.Create('land_use_transition_map.tif', land_use1.shape[1], land_use1.shape[0], 1, gdal.GDT_Float32)
output_band = output_tif.GetRasterBand(1)
output_band.WriteArray(transition_map)

# Close the files
output_tif = None
tif1 = None
tif2 = None