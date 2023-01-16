from itertools import permutations

n = int(input())

found = False
for a, b, c, d, e in permutations(range(10), 5):
    f, g, h, i, j = permutations(range(10), 5)
    if (a*10000 + b*1000 + c*100 + d*10 + e) * (j + i*10 + h*100 + g*1000 + f*10000) == n*10000000:
        print("{}{}{}{}{} / {}{}{}{}{} = {}".format(a, b, c, d, e, f, g, h, i, j, n))
        found = True

if not found:
    print("There are no solutions for {}.".format(n))
