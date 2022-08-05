def main():
    print(uniform("HaPpY"))

def uniform(line,up=0,low=0,i=0):
    if i == len(line):
        if up > low:
            return line.upper()
        elif low > up:
            return line.lower()
        elif up == low:
            if line[0].isupper():
                return line.upper()
            else:
                return line.lower()
    else:
        if line[i].isupper():
            up += 1
        elif line[i].islower():
            low +=1
        return uniform(line,up,low,i+1)



def checkup(line,up=0,i=0):
    if i == len(line):
        return up
    else:
        if line[i].isupper():
            up += 1
        return checkup(line,up,i+1)

def checklow(line,low=0,i=0):
    if i == len(line):
        return low
    else:
        if line[i].islower():
            low += 1
        return checklow(line,low,i+1)

if __name__ == '__main__':
    main()
