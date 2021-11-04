from palavrasDB import palavras
from imagem_forca import forca
import random
numero_de_erros_para_perder = 6
def iniciar_jogo():
    palavra_correta = obter_palavra_aleatoria(palavras)
    comprimento_da_palavra = len(palavra_correta)
    palavra_ocultada = "_" * comprimento_da_palavra
    numero_de_erros = 0
    letras_inseridas = []

    tem_jogo_em_andamento = True
    while tem_jogo_em_andamento:
        atualizar_tela_do_jogo(
                palavra_ocultada,
                numero_de_erros,
                letras_inseridas
                )
        letra = obter_letra_do_usuario()
        letras_inseridas.append(letra)
        tem_acerto = verificar_acerto(letra, palavra_correta)
        if tem_acerto == "acerto":
            palavra_ocultada = revelar_letra(
                    letra,
                    palavra_ocultada,
                    palavra_correta
                    )
            tem_palavra_completada = palavra_correta == palavra_ocultada
            if tem_palavra_completada:
                mostrar_mensagem_de_jogo_ganho(palavra_correta)
                tem_jogo_em_andamento = False
        else:
            numero_de_erros += 1
            if numero_de_erros >= numero_de_erros_para_perder:
                atualizar_tela_do_jogo(
                        palavra_ocultada,
                        numero_de_erros,
                        letras_inseridas
                        )
                tem_jogo_em_andamento = False

def obter_palavra_aleatoria(lista_palavras):
    # Retorna uma palavra aleatória da lista, sem capitalização
    return lista_palavras[random.randint(0, len(lista_palavras) - 1)].lower()

def atualizar_tela_do_jogo(
        palavra_ocultada,
        numero_de_erros,
        letras_inseridas
        ):
    print("\n" * 2)
    forca(numero_de_erros)
    print("\n")
    print("Palavra:  " + palavra_ocultada)
    linha_com_numero_de_erros = (
            "Erros:    "
            + str(numero_de_erros) + "/" + str(numero_de_erros_para_perder)
            )
    print(linha_com_numero_de_erros)
    linha_com_letras_inseridas = "Chutes:   " + " ".join(letras_inseridas)
    print(linha_com_letras_inseridas)

def obter_letra_do_usuario():
    letra_user = input('Digite uma letra: ').strip().lower()
    while len(letra_user) != 1 or not letra_user.isalpha():
        letra_user = input('Valor não aceito, tente novamente.\n'
                           'Digite uma letra: ').strip().lower()
    return letra_user

def verificar_acerto(letra, palavra_correta):
    letra = letra
    palavra_correta = palavra_correta
    output = ""
    lista_palavra_correta = []
    for x in palavra_correta:
        lista_palavra_correta.append(x)
    for q in lista_palavra_correta:
        if letra == q:
            output = "acerto"
    return output

def revelar_letra(letra, palavra_ocultada, palavra_correta):
    nova_palavra_ocultada = palavra_ocultada
    formas_da_letra_com_acentos = obter_formas_da_letra_com_acentos(letra)

    for letra_com_acento in formas_da_letra_com_acentos:
        indice_de_inicio = 0
        tem_letras_para_mostrar = True
        while tem_letras_para_mostrar:
            indice_da_letra = palavra_correta.find(
                    letra_com_acento,
                    indice_de_inicio
                    )
            if indice_da_letra == -1:
                tem_letras_para_mostrar = False
            else:
                nova_palavra_ocultada = (
                        nova_palavra_ocultada[0:indice_da_letra]
                        + letra_com_acento
                        + nova_palavra_ocultada[indice_da_letra + 1:]
                        )
                indice_de_inicio = indice_da_letra + 1
    return nova_palavra_ocultada

def obter_formas_da_letra_com_acentos(letra):
    formas = [letra]
    formas_somente_com_acentos = []

    if letra == "a":
        formas_somente_com_acentos = ["á", "à", "ã", "â"]
    elif letra == "e":
        formas_somente_com_acentos = ["é", "ê"]
    elif letra == "i":
        formas_somente_com_acentos = ["í"]
    elif letra == "o":
        formas_somente_com_acentos = ["ó", "õ", "ô"]
    elif letra == "u":
        formas_somente_com_acentos = ["ú"]
    elif letra == "c":
        formas_somente_com_acentos = ["ç"]

    formas.extend(formas_somente_com_acentos)
    return formas

def mostrar_mensagem_de_jogo_ganho(palavra_correta):
    mensagem_de_vitoria = ("\nVocê ganhou o jogo.\nA palavra é "
            + "\"" + str(palavra_correta) + "\"" + "." + "\n")
    print(mensagem_de_vitoria)

if __name__ == "__main__":
    deci = input("Deseja iniciar o jogo?[sim/nao]").lower()
    if deci == "sim":
        iniciar_jogo()

