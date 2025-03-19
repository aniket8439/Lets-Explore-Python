class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1

        return -1 if 0 in nums else ans                


# ! Explanation:
# * This function calculates the minimum number of operations required to make all elements of the input list equal to 1.
# * 1. Initialize the answer variable to 0.
# * 2. Iterate through the input list until the second-to-last element.
# * 3. If the current element is 0, perform the following operations:
#     * Set the current element to 1.
#     * Toggle the next two elements using the XOR operation.
#     * Increment the answer by 1.
# * 4. Return -1 if 0 is present in the list; otherwise, return the answer.

# ? Time Complexity:
# * The time complexity of this approach is O(n), where n is the number of elements in the input list.
# * This is because we iterate through the input list once.

# ? Space Complexity:
# * The space complexity of this approach is O(1) because we use a constant amount of extra space.