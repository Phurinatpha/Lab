#!/usr/bin/env python3
# ภูริณัฐ ภาณุพงศ์สกุล
# 640510676
# Lab 09
# Problem 4
# 204111 Sec 002

def main():
    p = [(0,0), (0,1), (0, -1), (0, 0.5), (0, -0.5), (1, 0), (1, 1), (1, -1), (1, 0.5), (1, -0.5)]
    x = 'y'
    print(print_polynomial(p, x))

def print_polynomial(p, x):
    rev_p = list(reversed(sorted(p)))
    zipm = list(map(list ,zip(*rev_p)))
    str_p = ""
    count = 0
    for i in range(len(p)):
       
        if rev_p[i][0]>1 and rev_p[i][1]!=0 and count==0 and abs(rev_p[i][1])==1:
            if rev_p[i][1]>0:
                str_p += '+{}^{}'.format(x,rev_p[i][0])
            else:
                str_p += '-{}^{}'.format(x,rev_p[i][0])
            count +=1

        elif rev_p[i][0]>1 and rev_p[i][1]!=0 and count==0:
            str_p += '{}{}^{}'.format(rev_p[i][1],x,rev_p[i][0])
            count +=1


        else:
            if rev_p[i][0]>1 and rev_p[i][1]!=0:
                if rev_p[i][1]>0:
                    str_p += ' + {}{}^{}'.format(rev_p[i][1],x,rev_p[i][0])

                elif rev_p[i][1]<0:
                    str_p += ' - {}{}^{}'.format(rev_p[i][1],x,rev_p[i][0])
                else:
                    str_p += '{}{}^{}'.format(abs(rev_p[i][1]),x,rev_p[i][0])

            elif rev_p[i][0] == 1 and rev_p[i][1]!=0:
                if rev_p[i][1]>0 and rev_p[i][1]!=1:
                    str_p += ' + {}{}'.format(rev_p[i][1],x)
                elif rev_p[i][1]<0 and rev_p[i][1]!=1:
                    str_p += ' - {}{}'.format(abs(rev_p[i][1]),x)
                else:
                    str_p += '{}'.format(x)

            elif rev_p[i][0] == 0 and rev_p[i][1]!=0:
                if rev_p[i][1]>0:
                    str_p += ' + {}'.format(rev_p[i][1])
                else:
                    str_p += ' - {}'.format(abs(rev_p[i][1]))

    return str_p

if __name__ == '__main__':
    main()

