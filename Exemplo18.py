idade = int(input("Digite a sua idade: "))

if idade < 14:
    print("Você é uma criança.")
elif 14 <= idade < 18:
    print("Você é um adolescente.")
elif 18 <= idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
    