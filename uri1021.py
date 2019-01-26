N = float(input())
note1 = 0
note2 = 0
note5 = 0
note10 = 0
note20 = 0
note50 = 0
note100 = 0
note_50 = 0
note_25 = 0
note_10 = 0
note_05 = 0
note_01 = 0
if 0.0 < N < 1000000.00:
    while N >= 0.01:
        if N < 0.05:
            note_01 = int(N//0.01)
            N = N % 0.01
        elif N < 0.10:
            note_05 = int(N//0.05)
            N = N % 0.05
        elif N < 0.25:
            note_10 = int(N//0.10)
            N = N % 0.10
        elif N < 0.50:
            note_25 = int(N//0.25)
            N = N % 0.25
        elif N < 1:
            note_50 = int(N//0.50)
            N = N % 0.50
        elif N < 2:
            note1 = int(N//1)
            N = N % 1
        elif N < 5:
            note2 = int(N//2)
            N = N % 2
        elif N < 10:
            note5 = int(N//5)
            N = N % 5
        elif N < 20:
            note10 = int(N//10)
            N = N % 10
        elif N < 50:
            note20 = int(N//20)
            N = N % 20
        elif N < 100:
            note50 = int(N//50)
            N = N % 50
        else:
            note100 = int(N//100)
            N = N % 100
print("NOTAS:")
print(str(note100)+" nota(s) de R$ 100.00")
print(str(note50)+" nota(s) de R$ 50.00")
print(str(note20)+" nota(s) de R$ 20.00")
print(str(note10)+" nota(s) de R$ 10.00")
print(str(note5)+" nota(s) de R$ 5.00")
print(str(note2)+" nota(s) de R$ 2.00")
print("MOEDAS:")
print(str(note1)+" moeda(s) de R$ 1.00")
print(str(note_50)+" moeda(s) de R$ 0.50")
print(str(note_25)+" moeda(s) de R$ 0.25")
print(str(note_10)+" moeda(s) de R$ 0.10")
print(str(note_05)+" moeda(s) de R$ 0.05")
print(str(note_01)+" moeda(s) de R$ 0.01")