soma=0
media=0
contador=0
while contador < 5:
    contador += 1
    numero = float(input(f"insira o salário dos trabalhadores:{contador} "))
    soma += numero
media = soma/contador
print("a media dos numeros: ", media)
print("a soma dos numeros: ", soma)