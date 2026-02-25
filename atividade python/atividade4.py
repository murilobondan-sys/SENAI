nota1 = float(input("insira a nota1 "))
nota2 = float(input("insira a nota2 "))
nota3 = float(input("insira a nota3 "))
nota4 = float(input("insira a nota4 "))
media = (nota1+nota2+nota3+nota4)/4
print("a media das notas: ", media)
if media >= 7:
    print("aluno esta aprovado")
else:
    print("aluno esta reprovado")