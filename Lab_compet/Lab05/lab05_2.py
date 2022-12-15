str = input()
str = str.split(" ")

if (len(str) >= 2):
    for i in range(len(str)):
        str[i] = str[i][::-1]

else:
    str = reversed(str)


str = " ".join(str)
print(str)