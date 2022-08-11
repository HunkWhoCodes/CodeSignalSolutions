# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC
# Level 2 - Easy: Edge of the Ocean

"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size.
Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1.
He may need some additional statues to be able to accomplish that.
Help him figure out the minimum number of additional statues needed.
"""

# Idea:
# Just find the max and min of the array to find the ideal length of the statues
# Then subtract actual length from ideal length and return it

# Complexity - Time: O(n), Space: O(1)


def solution(statues):
    mn = min(statues)
    mx = max(statues)
    N = len(statues)
    
    ideal = mx - mn + 1
    actual = N
    
    return ideal - actual
