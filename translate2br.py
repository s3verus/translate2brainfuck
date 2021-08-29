#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
    print("please use like this:")
    print("    python3 translate2br.py yourString")
    exit(0)


ourString = sys.argv[1]
def main():
    last_ord = 0
    for i in ourString:
        # print('\n', ord(i))
        # print(last_ord)
        # print(ord(i)-last_ord)
        if ord(i) <= 15:
            last_ord = ord(i)
            print(ord(i)*'+'+'.>', end=' ')
        elif -8 < ord(i) - last_ord < 8:
            summer = ord(i) - last_ord
            if summer == 0:
                print('<.>', end=' ')
            elif summer < 0:
                print('<'+(-summer)*'-'+'.>', end=' ')
            else:
                print('<'+summer*'+'+'.>', end=' ')
            last_ord = ord(i)
        elif len(str(ord(i))) == 2:
                last_ord = ord(i)
                temp = str(ord(i))[0]
                if int(temp) < 6:
                    temp_num = int(temp) * 10
                    left = temp_num / 5
                    right = int(ord(i)%10)
                    print(f"{int(left)*'+'}[>+++++<-]>{int(right)*'+'}.>",end=' ')
                else:
                    right = int(ord(i)%10)
                    print(f"{int(temp)*'+'}[>++++++++++<-]>{int(right)*'+'}.>", end=' ')

        elif len(str(ord(i))) == 3:
            last_ord = ord(i)
            left = int(str(ord(i))[0:2])
            right = int(str(ord(i))[2])
            print(f"{left*'+'}[>++++++++++<-]>{right*'+'}.>", end=' ')
    print()
    
    
if __name__ == "__main__":
    main()
