#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:17:33 2024

@author: vishweshpalani
"""

from sort import Sort
import numpy as np
import matplotlib.pyplot as plt

class Heap:
    def __init__(self, arr):
        '''
        *THIS IS A MIN-HEAP*
    
        NOTE: This form of indexing can be used to construct any kind of complete binary tree
        -> Left Child: 2 * i + 1 (ALWAYS ODD)
        -> Right Child: 2 * i + 2 (ALWAYS EVEN)
        <- Parent: (i - 1) // 2
        '''
        self.arr = list(arr) #NOT A NUMPY ARRAY
        self._heapify()
    
    def getArr(self):
        return self.arr
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def _heapify(self):
        #Called only once during initialization
        temp = []
        
        while not self.isEmpty():
            val = self.pop()
            temp.append(val)
        
        for val in temp:
            self.add(val)
            
    def peek(self):
        if self.isEmpty():
            raise ValueError("Empty Heap")
        else:
            return self.arr[0]
    
    def pop(self):
        if self.isEmpty():
            raise ValueError("Empty Heap")
        else:
            
            if len(self.arr) == 1:
                return self.arr.pop()
            
            head = self.arr[0]
            tail = self.arr[len(self.arr) - 1]
            self.arr.pop(len(self.arr) - 1)
            self.arr[0] = tail
            
            i = 0
            size = len(self.arr)
        
            while i < size:
                
                l = 2 * i + 1
                r = 2 * i + 2
                
                indexToSwap = i
                
                if l < size and self.arr[i] > self.arr[l]:
                    indexToSwap = l
                
                #l must be defined if r is defined
                if r < size and self.arr[i] > self.arr[r]:
                    if self.arr[r] < self.arr[l]:     
                        indexToSwap = r
                    
                if indexToSwap == i:
                    break
                    #nothing left
                else:
                    #swaps elements
                    self.arr[i], self.arr[indexToSwap] = self.arr[indexToSwap], self.arr[i]
                    i = indexToSwap
                
            return head
    
    def add(self, e):
        
        self.arr.append(e)
        
        i = len(self.arr) - 1
        
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[parent] > self.arr[i]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                return
    
class HeapSort(Sort):
    def sort(self):
        #beginning
        fig, ax, bars = self._prepare()
        frames = [(self.arr.copy(), [0], [])]
        sorted_idx = []
        
        size = len(self.arr)
        
        #SORT!
        
        h = Heap(self.arr)
        
        for i in range(size):
            self.arr[i] = h.pop()
            sorted_idx.append(i)
            frames.append((self.arr.copy(), [i], list(sorted_idx)))
                
        #end
        anim = self._process(fig, self._update(bars), frames)
        #it doesn't work if we don't store the anim object in a variable 
        plt.show()
        
if __name__ == '__main__':
    arr = np.random.choice(1000, size=200, replace=False)
    
    print('UNSORTED ARRAY:')
    print(arr)
    
    sort_arr = HeapSort(arr)
    sort_arr.sort()
    
    print('SORTED ARRAY:')
    print(sort_arr.getArr())