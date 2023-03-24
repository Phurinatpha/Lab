n = int(input())
area = [[False] * 50 for _ in range(50)]
for i in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            area[x][y] = True

count = 0
for x in range(50):
    for y in range(50):
        if not area[x][y]:
            count += 1

print(2500 - count)
