N = int(input())
years = 0
months = 0
days = 0
for i in range(3):
    if N >= 365:
        if N==30:
            months=1
            days=0
            break
        else:
            years = N//365
            N = N%365
    elif N>=30 and N<365:
        if N==30:
            months=1
            days=0
            break
        else:
            months = N//30
            N = N%30
    else:
        days = N
    i+=1
print(str(years)+' ano(s)')
print(str(months)+' mes(es)')
print(str(days)+' dia(s)')