class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix)-1
        while up <= down:
            m = (up + down) // 2
            check = matrix[m][0]
            if check > target:
                down = m-1
            else:
                up = m+1
        
        row = down
        l, r = 0, len(matrix[0])-1
        while l <= r:
            m = (l + r) // 2
            check = matrix[row][m]
            if check > target:
                r = m-1
            elif check < target:
                l = m+1
            else:
                return True

        return False