def count_paths(matrix, visited, row, col):
    if matrix[row][col] == 2:  # found the target room
        return 1

    count = 0
    visited[row][col] = True  # mark current room as visited

    # explore all four directions
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        next_row, next_col = row + dx, col + dy
        if (0 <= next_row < len(matrix) and
            0 <= next_col < len(matrix[0]) and
            not visited[next_row][next_col] and
            matrix[next_row][next_col] != -1):
            count += count_paths(matrix, visited, next_row, next_col)

    visited[row][col] = False  # unmark current room as visited
    return count


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# find the entrance
entrance = None
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            entrance = (i, j)
            break
    if entrance:
        break

print(count_paths(matrix, visited, entrance[0], entrance[1]))
