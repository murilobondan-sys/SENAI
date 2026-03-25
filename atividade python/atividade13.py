numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(11):
    print(f"{numero} x {i} = {numero * i}")
