def numberOfDigit(N):
 
    digit = 0
 
    # Calculate the count
    # of digits in N
    while (N > 0):
 
        # Update digit
        digit += 1
 
        # Update N
        N //= 10
    return digit
 
# Function to rotate the digits of N by K
def rotateNumberByK(N, K):
 
    # Stores count of digits in N
    X = numberOfDigit(N)
 
    # Update K so that only need to
    # handle left rotation
    K = ((K % X) + X) % X
 
    # Stores first K digits of N
    left_no = N // pow(10, X - K)
 
    # Remove first K digits of N
    N = N % pow(10, X - K)
 
    # Stores count of digits in left_no
    left_digit = numberOfDigit(left_no)
 
    # Append left_no to the right of
    # digits of N
    N = N * pow(10, left_digit) + left_no
    print(N)
 
# Driver Code
if __name__ == '__main__':
    N, K = 12345, 7
 
    # Function Call
    rotateNumberByK(N, K)
 