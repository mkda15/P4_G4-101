# -*- coding: utf-8 -*-

import numpy as np

def peak_dec(X, p, y):
    X = X.T
    sortedX = np.zeros(len(X),dtype = object)
    maxamp = np.max(X)
    limit = maxamp*p
    for i in range(len(X)):
        sortedX[i] = np.sort(X[i])
        max_freq_pos = np.zeros(len(X))
        
        for i in range(len(X)):
            if np.max(X[i]) > limit:
                a = np.where(X[i][:] == np.max(X[i]))
                max_freq_pos[i] = a[0][0]
            else:
                max_freq_pos[i] = 0
        max_freq_t = np.zeros(len(X))
       
        for i in range(len(X)):
            if max_freq_pos[i] == 0:
                max_freq_t[i] = 0
            else:
                max_freq_t[i] = y[int(max_freq_pos[i])]
                
        return max_freq_t