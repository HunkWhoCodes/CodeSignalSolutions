# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
# Level 3: Intro - Smooth Sailing

"""
Given two strings, find the number of common characters between them.
"""

# Idea:
# Create two frequency tables of the 2 strings
# Walk through k, v of one and if the key is also in another
# Then increment count to be the min val of both dictionary's value
# Return this count

# Can be done with lesser lines of code with Counters from Collections

def solution(s1, s2):
    freq1 = {}
    freq2 = {}
    
    for c in s1:
        if c not in freq1:
            freq1[c] = 1
        else:
            freq1[c] += 1
    
    for c in s2:
        if c not in freq2:
            freq2[c] = 1
        else:
            freq2[c] += 1
    
    count = 0
    for key,val in freq1.items():
        if key in freq2:
            count += min(val, freq2[key])
         
    return count
