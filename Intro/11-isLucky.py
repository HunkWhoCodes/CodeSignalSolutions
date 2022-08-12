# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ
# Difficulty: Level 3 - Intro : Smooth Sailing

"""
Ticket numbers usually consist of an even number of digits.
`55A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

# Idea - 
# Find the length of the number.
# Calculate the sum of second half, calculate sum first half
# Compare sum1 and sum2 and return result if same or not


def solution(n):
    length = get_length(n)
    sum1 = sum2 = 0
    first_half = second_half = length // 2
    
    while second_half:
        sum2 += n % 10
        n = n // 10
        second_half -= 1
    
    while first_half:
        sum1 += n % 10
        n = n // 10
        first_half -= 1
    
    return sum1 == sum2
        
        
def get_length(n):
    length = 0
    while n:
        n = n // 10
        length += 1
    
    return length

