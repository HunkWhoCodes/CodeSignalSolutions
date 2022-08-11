# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
# Level - (Intro) The Journey Begins

# Given a year, find the cntruy the year belongs to.


def solution(year):
    if year <= 100:
        return 1
    
    century = year // 100
    
    if year % 100 == 0:
        return century 
    else:
        return century + 1
    

