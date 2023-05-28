n = int(input(''))
count = 0 
for i in range(1,n+1):
    if '0' in str(i):
        count += str(i).count('0')

print(count)
