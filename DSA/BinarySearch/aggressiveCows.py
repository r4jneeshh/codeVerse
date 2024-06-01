def minimumDistance(array, cows):
    array.sort()

    def solve(distance:int, count: int)->bool:
        possible = True
        cows = 1
        index = 0
        for i in range(1,len(array)):
            if array[i]-array[index] >= distance:
                cows += 1
                index = i
        return cows >= count

    left = 1
    right = max(array)-min(array)
    ans = 0

    while left <= right:
        mid = left + (right-left)//2

        if solve(mid, cows):
            ans = mid
            left = mid+1
        else:
            right = mid-1

    return ans

array = [1,2,3,8,4,9]
cows = 3
print(minimumDistance(array, cows))
print(minimumDistance([10, 1, 2, 7, 5], 2))
print(minimumDistance([4, 2, 1, 3, 6], 2))
print(minimumDistance([3, 6, 8, 1, 5], 4))
print(minimumDistance([10, 20, 30, 40, 50], 5))