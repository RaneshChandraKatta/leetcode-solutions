# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         i, j, di, dj = 0, 0, 0, 1
#         arr = [[0] * n for _ in range(n)]

#         for m in range(n*n):
#             arr[i][j] = m + 1

#             if arr[(i+di)%n][(j+dj)%n]:
#                 di, dj = dj, -di
            
#             i+=di
#             j+=dj
        
#         return arr



class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n*n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix