nota1 = float (input("Digite sua nota: "))
nota2 = float (input("Digite sua segunda nota : "))
nota3 = float (input("Digite sua terceira nota :"))

media = (nota1 + nota2 + nota3)/3 

if media <=6:
    print("Voce foi reprovado")
elif media < 10:
    print("Voce foi aprovado")
else:
    print("Voce passou com nota máxima")


