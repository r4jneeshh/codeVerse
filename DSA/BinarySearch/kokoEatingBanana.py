from math import ceil
def minimumRate(piles, hour):
    def totalTimeToEat(rate):
        timeTaken = 0
        for item in piles:
            timeTaken += ceil(item/rate)
        return timeTaken

    left = 1
    right = max(piles)

    while left <= right:
        mid = left+(right-left)//2
        answer = totalTimeToEat(mid)
        if answer <= hour:
            finalAnswer = mid
            right = mid-1
        else:
            left = mid+1
    return finalAnswer

print(minimumRate([3,6,7,11],8))

# first create a function which takes an int rate and calculate total time it'll take to eat the bananas at that rate.
#Then create another function which will use binary search algo to divide the possible answer array into halves.