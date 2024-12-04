import numpy as np
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
n=np.array(arr)
print('So chieu',n.ndim)
print('so hang va cot',n.shape)
print('So phan tu',n.size)
#tạo một arr từ 1 list có sẵn
print('Tạo array từ list->reshape')
a=[1,2,3,4,5,6,7,8,9]
n=np.array(a).reshape(3,3)
print(n)
#tạo array bằng arange(begin,end,step)
print('Tạo array bằng arange(begin,end,step)->arange')
b=np.arange(0,11)
print(b)
#Tạo array mà các phần tử cách đều nhau
print('Tạo array mà các phần tử cách đều nhau->linspace')
c=np.linspace(1,10,5)
print(c)
#Tạo array toàn 0 hoặc 1
print('Tạo mảng toàn 0 hoặc 1')
d=np.zeros((3,3))
print(d)
e=np.ones((2,3))
print(e)
#tạo array tùy ý
q=np.full((3,5),6.9)
print(q)
#Truy cập phần tử
arr=[
    [1,3,5],
    [5,7,9],
    [9,11,13]
]
a=np.array(arr)
print(a[1][0])
print(a[0,:])
print(a[:,-2])
#Kiểm tra tồn tại của phần tử trong mảng
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j]==5:
            print(i,j)