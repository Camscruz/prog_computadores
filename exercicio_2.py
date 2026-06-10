"""
**Exercício 2**

*   Escreva uma função que recebe como parâmetros o peso e altura de uma pessoa e retorna o IMC, de acordo com a tabela abaixo.

*   Em seguida, escreva um programa completo que:
    *   Contém a função criada
    *   Realiza a leitura de dois números reais (input) representando peso e altura do usuário
    *   Usa a função para calcular o IMC do usuário
    *   Imprime o resultado.
    """


def imc(p, a):
    m = p/a**2

    if m < 18.5:
        return ("Você está abaixo do peso")
    elif m < 25.0:
        return ("Você está saúdavel")
    elif m < 30.0:
        return ("Você está com peso em excesso")
    elif m < 35.0:
        return ("Você está com obesidade grau I")
    else:
        return ("Você está com obesidade grau II")


p = input('Digite o seu peso (em kg): ')
a = input('Digite sua altura (em m): ')

print(imc(float(p), float(a)))
