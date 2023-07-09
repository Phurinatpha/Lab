#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 10
# Problem 3
# 204111 Sec 002

def patterned_message(message, pattern):
    out = [' ']*len(pattern)
    n=0
    message = ''.join((message.split())) 
    
    for i,mes in enumerate(pattern):
        if mes == "*":
            out[i] = message[n%len(message)]
            n+=1
        elif mes == "\n":
            out[i] = '\n'

    outp = ''.join(out) 
    print(outp)

def main():
    patterned_message("Three Diamonds!",'''
   *     *     *
  ***   ***   ***
 ***** ***** *****
  ***   ***   ***
   *     *     *
''')


if __name__ == '__main__':
    main()

