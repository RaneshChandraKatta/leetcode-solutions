class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j, di, dj = 0, 0, 0, 1
        arr = [[0] * n for _ in range(n)]

        for m in range(n*n):
            arr[i][j] = m + 1

            if arr[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            
            i+=di
            j+=dj
        
        return arr