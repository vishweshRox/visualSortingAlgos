#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:40:56 2024

@author: vishweshpalani
"""
import math
from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class MergeSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        frames = [(self.arr.copy(), [0], [])]
        
        size = len(self.arr)
        
        #SORT!
        
        def merge(i_s, i_e, j_s, j_e):
            #assumes i_s <= i_e && i_e + 1 == j_s && i_s <= j_e
            
            sorted_idx = []
            
            temp_arr = []
            i, j = i_s, j_s
            
            while i <= i_e and j <= j_e:
                if self.arr[i] <= self.arr[j]:
                    temp_arr.append(self.arr[i])
                    i += 1
                else:
                    temp_arr.append(self.arr[j])
                    j += 1
                    
            while i <= i_e:
                temp_arr.append(self.arr[i])
                i += 1
                    
            while j <= j_e:
                temp_arr.append(self.arr[j])
                j += 1
            
            orig_t, new_t = i_s, 0
            
            while orig_t <= j_e:
                self.arr[orig_t] = temp_arr[new_t]
                
                #some bookkeeping
                sorted_idx.append(orig_t)
                frames.append((self.arr.copy(), [orig_t], list(sorted_idx)))
                
                orig_t += 1
                new_t += 1
                
        def split(i, j):
            m = math.floor((i + j) / 2)
            if i != j:
                
                split(i, m)
                split(m+1, j)
            
            merge(i, m, m+1, j)
            
        split(0, size-1)
            
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=500, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = MergeSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())