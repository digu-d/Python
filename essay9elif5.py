print("Bem vindo ao Clash  Royale")
print("Monte seu deck e veja se e ele é bom")

sim = True
não = False

trofeus = int(input("Quantos trofeus voce possui  atualmente? "))
deck = input("Seu deck e leve ou pesado: ")
usa_feitiço = input("Voce usa algum feitiço? (sim/não) ")
nivel_rei = int(input("Qual o nivel da suta torre do rei? "))

bom_player = trofeus > 8500 and nivel_rei >= 14

if bom_player and deck =="leve" and usa_feitiço =="sim":
    print("Deck Excelente,voce  merece estar na liga das lendas")
elif deck =="pesado" and (usa_feitiço =="não" or nivel_rei <11):
    print("Deck arriscado, sem  feitiço com cartas  pesadas, cuidado contra ciclos rápidos")
elif deck =="leve" and(trofeus > 5000 and not usa_feitiço =="não"):
    print("Ótimo, Deck  de ciclo rapido, um estilo de deck que  demanda mais skill  com feitiços baratos e versateis, porem e um estilo de deck otimo para subir de arena")
else:
    print("Deck muito  ruim, acho que  o deck inical deve ser melhor kkkk")

print("Fim, Boa sorte agora nas suas próximas partidas , mais toma cuidado com o deck")
