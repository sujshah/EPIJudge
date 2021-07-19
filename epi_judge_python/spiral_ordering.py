from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(A: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    return _matrix_in_spiral_order_reduction(A, len(A), 0)


def _matrix_in_spiral_order_reduction(A: List[List[int]], n: int, x: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [A[x][x]]
    if n == 2:
        return [A[x][x], A[x][x + 1], A[x + 1][x + 1], A[x + 1][x]]
    top_order = A[x][x:x + n - 1]
    bottom_order = list(reversed(A[x + n - 1][x + 1:x + n]))
    right_column = [A[y][x + n - 1] for y in range(x, x + n - 1)]
    left_column = list(reversed([A[y][x] for y in range(x + 1, x + n)]))
    outer_layer = top_order + right_column + bottom_order + left_column
    return outer_layer + _matrix_in_spiral_order_reduction(A, n - 2, x + 1)


def matrix_in_spiral_order_improved_solution(A: List[List[int]]) -> List[int]:
    result = []
    n = len(A)
    if not len(A): return result
    translation = [(0,1), (1,0), (0,-1), (-1,0)]
    direction = x = y = 0
    while len(result) < n * n:
        print(x, y)
        result.append(A[x][y])
        A[x][y] = 0
        next_x, next_y = x + translation[direction][0], y + translation[direction][1]
        if not (next_x in range(len(A)) and next_y in range(len(A)) and A[next_x][next_y]):
            direction = (direction + 1) % 4
            next_x, next_y = x + translation[direction][0], y + translation[direction][1]
        x,y = next_x, next_y
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order_improved_solution))
