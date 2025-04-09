class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1

        unique_nums = set(nums)
        n = len(unique_nums)  

        if k in unique_nums:
            return n - 1
            
        return n      
    

# ! Explanation:
# * This function calculates the minimum number of operations required to make all elements in the array equal to k.
# * 1. If k is greater than the minimum value in nums, return -1.
# * 2. Create a set of unique numbers from nums.
# * 3. Get the length of the set of unique numbers.
# * 4. If k is in the set of unique numbers, return n - 1.
# * 5. Otherwise, return n.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the length of the input list nums.
# * This is because we need to iterate through the list to create a set of unique numbers.

# ? Space Complexity:
# * The space complexity of this approach is O(n), where n is the length of the input list nums.
# * This is because we create a set from the list to store unique numbers.
# * The space complexity is O(n) because we are using a set to store unique numbers.    