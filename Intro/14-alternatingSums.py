# https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9/
# Level 4 - Intro: Exploring the Waters

"""
You are given an array of positive integers - the weights of the people.
Return an array of two integers, where the first element is the total weight of team 1,
and the second element is the total weight of team 2 after the division is complete.
"""


def solution(a):
    weight1 = weight2 = 0
    
    for i in range(len(a)):
        if i % 2 == 0:
            weight1 += a[i]
        else:
            weight2 += a[i]
    
    return [weight1, weight2]

