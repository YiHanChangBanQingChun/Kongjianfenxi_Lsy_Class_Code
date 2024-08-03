import geopandas as gpd
import glob
import pandas as pd
# 设置输入和输出文件路径
input_folder = 'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian'
output_file = 'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\merged.shp'

# 读取所有的shapefile文件
files = glob.glob(input_folder + '/*.shp')
gdf_list = []

# 合并所有的shapefile文件
for file in files:
    gdf = gpd.read_file(file)
    gdf_list.append(gdf)

merged_gdf = gpd.GeoDataFrame(pd.concat(gdf_list, ignore_index=True))

# 去除重叠部分
merged_gdf = merged_gdf.dissolve()

# 保存合并后的shapefile文件
merged_gdf.to_file(output_file)
