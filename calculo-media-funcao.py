#Escreva um código que peça ao usuário dois números na função main()
#e utilize uma função separada para o cálculo da média desses números.
def media(n1, n2):
    media = (n1 + n2) /2
    return media

def main():
    n1 = float(input("numero 1: "))
    n2 = float(input("numero 2: "))
    print ("média = ", media(n1, n2))

main()
