idade = int(input("Digite a sua idade: "))
membro = input("Você é membro do clube (sim/não): ").lower()

if idade < 18 or idade >= 65:
    print("Você tem direito a um desconto.")
elif membro == "sim":
    print("Você tem direito a um desconto por ser membro do clube.")
else:
    print("Você não tem direito a um desconto.")
