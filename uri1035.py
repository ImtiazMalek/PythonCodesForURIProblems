A = int(input())
B = int(input())
C = int(input())
D = int(input())
greater=C+D
smaller=A+B
even=A%2
def wrong():
    print('Valores nao aceitos')
if B>C and D>A:
    if greater>smaller:
        if C>=0 and D>=0:
            if even==0:
                print('Valores aceitos')
            else:
                wrong()
        else:
            wrong()
    else:
        wrong()
else:
    wrong()