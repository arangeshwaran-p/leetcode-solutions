# 204. Count Primes

### Difficulty: Medium

## Description
Given an integer n, return the number of prime numbers that are strictly less than n.

 
Example 1:


Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Example 2:


Input: n = 0
Output: 0


Example 3:


Input: n = 1
Output: 0


 
Constraints:


	0 <= n <= 5 * 106

## Submission Details
- **Status**: Accepted
- **Runtime**: 2192
- **Memory**: 65624000
- **Language**: python3

## Code
```python3
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        count = 0

        for i in range(2, n):
            if prime[i]:
                count += 1

                for j in range(i * i, n, i):
                    prime[j] = False

        return count
```
