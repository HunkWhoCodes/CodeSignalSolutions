# https://app.codesignal.com/interview-practice/task/Hm98RnqK9Be575yoj/description
# Difficulty: Easy? or Medium

# This question is better than the basic two sum

"""
You have two integer arrays, a and b, and an integer target value v.
Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v.
Return true if such a pair exists, otherwise return false.
"""

# Idea:
# Walk through the first array and store its difference from target in a hash set (better) or hash map
# Then walk through the second array, if the current element is in hash set/table then return true
# Otherwise finally by default return False

# With a hash set:

def solution(a, b, v):
    if len(a) == 0 or len(b) == 0:
        return False
    
    seen = set()
    
    for n in a:
        seen.add(v-n)
        
    for j, m in enumerate(b):
        if m in seen:
            return True
    
    return False
        

 # With a hash map:

def solution(a, b, v):
    if len(a) == 0 or len(b) == 0:
        return False
    
    mapping = {}
    
    for i, n in enumerate(a):
        mapping[v-n] = i
        
    for j, m in enumerate(b):
        if m in mapping:
            return True
    
    return False
        
