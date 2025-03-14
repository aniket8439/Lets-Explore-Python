class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(pile // mid for pile in candies) # using interpolation

            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans        


# ! Explanation:
# * This function calculates the maximum number of candies that can be allocated to k children such that each child receives at least one candy.
# * 1. If the sum of candies is less than k, return 0 as it is not possible to allocate candies to k children.
# * 2. Initialize variables `left` and `right` to store the minimum and maximum number of candies in the input list.
# * 3. Initialize the answer variable `ans` to 0.
# * 4. Perform a binary search on the range of candies from `left` to `right`.
# * 5. Calculate the number of candies that can be allocated to k children with the current mid value.
# * 6. If the count is greater than or equal to k, update the answer and move the left pointer to mid+1.
# * 7. Otherwise, move the right pointer to mid-1.
# * 8. Return the answer as the maximum number of candies that can be allocated to k children.

# ? Time Complexity:
# * The time complexity of this approach is O(n log m), where n is the number of candies and m is the maximum number of candies in the input list.
# * This is because we perform a binary search on the range of candies from 1 to the maximum number of candies.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space for variables.
# * The space complexity of this approach is O(1).