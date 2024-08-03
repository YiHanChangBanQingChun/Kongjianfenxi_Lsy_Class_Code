import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def calculate_coverage(csv_file, district_file, facility_file, output_file):
    # 读取CSV文件和shapefile文件
    df = pd.read_csv(csv_file,encoding='utf-8')
    district_data = gpd.read_file(district_file)
    district_data2 = gpd.read_file(district_file)
    facility_data = gpd.read_file(facility_file)

    # 将CSV文件中的点数据转换为GeoDataFrame，并将其投影到EPSG:32648
    geometry = [Point(xy) for xy in zip(df['wgs84_lng'], df['wgs84_lat'])]
    df = df.drop(['wgs84_lng', 'wgs84_lat'], axis=1)
    crs = {'init': 'epsg:4326'}
    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
    geo_df = geo_df.to_crs({'init': 'epsg:32648'})

    # 将所有数据框的CRS设置为EPSG:32648
    district_data = district_data.to_crs({'init': 'epsg:32648'})
    facility_data = facility_data.to_crs({'init': 'epsg:32648'})
    district_data2 = district_data2.to_crs({'init': 'epsg:32648'})
    # 根据各区范围，计算各区点的数量
    district_data = gpd.sjoin(district_data, geo_df, how='left', op='intersects')
    district_data = district_data.drop(columns=['index_right'])
    district_counts = district_data['县区name'].value_counts()
    
    # 根据各区范围分割奶茶店设施面，计算在不同区奶茶店面中点的数量
    print(facility_data)
    print(district_data2)
    facility_data = gpd.overlay(facility_data, district_data2, how='intersection')
    if 'index_right' in facility_data.columns:
        facility_data = facility_data.drop(columns=['index_right'])
    print(facility_data)
    facility_data = gpd.sjoin(facility_data, geo_df, how='left', op='intersects')
    facility_counts = facility_data['县区name'].value_counts()
    # 计算覆盖率并保存结果为CSV文件
    result = pd.DataFrame({
        '区内点数量': district_counts,
        '区内奶茶店面里的点数量': facility_counts,
    })
    result['覆盖率'] = result['区内奶茶店面里的点数量'] / result['区内点数量']
    result.to_csv(output_file)

# 使用函数
csv_file = r"E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\repo_entertainment.csv"
district_file = r'E:\上课资料\kongjainfenxi_gdb\network\guangzhougequmian.shp'
facility_file = r'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\merged.shp'
output_file = r"E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\rate_entertainment.csv"
calculate_coverage(csv_file, district_file, facility_file, output_file)