class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        diff_arr = [0] * (n+1)
        curr_sum = j = 0

        for i, num in enumerate(nums):
            curr_sum += diff_arr[i]

            while j < m and curr_sum < num:
                l, r, val = queries[j]
                j += 1

                if i < l:
                    diff_arr[l] += val
                elif i <= r:
                    curr_sum += val

                diff_arr[r+1] -= val

            if curr_sum < num:
                return -1

        return j                        
    
# ! Explanation:    
# * This function calculates the minimum number of operations required to transform the input list into a zero array.
# * 1. Initialize variables `n` and `m` to store the lengths of the input list and queries, respectively.
# * 2. Create a difference array `diff_arr` of size `n+1` to store the differences between adjacent elements.
# * 3. Initialize variables `curr_sum` and `j` to store the current sum and the index of the query.
# * 4. Iterate through the elements of the input list using the `i` pointer.
# * 5. Update the current sum by adding the difference at index `i` in the difference array.
# * 6. While the current sum is less than the current element, process the queries.
# * 7. For each query, update the difference array based on the query values.
# * 8. If the current sum is still less than the current element, return -1.
# * 9. Return the index `j` as the minimum number of operations required.

# ? Time Complexity:
# * The time complexity of this approach is O(n + m), where n is the length of the input list and m is the number of queries.
# * This is because we iterate through the input list and process the queries separately.

# ? Space Complexity:
# * The space complexity is O(n) because we use a difference array of size n+1 to store the differences between elements.
# * The space complexity of this approach is O(n).    