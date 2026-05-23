vysledek=float(input("cislo: "))
while True:

    operace = input("Operace (+ - * /): ")

    if operace == "=":
        print(vysledek)
        break


    b = float(input("cislo: "))

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



