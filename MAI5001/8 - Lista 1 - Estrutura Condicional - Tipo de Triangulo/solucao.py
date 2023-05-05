# l1 = int(input())
# l2 = int(input())
# l3 = int(input())
entrada = input()

l1, l2, l3 = entrada.split()

l1 = float(l1)
l2 = float(l2)
l3 = float(l3)

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print("Não pode ser um triangulo")
elif l1 == l2 == l3:
    print("equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("isosceles")
else:
    print("escaleno")
