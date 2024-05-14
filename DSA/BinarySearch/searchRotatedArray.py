def search(nums:list, target: int) -> int:
    """
        Searches for the target integer in the rotated sorted array 'nums'.

        Args:
        - nums: A list of integers representing the rotated sorted array.
        - target: An integer to be searched in the array.

        Returns:
        - int: The index of the target if it is found, otherwise -1.

        Time complexity:
        O(log n) - The binary search is performed with logarithmic time complexity.
        """

    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (right + left) // 2

        # if middle value is the target then return the mid index
        if nums[mid] == target:
            return mid

        # to check if the mid is in left sorted portion
        if nums[mid] >= nums[left]:

            # if target > mid then move to right side
            if target > nums[mid]:
                left = mid + 1

            else:
                # check if target is less than left then move left to mid + 1
                # else right to mid - 1
                if target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        # now we are in right sorted portion
        else:

            # target is less than mid move right to mid - 1
            if target < nums[mid]:
                right = mid - 1

            else:
                # check if target is greater than the right then move right to mid - 1
                if target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

    # if number is not found then return -1
    return - 1

print(search([3,4,5,6,1,2],2))