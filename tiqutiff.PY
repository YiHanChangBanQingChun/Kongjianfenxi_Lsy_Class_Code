import os
import shutil

# 定义原始文件夹路径
base_folder = r'E:\上课资料\kongjainfenxi_gdb\tudiliyong\UNZIP'

# 定义目标文件夹路径
target_folder = r'E:\上课资料\kongjainfenxi_gdb\tudiliyong\guangdong'

# 遍历2000年到2022年的文件夹
for year in range(2000, 2023):
    # 构建每年的文件夹路径
    year_folder = os.path.join(base_folder, f'CLCD_v01_{year}_albert_province')
    guangdong_file_path = os.path.join(year_folder, f'CLCD_v01_{year}_albert_guangzhou.tif')
# 如果广东省的 tiff 文件存在，则复制到目标文件夹
    if os.path.exists(guangdong_file_path):
        # 构建目标文件的新文件名，可以根据需要修改
        new_filename = f'CLCD_v01_{year}_albert_guangdong.tif'
        # 构建目标文件的完整路径
        target_file_path = os.path.join(target_folder, new_filename)
        
        # 重命名文件并复制到目标文件夹
        os.rename(guangdong_file_path, target_file_path)
        