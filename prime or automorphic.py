number = input('enter your number\n')
length = len(number)
n = int(number)
square = n**2
power = 10**length
x = True
for i in range(2,n):
    if n%i==0:
        x=False
        break

if x:
    print("prime")
else:
    if square % power == n:
        print("automorphic")
    else:
        print("neither automorphic nor prime")