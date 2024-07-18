#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:46:05 2024

@author: vishweshpalani
"""

from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class InsertionSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        sorted_idx = []
        frames = [(self.arr.copy(), [0], list(sorted_idx))]
        
        size = len(self.arr)
        
        #SORT!
        
        for i in range(size):
            j = i - 1
            while j >= 0:
                swap = False
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swap = True
                    
                    #bookkeeping
                    sorted_idx.append(j+1)
                    frames.append((self.arr.copy(), [j], list(sorted_idx)))
                    
                if swap == False:
                    break
                j -= 1
            sorted_idx = []
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=100, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = InsertionSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())