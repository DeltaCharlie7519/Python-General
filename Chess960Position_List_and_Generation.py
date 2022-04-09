#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
from itertools import permutations
pieces = 'KQRrBbNN'
starts = {''.join(p).upper() for p in permutations(pieces)
                     if p.index('B') % 2 != p.index('b') % 2
                     and ( p.index('r') < p.index('K') < p.index('R')
                           or p.index('R') < p.index('K') < p.index('r') ) }       


# In[16]:


print(random.choice(tuple(starts)))


# In[5]:


len(starts)


# In[ ]:




