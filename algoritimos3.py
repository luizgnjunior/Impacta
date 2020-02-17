print("Bem vindo ao programa Mini calculadora")

MEDIA=1
DIFERENCA=2
PRODUTO=3
DIVISAO=4

print("Opções validas para este terminal: \n 1-Media \n 2-Diferença \n 3-Produto \n 4-divisição")

CALCULO=float(input("Por favor insira o número correspondente:"))

if CALCULO > 4:
    print("ERRO: Caracter inválido, por favor tente novamente mais tarde")

elif CALCULO==1:
    N1=float(input("Por favor insira o primeiro numero"))
    N2=float(input("Agora, o segundo numero"))
    
    MEDIA=(N1+N2)/2
    print("A média da entre os número digitados é de:",MEDIA)
    
elif CALCULO==2:
    N1=float(input("Por favor insira o primeiro numero"))
    N2=float(input("Agora, o segundo numero"))

    if N1>N2:
        CALCULO=N1-N2
        print("A diferença entre os números é de:" ,CALCULO)
    else:
        CALCULO=N2-N1
        print("A diferença entre os números é de:" ,CALCULO)

elif CALCULO==3:
    N1=float(input("Por favor insira o primeiro numero"))
    N2=float(input("Agora, o segundo numero"))

    CALCULO= N1*N2
    print("O produto na sua equação é:" ,CALCULO)

elif CALCULO==4:
     N1=float(input("Por favor insira o primeiro numero"))
     N2=float(input("Agora,digite por qual numero deseja dividir"))

if N2!= 0:
      CALCULO=N1/N2
      print("O Valor da divisão é de:" ,CALCULO)
else:
     N2=float(input("Não é possivel a divisção por ZERO, insira um novo numero"))
     CALCULO=N1/N2
     print("O Valor da divisão é de:" ,CALCULO)
    
        
    
    
