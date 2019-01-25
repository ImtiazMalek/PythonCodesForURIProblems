N = int(input())
hours = 0
minutes = 0
seconds = 0
for i in range(3):
    if N>3600:
        hours = N//3600
        N = N%3600
    elif 60<N<3600:
        minutes = N//60
        N = N%60
    else:
        seconds = N
    i+=1
print(str(hours)+':'+str(minutes)+':'+str(seconds))