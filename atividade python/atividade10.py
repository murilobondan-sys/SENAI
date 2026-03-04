maior = float()
menor = float()
soma = 0 
acima_15 = 0
for cont in range(10):
    amper = float(input(f"digite o {cont + 1} amper: "))
    soma += amper
    if cont == 0:
        maior = amper
        menor = amper
    if amper > 15:
        acima_15 += 1
        if amper > maior:
            maior = amper
        if amper < menor:
            menor = amper
media = soma / 10
print(f"Amper media: {media}")
print(f"Amper maior: {maior}")
print(f"Amper menor: {menor}")    
print(f"quantidade de amperes acima de 15: {acima_15} vezes")
