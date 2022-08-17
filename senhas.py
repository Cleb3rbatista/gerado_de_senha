import random
def senha():
    
    letra_minuscula ="qwertyuioplkjhgfdsazxcvbnm"
    letra_maiuscula ="QWERTYUIOPLKJHGFDSAZXCVBNM"
    numeros ="0123456789"
    sibolos ="!@#$%¨&*()_+"
    n=0
    while n<5:
        n+=1
        misturar=letra_maiuscula+letra_minuscula+sibolos+numeros
        quatidade_de_caracteres = 20
        password="".join(random.sample(misturar,quatidade_de_caracteres))
        print(f"Sua senha é{password}")
        print("-" * 30)

    senha()
    