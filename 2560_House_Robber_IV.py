class Solution:
    def can_steal(self, capability: int, nums: List[int], k: int):
        count = 0
        i = 0

        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1

        return count >= k

    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = left + (right - left) // 2 
            if self.can_steal(mid, nums, k):
                right = mid
            else:
                left = mid + 1

        return left                

# ! Explanation:
# * This function calculates the minimum capability required to steal from the houses such that at least k
# * houses can be robbed without setting off the alarm.
# * 1. Initialize the `left` and `right` pointers to the minimum and maximum values in the input list.
# * 2. Perform a binary search on the range of capabilities from `left` to `right`.
# * 3. Check if it is possible to steal from at least k houses with the current mid capability.
# * 4. If it is possible, update the right pointer to mid.
# * 5. Otherwise, update the left pointer to mid+1.
# * 6. Return the left pointer as the minimum capability required to steal from k houses.

# ? Time Complexity:
# * The time complexity of this approach is O(n log m), where n is the number of houses and m is the maximum value in the input list.
# * This is because we perform a binary search on the range of capabilities from the minimum to the maximum value in the input list.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space for variables.
# * The space complexity of this approach is O(1).

# ! Key Insight:
# * The problem can be solved using binary search by finding the minimum capability required to steal from k houses.
# * The `can_steal` function checks if it is possible to steal from at least k houses with a given capability.
# * The binary search is performed on the range of capabilities from the minimum to the maximum value in the input list.
# * The left pointer is updated to the mid+1 if it is not possible to steal from k houses with the current capability.
# * The right pointer is updated to the mid if it is possible to steal from k houses with the current capability.
# * The minimum capability required to steal from k houses is returned as the left pointer after the binary search.