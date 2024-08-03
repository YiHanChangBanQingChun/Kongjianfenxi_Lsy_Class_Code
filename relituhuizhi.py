import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# 设置全局字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 请将'SimHei'替换为你的系统中的一个中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 读取csv文件
df = pd.read_csv(r'E:\上课资料\kongjainfenxi_gdb\dengshiquangnaichadian\数据汇总.csv', index_col=0)

# 选择需要绘制热力图的列
columns_to_plot = ['商业点覆盖率', '娱乐设施覆盖率', '居民点覆盖率', '学校覆盖率', '人口覆盖率']
df_to_plot = df[columns_to_plot]

# 绘制热力图并获取colorbar对象
plt.figure(figsize=(10, 8))
cax = sns.heatmap(df_to_plot, annot=True, cmap='YlGnBu')

# 设置并旋转y轴的标签
plt.ylabel('区名', rotation=0)
plt.xlabel('覆盖率类型', rotation=0)
# 旋转y轴的标签
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.title('益禾堂30分钟公共交通等时圈于相关设施以及人口覆盖率热力图')
# 获取colorbar对象并设置图例的标签
cbar = cax.collections[0].colorbar
cbar.set_label('范围:0-1', rotation=0)

# 显示图形
plt.show()

