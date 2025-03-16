class Solution:
    def can_repair(self, time: str, ranks: List[int], cars: int):
        total_cars_repaired = 0

        for rank in ranks:
            cars_repaired = int((time / rank) ** 0.5)
            total_cars_repaired += cars_repaired

        return total_cars_repaired >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars

        while left < right:
            mid = left + (right - left) // 2
            if self.can_repair(mid, ranks, cars):
                right = mid
            else:
                left = mid + 1

        return left           
        

# ! Explanation:
# * This function calculates the minimum time required to repair cars such that at least k cars can be repaired.
# * 1. Initialize the `left` and `right` pointers to 1 and the maximum possible time required to repair all cars.
# * 2. Perform a binary search on the range of time from `left` to `right`.
# * 3. Check if it is possible to repair at least k cars with the current mid time.
# * 4. If it is possible, update the right pointer to mid.
# * 5. Otherwise, update the left pointer to mid+1.
# * 6. Return the left pointer as the minimum time required to repair k cars.

# ? Time Complexity:
# * The time complexity of this approach is O(n log m), where n is the number of ranks and m is the maximum value in the input list.
# * This is because we perform a binary search on the range of time from 1 to the maximum possible time required to repair all cars.

# ? Space Complexity:
# * The space complexity is O(1) because we use a constant amount of extra space for variables.
# * The space complexity of this approach is O(1).        