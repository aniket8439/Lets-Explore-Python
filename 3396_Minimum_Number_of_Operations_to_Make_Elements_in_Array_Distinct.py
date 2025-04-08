class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            count += 1

        return count
    
# ! Explanation:
# * This function calculates the minimum number of operations required to make all elements in the array distinct.
# * 1. Initialize a variable count to 0.
# * 2. While the length of nums is greater than the length of the set of nums (which removes duplicates), do the following:
# *    - Remove the first three elements from nums.
# *    - Increment the count by 1.
# * 3. Return the count.


# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input list nums.
# * This is because we need to iterate through the list to check for duplicates and remove elements.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the length of the input list nums.
# * This is because we create a set from the list to check for duplicates.    