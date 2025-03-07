# Brute Force

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True    

        primes = []
        for num in range(max(2, left), right + 1):
            if is_prime(num):
                primes.append(num)

        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        result = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]] 

        return result                                           
# ! Explanation:
# * This function finds the closest pair of prime numbers within a given range [left, right].
# * 1. Define a helper function `is_prime` to check if a number is prime.
# * 2. Initialize an empty list `primes` to store all prime numbers in the range [left, right].
# * 3. Iterate through the range [max(2, left), right + 1] and check if each number is prime using the `is_prime` function.
# * 4. Append prime numbers to the `primes` list.
# * 5. If there are less than 2 prime numbers in the range, return [-1, -1].
# * 6. Initialize variables `min_gap` and `result` to store the minimum gap and the closest pair of prime numbers, respectively.
# * 7. Iterate through the list of prime numbers and calculate the gap between adjacent prime numbers.
# * 8. Update `min_gap` and `result` if the current gap is smaller than the previous minimum gap.
# * 9. Return the closest pair of prime numbers as a list [result[0], result[1]].
#
# ? Time Complexity:
# * The time complexity of this approach is O((right - left) * sqrt(right)), where right is the upper bound of the range.       
# * This is because we iterate through the range [left, right] and check each number for primality using the `is_prime` function, which has a time complexity of O(sqrt(n)).
#
# ? Space Complexity:   
# * The space complexity is O(right - left) because we store the prime numbers in the range [left, right] in the `primes` list.
# * In the worst case, all numbers in the range [left, right] are prime, leading to O(right - left) space complexity.
# * The space complexity of the `result` and `min_gap` variables is O(1) since they store only two integers.
# * Overall, the space complexity is dominated by the `primes` list.
# * The space complexity of this approach is O(right - left).


# Approach 2: Sieve of Eratosthenes
# Optimized

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]
        
        return result
    
# ! Explanation:
# * This function finds the closest pair of prime numbers within a given range [left, right] using the Sieve of Eratosthenes algorithm.
# * 1. Initialize a sieve list `sieve` of size right + 1 to mark prime numbers.
# * 2. Set the first two elements of the sieve list to False since 0 and 1 are not prime numbers.
# * 3. Iterate through the range [2, sqrt(right)] and mark multiples of each prime number as non-prime in the sieve list.
# * 4. Generate a list of prime numbers `primes` in the range [left, right] based on the sieve list.
# * 5. If there are less than 2 prime numbers in the range, return [-1, -1].
# * 6. Initialize variables `min_gap` and `result` to store the minimum gap and the closest pair of prime numbers, respectively.
# * 7. Iterate through the list of prime numbers and calculate the gap between adjacent prime numbers.
# * 8. Update `min_gap` and `result` if the current gap is smaller than the previous minimum gap.
# * 9. Return the closest pair of prime numbers as a list [result[0], result[1]].
#
# ? Time Complexity:
# * The time complexity of this approach is O(right * log(log(right))), where right is the upper bound of the range.
# * This is because we use the Sieve of Eratosthenes algorithm to generate prime numbers up to right, which has a time complexity of O(n log(log(n))).
# * We then iterate through the list of prime numbers to find the closest pair, which takes O(right) time.
#
# ? Space Complexity:
# * The space complexity is O(right) because we store the sieve list of size right + 1 to mark prime numbers.
# * The space complexity of the `primes` list is also O(right) in the worst case.
# * The space complexity of the `result` and `min_gap` variables is O(1) since they store only two integers.
# * Overall, the space complexity is dominated by the sieve list and the list of prime numbers.
# * The space complexity of this approach is O(right).