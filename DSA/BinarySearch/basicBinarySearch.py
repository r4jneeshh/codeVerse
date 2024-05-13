#Iterative Binary Search
def binarySearch(array, key):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = left + (right-left)//2

        if array[mid] == key:
            return mid
        elif array[mid] > key:
            right = mid-1
        else:
            left = mid+1
    return "Item not in the list"

print(binarySearch([1,4,6,88,200,377,3377],111))
print(binarySearch([1,2],2))