import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = (len(data) - 1) // 2

    list1 = [None] * n
    list2 = [None] * n

    idx = 0
    for i in range(1, len(data), 2):
        x = data[i]
        y = data[i + 1]
        list1[idx] = (y, -x, idx)
        list2[idx] = (x, -y, idx)
        idx += 1

    list1.sort()
    list2.sort()

    res1 = [0] * n
    res2 = [0] * n

    pos = 0
    for y, nx, i in list1:
        if pos >= -nx:
            res1[i] = 1
        if -nx > pos:
            pos = -nx

    pos = 0
    for x, ny, i in list2:
        if pos >= -ny:
            res2[i] = 1
        if -ny > pos:
            pos = -ny

    out = sys.stdout.write
    out(" ".join(map(str, res1)) + "\n")
    out(" ".join(map(str, res2)))

if __name__ == "__main__":
    solve()
