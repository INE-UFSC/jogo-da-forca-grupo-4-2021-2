#mostra a forca com o boneco e a lista de letras ja usadas
def forca(n_erros: 0):
    n_erros=n_erros
    if n_erros == 0:
        print("  ________")
        print(" |/      \|")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    elif n_erros == 1:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
    elif n_erros == 2:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |        |  ")
        print(" |")
        print(" |")
        print(" |")
    elif n_erros == 3:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |       /|  ")
        print(" |")
        print(" |")
        print(" |")
    elif n_erros == 4:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |       /|\ ")
        print(" |")
        print(" |")
        print(" |")
    elif n_erros == 5:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |       /|\ ")
        print(" |       /   ")
        print(" |")
        print(" |")
    elif n_erros == 6:
        print("  ________   ")
        print(" |/      \|  ")
        print(" |        O  ")
        print(" |       /|\ ")
        print(" |       / \ ")
        print(" |")
        print(" |VOCÊ PERDEU")
        
#adiciona letras já usadas em uma lista
def adiciona_letra(letra):
    letra=letra
    lista_letras=[]
    lista_letras.append(letra)
    return lista_letras

#imprime as letras já usadas
def mostra_letras(lista):
    lista_letras=', '.join(lista)
    print(lista_letras)
    
#exclui o conteudo da lista de letras
def exclui_lista(lista):
    lista_letras=lista
    lista_letras.clear()