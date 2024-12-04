#Tạo arr viền ngoài là số 1, bên trong là số 0
import numpy as np
a=np.zeros((5,5))
print(a)
# a[1:4,1]=1
# a[1:4,2]=1
# a[1:4,3]=1
a[1:4,1:4]=1
print(a)
#Tạo mảng 8*8 quy luật 0101... dòng cuối ngược lại
arr=np.zeros((8,8))
print(arr)
for column in range(arr.shape[1]):
    if column % 2 != 0:
        arr[0:7,column]=1
    else:
        arr[-1,column]=1
print(arr)
n=[[10,2,3],[4,5,6],[8,9,10]]
m=np.array(n)
print(np.max(m))
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j]==np.max(m):
            print(i,j)