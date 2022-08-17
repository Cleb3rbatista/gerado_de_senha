from ast import Break

letra_minuscula ="qwertyuioplkjhgfdsazxcvbnm"
letra_maiuscula ="QWERTYUIOPLKJHGFDSAZXCVBNM"
numeros ="0123456789"
sibolos ="!@#$%¨&*()_+"
def main():
    escolha=int(input("deseja gerar mais senhas ?\n"+"digite 1 para sim e 0 para não\n"))
    if escolha== 1:
        senha()
    elif escolha==0:
        print("saindo...")
        Break
    elif (escolha!=1 and escolha!=0):
        print("opção invalida")
        main()
         
def senha():
    import random
    n=0
    while n<5:
        n+=1
        misturar=letra_maiuscula+letra_minuscula+sibolos+numeros
        quatidade_de_caracteres = 20
        password="".join(random.sample(misturar,quatidade_de_caracteres))
        print(f"Sua senha é{password}")
        print("-" * 30)
    else:
        main()
        
escolha1=int(input("deseja gerar senhas ?\n"+"digite 1 para sim e 0 para não\n"))
if escolha1!=1 and escolha1!=0:
    print("opção invalida")
    main()
if escolha1== 1:
    senha()
if escolha1==0:
    print("saindo...")
    Break
else:
    print("opção invalida")
    main()        
        
