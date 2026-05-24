import math

vysledek = input("cislo: ")

if vysledek == "p":

        vysledek = math.pi

else:

        vysledek = float(vysledek)

while True:

    operace = input("Operace (+ - * /): ")

    #if operace == "()": závorka budouci

    if operace == "=":
        print(vysledek)
        break

    b = (input("cislo: "))

    if b == "p":

        b = math.pi

    else:

        b = float(b)



    if operace == "+":
        vysledek += b
        print(vysledek)


    elif operace == "-":
        vysledek -= b
        print(vysledek)


    elif operace == "*":
        vysledek *= b
        print(vysledek)

    elif operace == "/":
        if b != 0:
            vysledek /= b
            print(vysledek)

        else:
            print("Deleni nulou nejde")



