import geopandas as gpd
import pandas as pd
import rasterio
from rasterstats import zonal_stats

def calculate_population_coverage(raster_file, boundary_file, facility_file, output_file):
    # 读取栅格文件
    with rasterio.open(raster_file) as src:
        raster_data = src.read(1)
        affine = src.transform

    # 读取区域边界shapefile
    boundary_data = gpd.read_file(boundary_file)

    # 重命名 '市name' 列为 'city_name'
    boundary_data = boundary_data.rename(columns={'县区name': 'city_name'})

    # 计算每个区域的栅格总和
    district_raster_sum = zonal_stats(boundary_data, raster_data, affine=affine, stats="sum")
    boundary_data['district_population'] = [d['sum'] for d in district_raster_sum]

    # 读取设施覆盖shapefile
    facility_data = gpd.read_file(facility_file)

    # 将设施数据转换到与边界数据相同的CRS
    facility_data = facility_data.to_crs(boundary_data.crs)

    # 分割奶茶店面数据到各区
    facility_data = gpd.overlay(facility_data, boundary_data, how='intersection')

    # 计算奶茶店各区的人口总数
    facility_raster_sum = zonal_stats(facility_data, raster_data, affine=affine, stats="sum")
    facility_data['facility_population'] = [d['sum'] for d in facility_raster_sum]

    # 计算奶茶店覆盖人口率
    facility_data['coverage_rate'] = facility_data['facility_population'] / facility_data['district_population']

    # 保存结果为CSV文件
    result = facility_data[['city_name', 'district_population', 'facility_population', 'coverage_rate']]
    result.to_csv(output_file, index=False)

# 使用函数
tif_file = r"E:\上课资料\kongjainfenxi_gdb\network\repo_pop2020.tif"
district_file = r'E:\上课资料\kongjainfenxi_gdb\network\guangzhougequmian.shp'
facility_file = r'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\merged.shp'
csv_file = r'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\output.csv'
calculate_population_coverage(tif_file, district_file, facility_file, csv_file)