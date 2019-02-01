A = float(input())
if 0 <= A <= 100:
    if A<=75:
        if A<=50:
            if A<=25:
                print("Intervalo [0,25]")
            else:
                print("Intervalo (25,50]")
        else:
            print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")
else:
    print("Fora de intervalo")