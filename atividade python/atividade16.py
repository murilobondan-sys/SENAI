print("Bem-vindo ao sistema de qualidade da fábrica de sensores!")
total_leitura = 0.0
for i in range(1, 6):
    leitura = float(input(f"Digite o valor da leitura do sensor {i}: "))
    horas_uso = int(input(f"Digite a quantidade de horas de uso do sensor {i}: "))
    if horas_uso < 200:
        fator_calibracao = 0.0
    elif 200 <= horas_uso < 1000:
        fator_calibracao = 0.05
    elif 1000 <= horas_uso < 2000:
        fator_calibracao = 0.10
    else:
        fator_calibracao = 0.15
    valor_calibrado = leitura * (1 - fator_calibracao)
    total_leitura += valor_calibrado
    print(f"Sensor {i}: Valor Bruto = {leitura:.2f}, Valor Calibrado = {valor_calibrado:.2f}")
media_calibrada = total_leitura / 5
print(f"Valor médio calibrado dos sensores: {media_calibrada:.2f}")