def convert_base(n, k):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""
    while n > 0:
        remainder = n % k
        result = alphabet[remainder] + result
        n //= k
    return result if result else "0"

# Example usage:
n = int(input())
k = int(input())
result = convert_base(n, k)
print(result)