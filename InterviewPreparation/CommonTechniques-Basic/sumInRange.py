# https://app.codesignal.com/interview-practice/task/4MoqQLaw22nrzXbgs/description
# Difficulty: Easy

# Problem Statement:
"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based).
Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query,
then add all of the sums for all the queries together.
Return that number modulo 109 + 7.
"""

# Idea:
# Use prefix sum to calculate the sum of arrays
# Then go through quries one by one and maintain a total variable
# If the start == 0 then the prefix sum array can be used as it is so then just add prefix[end]
# Else do prefix[end] - prefix[start - 1] and add it to total
# finally return total % (10 *8 9 + 7) as asked in the problem statement



def solution(nums, queries):
    total = 0
    N = len(nums)
    
    prefix = [0]*N
    prefix[0] = nums[0]
    
    for i in range(1, N):
        prefix[i] = prefix[i-1] + nums[i]
        
    for start, end in queries:
        # total += sum(nums[start:end+1])   # TLE with this
        if  start == 0:
            total += prefix[end]
        else:
            total += prefix[end] - prefix[start-1]
    
    return total % (10 ** 9 + 7)
