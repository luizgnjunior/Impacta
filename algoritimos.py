
print ("Olá, bem vindo ao programa que calcula sua nota")

N1=float(input("Por favor,Digite a sua primeira nota "))
N2=float(input("Por favor, a sua segunda nota "))
N3=float(input("Por favor, a sua terceira nota "))
N4=float(input("Por favor, a sua quarta nota "))

MEDIA=float(N1+N2+N3+N4)/4

if MEDIA > 7:
    print("Sua nota foi de:",MEDIA, "Parabéns, você foi aprovado(a)!")
else:
    print("Sua nota foi de:",MEDIA, "Infelizmente você não foi aprovado(a).")

