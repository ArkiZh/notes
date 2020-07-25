"""
有一个正方形的岛屿，用二维方形矩阵表示。岛上有一个醉汉，每一步刻意上下左右四个方向之一移动一格。如果超出矩阵他就挂了。假设每一步方向的选择是随机的，请计算n步后他还活着的概率。
例如：
输入矩阵大小2*2，起点（0,0），n=1，输出0.5
输入矩阵大小3*3，起点（1,1），n=1，输出1
输入矩阵大小3*3，起点（0,0），n=2，输出0.375
"""

cached_probs = {}


def how_likely_alive(size, startx, starty, n):
    """
    Make sure the arguments match the following conditions.
    size: tuple of two positive int
    startx: non-negative int
    starty: non-negative int
    n: non-negative int
    """
    cached_val = cached_probs.get((startx, starty, n))
    if cached_val is not None:
        return cached_val
    x, y = size
    if startx < 0 or startx >= x or starty < 0 or starty >= y:
        return 0
    if n == 0:
        return 1
    prob = sum([how_likely_alive(size, startx + step[0], starty + step[1], n - 1)
                for step in [(-1, 0), (1, 0), (0, -1), (0, 1)]]) / 4
    cached_probs[(startx, starty, n)] = prob
    return prob


print(how_likely_alive((2, 2), 0, 0, 1))
print(how_likely_alive((3, 3), 1, 1, 1))
print(how_likely_alive((3, 3), 0, 0, 2))
print(how_likely_alive((10, 10), 3, 5, 300))
print(how_likely_alive((1, 2), 0, 1, 100))

from collections import deque


def how_likely_alive1(size, startx, starty, n):
    """
    Make sure the arguments match the following conditions.
    size: tuple of two positive int
    startx: non-negative int
    starty: non-negative int
    n: non-negative int
    """
    x, y = size
    if startx >= x or starty >= y:
        return 0
    positions = deque([(0, startx, starty)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    live_prob = 1
    while positions:
        cur = positions.popleft()
        if (cur[1] - x) * (cur[1] + 1) * (cur[2] - y) * (cur[2] + 1) == 0:
            live_prob -= (0.25) ** cur[0]
            continue
        if cur[0] < n:
            for direction in directions:
                positions.append((cur[0] + 1, cur[1] + direction[0], cur[2] + direction[1]))
    return live_prob
