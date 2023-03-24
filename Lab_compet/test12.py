import math

n = int(input())
rock = []
for i in range(n):
    x, y = map(int, input().split())
    rock.append((x, y))


start = rock[0]
end = rock[1]
min_distance = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
for i in range(2, n):
    distance = math.sqrt((rock[i][0] - start[0])**2 + (rock[i][1] - start[1])**2)
    if distance < min_distance:
        min_distance = distance

print("{:.3f}".format(min_distance))
