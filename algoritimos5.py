print("Bem vindo ao Programa de nova precificação")

PRODUTO=float(input("Por favor, insira o valor do Produto"))

if PRODUTO >= 100:
    REAJUSTE = float (PRODUTO/100*15)
    NOVOPRECO= PRODUTO+REAJUSTE
   

elif PRODUTO > 50 and PRODUTO <= 100:
    REAJUSTE = float (PRODUTO/100*10)
    NOVOPRECO= PRODUTO+REAJUSTE
   

elif PRODUTO <= 50:
    REAJUSTE = float (PRODUTO/100*5)
    NOVOPRECO= PRODUTO+REAJUSTE


if NOVOPRECO < 80:
     CLASSIFICADO =  'Barato'
     print("O novo preço do produto é de:" ,NOVOPRECO, "e ele esta classificado como" ,CLASSIFICADO,) 

elif NOVOPRECO >= 80 and NOVOPRECO <= 120:
      CLASSIFICADO = 'Normal'   
   
elif NOVOPRECO >= 120 and NOVOPRECO <= 200:
      CLASSIFICADO = 'Caro'   

elif NOVOPRECO > 200:
      CLASSIFICADO = 'Muito Caro'     
print("O novo preço do produto é de:" ,NOVOPRECO, "e ele esta classificado como" ,CLASSIFICADO,)
