from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# 启动浏览器
driver = webdriver.Chrome(executable_path='D:/Users/admin/Downloads/chromedriver-win64/chromedriver.exe')
# 打开目标网页
url = 'https://ni1o1.github.io/amapreachcircle/'
driver.get(url)
time.sleep(10)
# 找到经纬度文本框
lnglat_input = driver.find_element_by_id('lnglat')

# Open the CSV file
with open(r"E:\上课资料\kongjainfenxi_gdb\gcj_repo_yht_gz_and_ck.csv", 'r',encoding='utf-8') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Get the longitude and latitude from the 9th and 10th columns
        longitude = row[8]
        latitude = row[9]
        # 找到经纬度文本框
        lnglat_input = driver.find_element_by_id('lnglat')
        # Create the coordinates string
        coordinates = f'{longitude},{latitude}'
        
        # Clear the text box
        lnglat_input.clear()
        
        # Enter the coordinates into the text box
        lnglat_input.send_keys(coordinates)
        
        # Find the slider element
        slider = driver.find_element_by_class_name('back-bar')

        # Calculate the desired position in pixels
        desired_position = 158

        # Calculate the offset from the current position
        current_position = int(slider.find_element_by_class_name('selected-bar').get_attribute('style').split('left: ')[1].split('px;')[0])
        offset = desired_position - current_position

        # Move the slider to the desired position
        driver.execute_script("arguments[0].style.left = arguments[1] + 'px';", slider, desired_position)
        # Click the "查询" button
        search_button = driver.find_element_by_id('search')
        search_button.click()

        # Wait for 1 second
        time.sleep(1)

        # Find the "导出geojson" button
        export_geojson_button = driver.find_element_by_xpath("//input[@value='导出geojson']")

        # Click the "导出geojson" button
        export_geojson_button.click()
