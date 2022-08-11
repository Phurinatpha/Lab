def longest_digit_run(n,m=1,c=1):
    n = str(n)
    if len(n) == 0:
        return m
    elif n[0] == n[1:2]:
        c +=1
        m = max(m,c)
        return longest_digit_run(n[1:],m,c)
    else:
        return longest_digit_run(n[1:],m,c=1)

print(longest_digit_run(12345))
        