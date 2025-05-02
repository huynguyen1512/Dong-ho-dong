import random
import numpy as np
# Xác suất bắn trúng của Z là 30%
p_Z = 0.3
z=0
a=np.array([0,0,0,0,0,0,0,0,0,0]) #tạo mảng lưu dữ liệu, mỗi phần tử lưu số lần bắn trúng mỗi
lượt
for p in range(10):
for i in range(10):
if random.random() < p_Z:
z+=1
a[p]=z
z=0
print(a)
sum=0
for _ in range(10):
sum+=a[_]
print(sum/10)