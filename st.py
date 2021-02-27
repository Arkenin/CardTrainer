import math


def mean(nums):
    N = len(nums)
    return sum(nums)/N

def variance(nums):
    mn = mean(nums)
    N = len(nums)
    return sum((x - mn)**2 for x in nums)/N
    
    
def st_dev(nums):
    var = variance(nums)
    return math.sqrt(var)
