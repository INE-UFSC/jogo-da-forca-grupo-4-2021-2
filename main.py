numero_maximo_de_erros = 7
def iniciar_jogo():
    palavra_correta = obter_palavra_aleatoria()
    comprimento_da_palavra = len(palavra_correta)
    palavra_ocultada = "_" * comprimento_da_palavra
    numero_de_erros = 0

    tem_jogo_em_andamento = True
    while tem_jogo_em_andamento:
        mostrar_palavra_ocultada(palavra_ocultada)
        mostrar_numero_de_erros(numero_de_erros)
        letra = obter_letra_do_usuario()
        tem_acerto = verificar_acerto(letra, palavra_correta)
        if tem_acerto:
            palavra_ocultada = revelar_letra(
                    letra,
                    palavra_ocultada,
                    palavra_correta
                    )
            tem_palavra_completada = palavra_correta == palavra_ocultada
            if tem_palavra_completada:
                mostrar_mensagem_de_jogo_ganho()
                tem_jogo_em_andamento = False
        else:
            numero_de_erros += 1
            if numero_de_erros > numero_maximo_de_erros:
                mostrar_mensagem_de_jogo_perdido()
                tem_jogo_em_andamento = False

def obter_palavra_aleatoria():
    pass

def mostrar_palavra_ocultada(palavra_ocultada):
    pass

def mostrar_numero_de_erros(numero_de_erros):
    pass

def obter_letra_do_usuario():
    pass

def verificar_acerto(letra, palavra_correta):
    pass

def revelar_letra(letra, palavra_ocultada, palavra_correta):
    pass

def mostrar_mensagem_de_jogo_perdido():
    pass

def mostrar_mensagem_de_jogo_ganho():
    pass

