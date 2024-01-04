import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 折れ線グラフ
x_line = [1, 2, 3, 4, 5]
y_line = [2, 4, 3, 10, 8]

sns.lineplot(x=x_line, y=y_line)
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 散布図
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 3, 10, 8]

sns.scatterplot(x=x_scatter, y=y_scatter, color='red', marker='o')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# ヒストグラム
data_hist = [1, 2, 2, 3, 3, 3, 4, 4, 5]

sns.histplot(data_hist, bins=5, color='green', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# ヒートマップ
data_heatmap = np.random.random((5, 5))
sns.heatmap(data_heatmap, cmap='viridis', annot=True)
plt.title('Heatmap Example')
plt.show()

# 散布図行列
data_pairplot = {'A': np.random.random(100), 'B': np.random.random(100), 'C': np.random.random(100)}
df_pairplot = pd.DataFrame(data_pairplot)
sns.pairplot(df_pairplot)
plt.show()

# 箱ひげ図
data_boxplot = [np.random.normal(0, std, 100) for std in range(1, 4)]
sns.boxplot(data=data_boxplot)
plt.title('Boxplot Example')
plt.show()

# バイオリンプロット
data_violinplot = [np.random.normal(0, std, 100) for std in range(1, 4)]
sns.violinplot(data=data_violinplot)
plt.title('Violin Plot Example')
plt.show()

# 棒グラフ
categories_bar = ['Category A', 'Category B', 'Category C']
values_bar = [3, 7, 5]

sns.barplot(x=categories_bar, y=values_bar, hue=categories_bar, palette='pastel', legend=False)
plt.title('Bar Chart Example')
plt.show()

# 円グラフ
labels_pie = ['Category A', 'Category B', 'Category C']
sizes_pie = [3, 7, 5]

plt.pie(sizes_pie, labels=labels_pie, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.axis('equal')
plt.title('Pie Chart Example')
plt.show()
