#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:33:17 2024

@author: vishweshpalani
"""

from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class BubbleSort(Sort):
    def sort(self):
        
        #beginning
        fig, ax, bars = self._prepare()
        sorted_idx = []
        frames = [(self.arr.copy(), [0], list(sorted_idx))]
        
        size = len(self.arr)
        
        
        #SORT!
        for i in range(size):
            swapped = False
            for j in range(size - i - 1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True
                #self.arr[j], self.arr[j+1] = min(self.arr[j], self.arr[j+1]), max(self.arr[j], self.arr[j+1])
                
                #bookkeeping
                frames.append((self.arr.copy(), [j+1], list(sorted_idx)))
            sorted_idx.append(size - i - 1)
            if swapped == False:
                break
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=50, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = BubbleSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())
    