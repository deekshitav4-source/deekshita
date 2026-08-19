class Solution(object):
    def constructProductMatrix(self, grid):
        mod = 12345
        n,m = len(grid),len(grid[0])
        p=[[0]*m for _ in range(n)]
        suffix = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                p[i][j] = suffix
                suffix = (suffix* grid [i][j])% mod

        prefix= 1
        for i in range(n):
            for j in range(m):
                p[i][j]=(p[i][j]* prefix)% mod
                prefix = (prefix * grid[i][j])% mod
        return p
        