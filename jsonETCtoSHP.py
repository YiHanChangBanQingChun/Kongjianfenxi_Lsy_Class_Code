import os
import geopandas as gpd

# Set the input directory path
input_dir = r'D:\Users\admin\Downloads\chromedownload'

# Set the output directory path
output_dir = r'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian'

# Iterate over the JSON files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        # Read the JSON file as a GeoDataFrame, specify the CRS as WGS84
        json_file = os.path.join(input_dir, filename)
        gdf = gpd.read_file(json_file, crs='EPSG:4326')

        # Set the output file path
        output_file = os.path.join(output_dir, filename.replace('.json', '.shp'))

        # Save the GeoDataFrame as a SHP file
        gdf.to_file(output_file, driver='ESRI Shapefile', encoding='utf-8')
