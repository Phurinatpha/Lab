a, b = map(int, input().split())
c = int(input())
distances = list(map(int, input().split()))

# Find the minimum time to catch the thief
min_time = float('inf')
for distance in distances:
    time = abs(b - a) // distance
    if abs(b - a) % distance != 0:
        time += 1
    if a + time * distance >= b:
        min_time = min(min_time, time)

if min_time == float('inf'):
    print("-1")
else:
    print(min_time)
