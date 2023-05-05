# import functools
# import math

# n = int(input())


# @functools.cache
# def fatorial(n):
#     return n * fatorial(n-1) if n else 1

# x = fatorial(n)

# print()
import math


# rad
def para_radianos(x):
    return x/180*math.pi


# taylor
def taylor(x, i):
    return math.pow(x, i)/math.factorial(i)


# sen
def calcula_seno(x, termos):
    y = 3
    z = 0
    while True:
        z = z - taylor(x, y)
        y = y + 2
        z = z + taylor(x, y)
        y = y + 2
        if y >= termos:
            break
    return x+z


# testa seno
print('testa seno:')
seno_math = math.sin(para_radianos(1.500988))
seno_taylor = calcula_seno(para_radianos(1.500988), 200)
print('math.sin: ' + str(seno_math))
print('taylor:   ' + str(seno_taylor))
print('')
