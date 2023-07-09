year = int(input())
y_zo = abs((year-1996)%12)
zodiac = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

y_ele = abs((year+6)%10//2)
element = ["Wood", "Fire", "Earth", "Metal", "Water"]



print(zodiac[y_zo])
print(element[y_ele])

