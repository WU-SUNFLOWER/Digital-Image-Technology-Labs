import numpy as np
import matplotlib.pyplot as plt

source_hist = np.array([2, 57, 704, 1979, 2452, 1501, 1128, 1196, 505, 316, 105, 40, 12, 2, 1, 0], dtype=np.uint32)

# 求分布累计函数
total_pixels = source_hist.sum()
frequencies = source_hist / total_pixels
cumulative_sum = frequencies.cumsum()

# 计算灰度映射关系
M = np.zeros((16,), dtype=np.uint32)
for val in range(0, 16):
    M[val] = min(15, round(15 * cumulative_sum[val]))
    
# 计算变换后图像的直方图
result_hist = np.zeros((16,), dtype=np.uint32)
for val in range(0, 16):
    target_val = M[val]
    result_hist[target_val] += source_hist[val]
    
print(result_hist.sum())
# 绘制图像
fig, (picture1, picture2) = plt.subplots(1, 2, figsize=(25, 6))
picture1.bar(range(16), source_hist)
picture2.bar(range(16), result_hist)
plt.show()
