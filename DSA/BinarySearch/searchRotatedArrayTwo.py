def searchTwo(array, key):
    """
        Searches for a key in a rotated sorted array using binary search.

        Args:
        - array: A list of integers representing the rotated sorted array.
        - key: An integer to be searched in the array.

        Returns:
        - bool: True if the key is found in the array, otherwise False.

        Algorithm:
        The function implements binary search with modifications to handle rotated arrays.
        - Initialize left and right pointers to the start and end of the array.
        - While left <= right:
            - Calculate the mid index.
            - If array[mid] equals key, return True.
            - If array[left], array[mid], and array[right] are equal, move left and right pointers towards the center.
            - If the left half of the array is sorted:
                - If the key is within the range of the left half, search left.
                - Otherwise, search right.
            - If the right half of the array is sorted:
                - If the key is within the range of the right half, search right.
                - Otherwise, search left.

        Time Complexity:
        O(log n) - Binary search is performed with logarithmic time complexity.
        """

    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == key:
            return True

        if array[left] == array[mid] and array[mid] == array[right]:
            left += 1
            right -= 1
            continue

        if array[left] <= array[mid]:
            if array[left] <= key and key <= array[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if array[mid] <= key and key <= array[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False

print(searchTwo([2,5,6,0,0,1,2],0))


