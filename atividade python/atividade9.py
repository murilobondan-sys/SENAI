maior = float()
menor = float()
soma = 0 
acima_100 = 0
for cont in range(10):
    temperatura = float(input(f"digite a {cont + 1} temperatura: "))
    soma += temperatura
    if cont == 0:
        maior = temperatura
        menor = temperatura
    if temperatura > 100:
        acima_100 += 1
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
media = soma / 10
print(f"temperatura media: {media}")
print(f"temperatura maior: {maior}")
print(f"temperatura menor: {menor}")    
print(f"quantidade de temperaturas acima de 100: {acima_100} vezes")
