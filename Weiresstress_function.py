#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def Weierstrass_func(x_local):
    #instantiating variables
    kmax=20 
    a=0.5
    b=3
    D=x_local.size     # size of Numpy vector x_local
    weires_i=[0]
    for i,x_i in enumerate(x_local):
        for k in range(kmax):
            weires_i +=np.power(a,k)*(np.cos((2*np.pi)*np.power(b,k)*(x_i+a)))                        -D*(np.power(a,k)*(np.pi*np.cos((2*np.pi*np.power(b,k))*(a))))
    return weires_i  

