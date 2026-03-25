pressao = 0.0
temperatura = 0.0
reduçao = 0.0
ciclos = int(input("Digite a quantidade de ciclos de trabalho: "))
pressao = float(input("Digite a pressão lida (em bar): "))
temperatura = float(input("Digite a temperatura lida (em °C): "))
if ciclos < 200:
    reduçao = 0.0
elif 200 <= ciclos < 1000:
    reduçao = 0.05
elif 1000 <= ciclos < 2000:
    reduçao = 0.10
else:
    reduçao = 0.15
fator_risco = (pressao * temperatura) * (1 - reduçao)
print(f"Fator de Risco calculado: {fator_risco:.2f}")
print(f"redução da pressão: {reduçao * pressao:.2f} bar")
