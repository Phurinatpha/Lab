def rotate_string(s, n):
    """
    Rotate string s based on the given number n.
    If n is even, rotate the characters to the right.
    If n is odd, rotate the characters to the left.
    """
    if n % 2 == 0:
        return s[-n:] + s[:-n]
    else:
        return s[n:] + s[:n]

# Read input
n = int(input())
prev_day = 0  # Start with day 1
for i in range(n):
    d, m = input().split()
    d = int(d)
    
    # Calculate the rotation amount based on the previous day
    if d % 2 == 0:
        rot_amount = d - prev_day
    else:
        rot_amount = prev_day - d
    
    # Rotate the message and update the previous day
    rotated = rotate_string(m, rot_amount)
    prev_day = d
    
    print(rotated)
