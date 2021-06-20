#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
def sumsquare(x):
    y  = len(x)
    z = x
    sum = 0
    for i in range(y):
      z[i]*=z[i]
      sum += z[i]
      
    return sum

def sumsquare2d(f):
    k = np.empty((4,1))
    k[:] = np.NaN
    r = len(f)
    for j in range(r):
        arrsum = sumsquare(f[j])
        k[j] = arrsum
    return k
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(sumsquare2d(T))


# In[ ]:




