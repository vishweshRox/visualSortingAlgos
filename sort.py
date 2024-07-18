#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:22:51 2024

@author: vishweshpalani
"""

'''
Sorting Algorithms implemented:
    -> Quick Sort
    -> Merge Sort
    -> Counting Sort
    -> Heap Sort
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Sort:
    def __init__(self, arr):
        self.arr = np.array(arr)
        
    def getArr(self):
        return self.arr
    
    def _prepare(self):
        
        #creating the window
        figure, ax = plt.subplots()
        
        #creating the bars for the bar plot
        plot_bars = ax.bar(range(len(self.arr)), self.arr, align="edge")
        
        #setting the axes limits
        ax.set_xlim(0, len(self.arr))
        ax.set_ylim(0, 1.1 * max(self.arr))
        
        ax.xaxis.set_visible(False)
        #ax.yaxis.set_visible(False)
        
        return figure, ax, plot_bars
        
    '''
    SUBCLASS SORT IMPLEMENTATION

        def sort(self):
            
            #beginning
            fig, ax, bars = self._prepare()
            frames = [(self.arr.copy(), 0)]
            
            #SORT!
            # <- sorting algorithm implementation goes here
            # <- at the end of every iteration, add (a copy of the array to frames, and the index)
            
            #end
            self._process(fig, self._update(bars), frames)
            plt.show()
    '''

    def _update(self, bars):
        def update_frame(frame):
            cur, i, sorted_idx = frame
            for idx, (bar, val) in enumerate(list(zip(bars, cur))):
                if idx in i:
                    bar.set_color('r')
                elif idx in sorted_idx:
                    bar.set_color('#90EE90')
                else:
                    bar.set_color('#ADD8E6')
                bar.set_height(val)
            return bars
        return update_frame
            
    
    def _process(self, fig, update_bar, snaps):
        anim = animation.FuncAnimation(fig, update_bar, frames=snaps, interval=1, blit=False)
        return anim
    
    
        

        
    
            
        
