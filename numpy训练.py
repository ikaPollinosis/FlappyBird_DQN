from re import A
import numpy as np
a = np.arange(20).reshape(4,5)
print(a,'\n')
# print(a[1],a[3])
# print(a[:,0],a[:,2])
# print(a[(a%3==0) & (a>10)])
# print(a[2,3],a[1,1])

print(a[:,:1])
print(a[:,1:4])
print(a[:,4:])