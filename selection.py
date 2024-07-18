#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:30:03 2024

@author: vishweshpalani
"""

from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class SelectionSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        sorted_idx = []
        frames = [(self.arr.copy(), [0], list(sorted_idx))]
        
        size = len(self.arr)
        
        #SORT!
        
        for i in range(size):
            min_val, min_idx = float("inf"), i
            for j in range(i+1, size):
                if self.arr[j] < min_val:
                    min_idx, min_val = j, self.arr[j]
                    
                    #bookkeeping
                    frames.append((self.arr.copy(), [j], list(sorted_idx)))
                    
            self.arr[min_idx], self.arr[i] = self.arr[i], self.arr[min_idx]
            sorted_idx.append(i)
            
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=100, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = SelectionSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())