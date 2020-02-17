print("Bem vindo ao Aumento de Salário")

SALARIO=float(input("Por favor, insira o valor do seu atual sálario"))

if SALARIO > 900:
    
    print("Infelizmente você não pode receber o beneficio.")

elif SALARIO <= 300:
    CREDITO = float (SALARIO/100*15)
    SALDOAUMENTO= SALARIO+CREDITO

    print("Devido ao aumento, seu salário de:",SALARIO, "você recebera um acrescimo de 15% e passa a receber:" ,SALDOAUMENTO,)
    
elif SALARIO > 300 and SALARIO <= 600:
     CREDITO = float (SALARIO/100*10)
     SALDOAUMENTO= SALARIO+CREDITO

     print("Devido ao aumento, seu salário de:",SALARIO, "você recebera um acrescimo de 10% e passa a receber:" ,SALDOAUMENTO,)

elif SALARIO > 600 and SALARIO <= 900:
     CREDITO = float (SALARIO/100*5)
     SALDOAUMENTO= SALARIO+CREDITO

     print("Devido ao aumento, seu salário de:",SALARIO, "você recebera um acrescimo de 5% e passa a receber:" ,SALDOAUMENTO,)




