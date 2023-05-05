p1 = int(input())
p2 = int(input())


def mdc(a, b):
    return a if not b else mdc(b, a % b)


print(mdc(p1, p2))
