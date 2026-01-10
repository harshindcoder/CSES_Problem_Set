import sys
sys.setrecursionlimit(10**7)

# directions: U, R, D, L
x = (-1, 0, 1, 0)
y = (0, 1, 0, -1)

def solve():
    s = sys.stdin.readline().strip()

    # grid with sentinels
    grid = [[True]*9 for _ in range(9)]
    for i in range(1, 8):
        for j in range(1, 8):
            grid[i][j] = False

    # encode moves
    p = [4]*48
    for i in range(48):
        c = s[i]
        if c == 'U':
            p[i] = 0
        elif c == 'R':
            p[i] = 1
        elif c == 'D':
            p[i] = 2
        elif c == 'L':
            p[i] = 3

    def dfs(idx, i, j):
        # grid split pruning (CSES editorial)
        if grid[i][j-1] and grid[i][j+1] and not grid[i-1][j] and not grid[i+1][j]:
            return 0
        if grid[i-1][j] and grid[i+1][j] and not grid[i][j-1] and not grid[i][j+1]:
            return 0

        # reached end
        if i == 7 and j == 1:
            return 1 if idx == 48 else 0

        if idx == 48:
            return 0

        grid[i][j] = True
        ans = 0

        # FORCED MOVE PRUNING
        cnt = 0
        ni = nj = 0

        if not grid[i-1][j]:
            cnt += 1; ni, nj = i-1, j
        if not grid[i+1][j]:
            cnt += 1; ni, nj = i+1, j
        if not grid[i][j-1]:
            cnt += 1; ni, nj = i, j-1
        if not grid[i][j+1]:
            cnt += 1; ni, nj = i, j+1

        if cnt == 0:
            grid[i][j] = False
            return 0

        d = p[idx]

        if d < 4:
            ni = i + x[d]
            nj = j + y[d]
            if not grid[ni][nj]:
                ans = dfs(idx + 1, ni, nj)
        else:
            if cnt == 1:
                ans = dfs(idx + 1, ni, nj)
            else:
                if not grid[i-1][j]:
                    ans += dfs(idx + 1, i-1, j)
                if not grid[i+1][j]:
                    ans += dfs(idx + 1, i+1, j)
                if not grid[i][j-1]:
                    ans += dfs(idx + 1, i, j-1)
                if not grid[i][j+1]:
                    ans += dfs(idx + 1, i, j+1)

        grid[i][j] = False
        return ans

    print(dfs(0, 1, 1))


if __name__ == "__main__":
    solve()
