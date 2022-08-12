# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q


"""
Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers,
return the number for which the second occurrence has a smaller index than the second occurrence of the other number does.
If there are no such elements, return -1.
"""

# Idea
# Populate a defaultdict of list first then iterate through it
# Maintain a min_ind and an ans variable.
# If the value in defaultdict is more than 1 means that the number is repeated, then compare min_ind with its second index i.e. v[1]
# When you find min, update the ans and return the ans


from collections import defaultdict
import math


def solution(a):
        
    freq = defaultdict(list)
    
    for i, v in enumerate(a):
        freq[v].append(i)
    
    min_ind = math.inf
    ans = -1
    for k,v in freq.items():
        if len(v) > 1:
            if min_ind > v[1]:
                min_ind = v[1]     # We use v[1], because we only second occurrence, not last so not v[-1]
                ans = k
    
    return ans
            
        
    

