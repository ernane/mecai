direcao = input()

qntordens = 0


for idx, i in enumerate(direcao):
    if direcao[idx] == "D":
        qntordens += 1
    elif direcao[idx] == "E":
        qntordens -= 1

if qntordens % 4 == 1 or qntordens % 4 == -3:
    print("Leste")
elif qntordens % 4 == 2 or qntordens % 4 == -2:
    print("Sul")
elif qntordens % 4 == 3 or qntordens % 4 == -1:
    print("Oeste")
else:
    print("Norte")
