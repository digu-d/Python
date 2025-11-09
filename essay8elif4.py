idade = int(input("Qual a sua idade? "))
if (idade >18  and idade <100):
    
    tem_experiencia = (input("Voce tem experiencia? (True/False) "))
    if tem_experiencia =="True" or tem_experiencia =="False":
        tem_experiencia = bool(tem_experiencia)

        ficha_criminal = (input("Voce possui ficha criminal? (True/False) "))
        if ficha_criminal =="True" or  ficha_criminal =="False":
            ficha_criminal = bool(ficha_criminal)

            ensino_completo = (input("Voce possui ensino completo? (True/False) "))
            if ensino_completo =="True" or ensino_completo =="False":
                ensino_completo = bool(ensino_completo)

                foi_indicado = (input("Voce foi indicado? (True/False) "))
                if foi_indicado =="True" or foi_indicado =="False":
                    foi_indicado == bool(foi_indicado)

                    if(idade >18 and tem_experiencia and not ficha_criminal ):
                        print("Pode Participar  Pela sua experiencia")
                    elif(idade >18 and not ficha_criminal and ensino_completo  or foi_indicado):
                        print("Pode Participar Pelo seu ensino ou Indicação")
                    else:
                        print("Não pode participar")
                
                else:
                    print("Indicado Inválido")
            else:
                print("Ensino Inválido")
        else:
            print("Ficha criminal Inválida")
    else:
        print("Experiencia Inválida")
else:
    print("Idade Inválida")
        

                
