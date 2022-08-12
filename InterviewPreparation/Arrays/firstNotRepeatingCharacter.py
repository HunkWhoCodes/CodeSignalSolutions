# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC/

"""
Given a string s consisting of small English letters,
find and return the first instance of a non-repeating character in it.
If there is no such character, return '_'.
"""

# Idea:
# Create a defaultdict and update it with the values
# Iterate through it, if there's a value which is equal to 1 then return its key
# Else return "_"




from collections import defaultdict 


def solution(s):
    freq = defaultdict()
    
    for v in s:
        if v not in freq:
            freq[v] = 1
        else:
            freq[v] += 1
    
    
    for k, v in freq.items():
        if v == 1:
            return k
    
    return "_"

