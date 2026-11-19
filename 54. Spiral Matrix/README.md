# 54. Spiral Matrix

### Difficulty: Medium

## Description
Given an m x n matrix, return all elements of the matrix in spiral order.

 
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


 
Constraints:


	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 10
	-100 <= matrix[i][j] <= 100

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19148000
- **Language**: python3

## Code
```python3
class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
```
