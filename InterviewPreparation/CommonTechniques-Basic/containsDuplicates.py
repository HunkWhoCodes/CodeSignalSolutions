# https://app.codesignal.com/interview-practice/task/CfknJzPmdbstXhsoJ/description
# Difficulty: Easy

"""
Given an array of integers, write a function that determines whether the array contains any duplicates.
Your function should return true if any element appears at least twice in the array,
and it should return false if every element is distinct.
"""

def solution(a):
    seen = set() 
    
    for v in a:
        if v not in seen:
            seen.add(v)
        else:
            return True
    
    return False

