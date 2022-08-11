# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ/solutions
# Level: Intro - The Journey Begins

# Check if a number is a palindrome and return T/F

def solution(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False

