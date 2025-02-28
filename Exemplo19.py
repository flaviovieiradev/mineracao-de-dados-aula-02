temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura > 30:
    print("Está quente.")
elif temperatura > 20 and temperatura <= 30:
    print("Está agradável.")
elif temperatura > 10 and temperatura <=20:
    print("Está fresco.")
elif temperatura >= 0 and temperatura <=10:
    print("Está frio.")
else:
    print("Temperatura fora do intervalo considerado.")
    