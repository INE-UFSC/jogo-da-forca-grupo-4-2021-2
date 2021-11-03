def iniciar_testes():
    testar_revelar_letra()

def testar_revelar_letra():
    from main import revelar_letra
    
    tem_teste_funcionando = True

    palavra_teste = "teste"
    letra = "e"
    palavra_ocultada = "_" * len(palavra_teste)
    palavra_revelada = revelar_letra(letra, palavra_ocultada, palavra_teste)
    retorno_esperado = "_e__e"

    tem_retorno_correto = palavra_revelada == retorno_esperado
    if not tem_retorno_correto:
        tem_teste_funcionando = False
        print("Erro na função revelar_letra, teste 1.")

    palavra_teste_2 = "computador"
    letra_2 = "x"
    palavra_ocultada_2 = "_" * len(palavra_teste_2)
    palavra_revelada_2 = revelar_letra(
            letra_2,
            palavra_ocultada_2,
            palavra_teste_2
            )
    retorno_esperado_2 = palavra_ocultada_2

    tem_retorno_correto_2 = palavra_revelada_2 == retorno_esperado_2
    if not tem_retorno_correto_2:
        tem_teste_funcionando = False
        print("Erro na função revelar_letra, teste 2.")

    if tem_teste_funcionando:
        print("Passou nos testes da função revelar_letra.")

iniciar_testes()

