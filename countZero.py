n = int(input(''))
co = 0 
for i in range(1,n+1):
    if '0' in str(i):
        co += str(i).count('0')

print(co)
