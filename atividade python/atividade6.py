nome = input("digite seu nome: ")
idade = int(input("digite a idade em anos: "))
while idade > 120 or idade < 0:
    idade = int(input("idade(anos completos - ate 120 anos)"))
dias_de_vida = idade * 365
print(f"{nome}, voce viveu {dias_de_vida})