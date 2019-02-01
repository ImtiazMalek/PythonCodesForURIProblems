X,Y = input().split()
Y = int(Y)
result=0.00
if X=="1":
    result=4.00
if X=="2":
    result=4.50
if X=="3":
    result=5.00
if X=="4":
    result=2.00
if X=="5":
    result=1.50
result=result*Y
print('Total: R$ %.2f' %result)