import math
A, B, C =input().split()
A = float(A)
B = float(B)
C = float(C)
if (A != 0):
    mid = (B * B) - (4 * A * C)
    if (mid > 0):
        r1 = (- B+math.sqrt(mid)) / (2 * A)
        r2 = (- B - math.sqrt(mid)) / (2 * A)
        print("R1 = %.5f" %r1)
        print("R2 = %.5f" %r2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")