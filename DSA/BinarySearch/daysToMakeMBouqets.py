def minDays(bloomDay: list[int], m: int, k: int) -> int:
    requiredFlowers = m * k
    if len(bloomDay) < requiredFlowers:
        return -1

    def bloomedFlowers(day):
        total = 0
        combinationArray = [0] * len(bloomDay)
        i = 0
        for item in bloomDay:
            if item <= day:
                total += 1
                combinationArray[i] = 1
            i += 1

        return [total, combinationArray]

    left = 1
    right = max(bloomDay)
    result = right
    while left <= right:

        mid = left + (right - left) // 2
        tempArray = bloomedFlowers(mid)

        if tempArray[0] < requiredFlowers:
            left = mid + 1
        else:
            count = 0
            flowersBloomed = 0
            for item in tempArray[1]:
                if item == 1:
                    count += 1
                else:
                    flowersBloomed += count // k
                    count = 0
            flowersBloomed += count // k
            if flowersBloomed >= m:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
    return result

print(minDays([1,10,3,10,2],3,1))
print(minDays([7,7,7,7,12,7,7],2,3))