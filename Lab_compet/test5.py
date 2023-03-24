# define the mapping between digits and characters
mapping = {
    '1': 'ijIJ',
    '2': 'abcABC',
    '3': 'defDEF',
    '4': 'ghGH',
    '5': 'klKL',
    '6': 'mnMN',
    '7': 'prsPRS',
    '8': 'tuvTUV',
    '9': 'wxyWXY',
    '0': 'oqzOQZ'
}

# read input number and number of words
number = input().strip()
n = int(input().strip())

# loop through each word and check if it matches the number
words = []
for i in range(n):
    word = input().strip()
    match = True
    for j in range(len(number)):
        if number[j] not in mapping or word[j].lower() not in mapping[number[j]]:
            match = False
            break
    if match:
        words.append(word)

# sort the words and print them
words.sort()
if len(words) ==0 :
    print("No")
else:
    for word in words:
        print(word)
