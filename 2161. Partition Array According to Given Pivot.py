# Brute force:

# ! Time Complexity:
# ? The time complexity of this brute force approach is O(n), where n is the number of elements in the input list `nums`.
# ? This is because we iterate through the list once to partition the elements into three separate lists.

# ! Space Complexity:
# ? The space complexity is also O(n) because we are using three additional lists (`lesser_list`, `pivot_list`, and `greater_list`)
# ? to store the elements, which in the worst case can be as large as the input list `nums`.

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser_list = []
        pivot_list = []
        greater_list = []

        for num in nums:
            if num < pivot:
                lesser_list.append(num)
            elif num == pivot:
                pivot_list.append(num)
            else:
                greater_list.append(num)

        return lesser_list + pivot_list + greater_list 
    
# 24 ms

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser_list = [num for num in nums if num < pivot]
        greater_list = [num for num in nums if num > pivot]
        count_of_pivot = len(nums) - len(lesser_list) - len(greater_list)
        pivot_list = [pivot] * count_of_pivot
        return lesser_list + pivot_list + greater_list    
    
    
# Two Pointers:

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result_list = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                result_list[left] = nums[i]
                left += 1

            if nums[j] > pivot:
                result_list[right] = nums[j]
                right -= 1

        while left <= right:
            result_list[left] = pivot
            left += 1

        return result_list                               
            
# ! Explanation:
# ? This approach uses two pointers to partition the array into three sections: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
# ? 1. Initialize an empty result list of the same length as the input list.
# ? 2. Use two pointers, `left` starting from the beginning and `right` starting from the end of the list.
# ? 3. Iterate through the list using two pointers:
# *  - If the current element from the left pointer is less than the pivot, place it in the result list at the `left` index and increment the `left` pointer.
# *  - If the current element from the right pointer is greater than the pivot, place it in the result list at the `right` index and decrement the `right` pointer.
# ? 4. After the iteration, fill the remaining positions between `left` and `right` with the pivot value.
# ? 5. Return the result list.

# ! Time Complexity:
# ? The time complexity of this approach is O(n), where n is the number of elements in the input list `nums`.
# ? This is because we iterate through the list once using two pointers to partition the elements into three separate sections.

# ! Space Complexity:
# ? The space complexity is O(n) because we are using an additional list (`result_list`) to store the elements, which is the same size as the input list `nums`.
 