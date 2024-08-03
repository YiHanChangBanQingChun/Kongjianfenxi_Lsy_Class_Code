import os
from osgeo import gdal, ogr

# 设置输入文件夹路径和输出文件夹路径
input_folder = r'E:\上课资料\kongjainfenxi_gdb\tudiliyong\guangdong'
output_folder = r'E:\上课资料\kongjainfenxi_gdb\tudiliyong\zhongshan'

# 读取边界文件
boundary_shapefile = r'E:\上课资料\kongjainfenxi_gdb\kongjianfenxi_lsy_mission\shp_location\zhongshan_boundary.shp'
boundary_data_source = ogr.Open(boundary_shapefile)
if boundary_data_source is None:
    print(f'Failed to open {boundary_shapefile}')
    exit(1)

boundary_layer = boundary_data_source.GetLayer()
if boundary_layer is None:
    print(f'Failed to get layer from {boundary_shapefile}')
    exit(1)

# 遍历2000年到2023年的tif文件
for year in range(2000, 2024):
    # 构建tif文件路径
    tif_file = os.path.join(input_folder, f'CLCD_v01_{year}_albert_guangdong.tif')
    
    # 如果文件存在
    if os.path.exists(tif_file):
        # 打开tif文件
        ds = gdal.Open(tif_file)
        if ds is None:
            print(f'Could not open {tif_file}')
            continue
        
        # 创建输出文件路径
        output_tif_file = os.path.join(output_folder, f'CLCD_v01_{year}_albert_zhongshan.tif')
        
        # 进行裁剪
        gdal.Warp(output_tif_file, ds, cutlineDSName=boundary_shapefile, cropToCutline=True)
        
        print(f'Processed {tif_file}')

print('All files processed.')
