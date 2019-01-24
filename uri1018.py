N = int(input())
print(N)
if 0 < N < 1000000:
    note1=0
    note2=0
    note5=0
    note10=0
    note20=0
    note50=0
    note100=0
    while N >= 1:
        if N < 2:
            note1 = N//1
            N = N % 1
        elif N < 5:
            note2 = N//2
            N = N % 2
        elif N < 10:
            note5 = N//5
            N = N % 5
        elif N < 20:
            note10 = N//10
            N = N % 10
        elif N < 50:
            note20 = N//20
            N = N % 20
        elif N < 100:
            note50 = N//50
            N = N % 50
        else:
            note100 = N//100
            N = N % 100
print(str(note100)+" nota(s) de R$ 100,00")
print(str(note50)+" nota(s) de R$ 50,00")
print(str(note20)+" nota(s) de R$ 20,00")
print(str(note10)+" nota(s) de R$ 10,00")
print(str(note5)+" nota(s) de R$ 5,00")
print(str(note2)+" nota(s) de R$ 2,00")
print(str(note1)+" nota(s) de R$ 1,00")