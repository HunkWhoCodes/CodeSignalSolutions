# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
# Level 2 - Intro: Edge of the Ocean

"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing.
"""

def solution(sequence):
    if len(sequence) == 1:
        return True
    
    count = 0 
    N = len(sequence)    
    i = 1
    
    while i < N:
        if sequence[i - 1] >= sequence[i]:
            count += 1
            if (i > 1 and sequence[i - 2] >= sequence[i]):  
                sequence[i] = sequence[i-1]
        
        if count > 2: return False
        i += 1
    
    return count < 2
   
        
        
            
    
