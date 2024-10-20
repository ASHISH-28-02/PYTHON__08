sys = [["Decimal", 10], ["Octal", 8], ["Hexadecimal", 16]]
deci = 0
ans = 0
num = 0
rev = 0
strAns = ""
hexDigi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

print("Number System Convertor\nConvert to/from Binary to\n1 : Decimal\n2 : Octal\n3 : Hexadecimal\n\n4 : To exit\n\n> ", end="")

ip = int(input())
if ip >= 4:
    exit()
rad = ip-1

print(f"1 : Binary to {sys[rad][0]} or \n2 : {sys[rad][0]} to Binary ?\n> ", end="")

ip = int(input())

if ip == 1:
    print("Binary value : ", end="")
    digi = input()
    for i in range(len(digi)):
        deci += int(digi[-i-1]) * 2 ** i
    
    if rad == 0:
        print(f"Decimal value : {deci}")
        exit()
    elif rad == 1:
        while deci:
            rev = rev*10 + deci%8
            deci //= 8
        while rev:
            ans = ans*10 + rev%10
            rev //= 10
        print(f"Octal value : {ans}")
    elif rad == 2:
        while deci:
            strAns = hexDigi[deci%16] + strAns
            deci //= 16
        print(f"Octal value : {strAns}")
elif ip == 2:
    if rad == 0:
        print("Decimal value : ", end="")
        num = int(input())
    elif rad == 1:
        print("Octal value : ", end="")
        digi = input()
        for i in range(len(digi)):
            num += int(digi[-1-i])*8**i
    elif rad == 2:
        print("Hexadecimal value : ", end="")
        digi = input()
        for i in range(len(digi)):
            num += hexDigi.index(digi[-1-i])*16**i
    while num:
        rev = rev*10 + num%2
        num //= 2
    while rev:
        ans = ans*10 + rev%10
        rev //= 10
    print(f"Binary value : {ans}")    
