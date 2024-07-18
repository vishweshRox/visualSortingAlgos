#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:43:51 2024

@author: vishweshpalani
"""
import math
from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class QuickSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        frames = [(self.arr.copy(), [0, len(self.arr) - 1], [])]
        
        size = len(self.arr)
        
        #SORT!
        def partition(low, high):
            
            #going to keep sorted within here    
            sorted_idx = []
            
            m = math.floor((high + low) / 2)
            
            if low >= high:
                return
            
            p = self.arr[m]
            i, j = low, high
            while i < j:
                if self.arr[i] > p and self.arr[j] <= p:
                    #swap
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                if self.arr[i] <= p:
                    if self.arr[i] == p: m = i
                    #bookkeeping
                    sorted_idx.append(i)
                    i += 1
                if self.arr[j] > p:
                    if self.arr[j] == p: m = j
                    #more bookkeeping
                    sorted_idx.append(j)
                    j -= 1
                
                #last bit of bookeeping
                frames.append((self.arr.copy(), [i, j], list(sorted_idx)))
                    
            if self.arr[i] <= p:
                idx = i
            else:
                idx = i-1
            
            #swap pivot
            self.arr[m], self.arr[idx] = self.arr[idx], self.arr[m]
            
            partition(low, idx-1)
            partition(idx+1, high)
        
        partition(0, size-1)
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=200, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = QuickSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())