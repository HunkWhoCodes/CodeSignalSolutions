# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
# Level 2 - Intro : Edge of the Ocean

# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product

import math

def solution(arr):
    N = len(arr)
    i, j = 0, 1
    max_prod = -math.inf
    
    while i < N and j < N and i < j:
        curr_prod = arr[i] * arr[j]
        max_prod = max(max_prod, curr_prod)
        i += 1
        j += 1
    
    return max_prod
