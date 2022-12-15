a = [5, 2, 4, 1, 7, 5]
a = sorted(a)
print(a)

su_a = sum(a)/len(a)
co = 0
for i in a:
    if i < su_a:
        co += su_a - i

print(int(co))
