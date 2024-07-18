#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:01:58 2024

@author: vishweshpalani
"""

from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class CountingSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        frames = [(self.arr.copy(), [0], [])]
        sorted_idx = []
        
        size = len(self.arr)
        
        #SORT!
        
        max_val = -1 * float("inf")
        freq_arr = [0]
        
        for i in range(size):
            max_val = max(self.arr[i], max_val)
            
            #extend array length
            if len(freq_arr)-1 < self.arr[i]:
                diff = self.arr[i] - len(freq_arr) + 1
                freq_arr += diff * [0]
                
            freq_arr[self.arr[i]] += 1
            
        i = 0
        for n in range(len(freq_arr)):
            count = freq_arr[n]
            while count > 0:
                self.arr[i] = n
                
                #some bookkeeping
                sorted_idx.append(i)
                frames.append((self.arr.copy(), [i], list(sorted_idx)))
                
                i += 1
                count -= 1
            
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=200, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = CountingSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())