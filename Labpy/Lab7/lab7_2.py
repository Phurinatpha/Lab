
def patterned_message(message, pattern,i=0,j=0):
    message = message.replace(" ","")
    if i == len(pattern)-1:
        return ""
    elif pattern[i] == "*":
        print(message[j],end="")
        if j == len(message)-1:
            return patterned_message(message,pattern,i+1,0)        
        else:
            return patterned_message(message,pattern,i+1,j+1)
    elif pattern[i] == "\n":
        print("\n",end="")
        return patterned_message(message,pattern,i+1,j)
    elif pattern[i] == " ":
        print(" ",end="")
        return patterned_message(message,pattern,i+1,j)

def main():
    patterned_message("Three Diamonds!",
    '''
   *     *     *
  ***   ***   ***
 ***** ***** *****
  ***   ***   ***
   *     *     *
''')


if __name__ == '__main__':
    main()

