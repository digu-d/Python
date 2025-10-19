idade = int(input("Qual a sua idade: "))
if (idade >=0 and idade < 200):

    tem_autorizacao = (input("Voce possui autorizacao: "))
    if tem_autorizacao =="True" or tem_autorizacao =="False":
        tem_autorizacao = bool(tem_autorizacao)

        tem_ingresso = (input("Voce tem o ingresso: "))
        if tem_ingresso =="True" or tem_autorizacao =="False":
            tem_ingresso = bool(tem_ingresso)

            e_vip = (input("Voce e vip: "))
            if e_vip =="True" or e_vip =="False":
                e_vip = bool(e_vip)

                if(idade >=18 and tem_ingresso) or (idade >12 and idade <18 and  tem_autorizacao and tem_ingresso) or (idade >12 and e_vip):
                    print("Pode entrar")
                else:
                    print("nao pode entrar")
                    
            else:
                print("Vip invalido")
        else:
            print("Ingresso invalido")
    else:
        print("Autorizacao invalida")
else:
    print("Idade invalida")
