# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
# Level 3 - Intro: Smooth Sailing

"""
Given an array of strings, return another array containing all of its longest strings.
"""

# Idea:
# In python len(string) is an O(1) operaation.
# So we can create a dict of lists and calculate the length of each string in an O(1) operation and then append the strings to correct lengths
# Then we can get the max of all keys and then return hast_table[max_key]


from collections import defaultdict

def solution(arr):
    mapping = defaultdict(list)
    
    for s in arr:
        length = len(s)
        mapping[length].append(s)
        
    max_len = max(mapping.keys())
    
    return mapping[max_len]
    
    

