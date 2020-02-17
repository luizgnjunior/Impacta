print("Bem vindo ao Programa de Investimento")

POUPANCA=1
FUNDOS=2

print("Escolha a opção desejada: \n 1-Poupança \n 2-Fundos de renda Fixa")

TIPO=float(input("Por favor insira o número correspondente:"))

if TIPO > 2:
    print("ERRO: Caracter inválido, por favor tente novamente mais tarde")

elif TIPO==1:
    N1=float(input("Por favor insira o valor do investimento"))
    REAJUSTE = float (N1/100*3)
    VALOR = float (REAJUSTE + N1)
    print("Como a opção escolhida foi a de Poupança, o valor do investimento é de:",VALOR,)
    

elif TIPO==2:
    N1=float(input("Por favor insira o valor do investimento"))
    REAJUSTE = float (N1/100*4)
    VALOR = float (REAJUSTE + N1)
    print("Como a opção escolhida foi a de Fundos de renda Fixa, o valor do investimento é de:" ,VALOR,)
