
for numero in range(0, 31, 2):  # percorre apenas os pares de 0 a 30
    if numero in [10, 20, 30]:
        continue  # pula esses números
    print(numero)