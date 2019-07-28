print ("Bem vindo ao Cálculo do Índice de Massa Corporal - IMC")
print("Insira alguns dados para saber o seu IMC")

peso = float(input("Informe o seu peso(em kg):"))
altura = float(input("Informe a sua altura(em m):"))
imc = peso / (altura*altura)

print ("Seu IMC é igual a:","%.2f" % imc)

if imc <= 17:
    print("Você está muito abaixo do peso.")

elif imc >= 17 and imc <= 18.49:
    print("Você está abaixo do peso.")

elif imc >= 18.50 and imc  <= 24.99:
    print("Você está com o peso normal, parabéns!")

elif imc >= 25 and imc <= 29.99:
    print("Você está um pouco acima do peso, cuidado!")

elif imc >= 30 and imc <= 34.99:
    print("Você está no primeiro estágio de obesidade!")

elif imc >= 35 and imc <= 39.99:
    print("Você está no segundo estágio de obesidade (severa).")

elif imc>= 40:
    print("Você está em situação de obesidade mórbida.")