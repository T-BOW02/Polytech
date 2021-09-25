pari = int(input())
numero = int(input())
mise = 10

if pari == 13 and numero % 2 == 0:
    print(20)
else:
    if pari == 14 and numero % 2 != 0:
        print(20)
    else:
        if pari == numero:
            print(120)
        else:
            if pari == 15:
                if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9 or numero == 12:
                    print(20)
                else:
                    if pari == 16:
                        if numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 10 or numero == 11:
                            print(20)
                        else:
                            print(0)
x
