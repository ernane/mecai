from math import factorial


data = input()

x, n = data.split()

x = float(x)
n = int(n)

count = 1
s = x

for i in range(2, (n * 2) + 2, 2):
    if count % 2 != 0:
        s -= round((x**i) / factorial(i + 1), 6)
    else:
        s += round((x**i) / factorial(i + 1), 6)
    count += 1

print(s)
