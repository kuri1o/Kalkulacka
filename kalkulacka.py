import math

def nacti_cislo():
    b = input("cislo: \n")
    if b == "pi":
        return math.pi
    return float(b)

def prevadec(jednotkad):
    a = float(input("kolik?\n"))

    b = input("Na co to chces? (km, m, dm, cm, mm)\n")
    if jednotkad == "km":
        match b:
            case "km":
                print(a*1)
            case "m":
                print(a * 1000)
            case "dm":
                print(a * 10000)
            case "cm":
                print(a * 100000)
            case "mm":
                 print(a * 1000000)
            case _:
                print("neplatne\n")

    if jednotkad == "m":
        match b:
            case "km":
                print(a / 1000)
            case "m":
                print(a * 1)
            case "dm":
                print(a * 10)
            case "cm":
                print(a * 100)
            case "mm":
                print(a * 1000)
            case _:
                print("neplatne\n")


    if jednotkad == "dm":
        match b:
            case "km":
                print(a / 10000)
            case "m":
                print(a / 10)
            case "dm":
                print(a * 1)
            case "cm":
                print(a * 10)
            case "mm":
                print(a * 100)
            case _:
                print("neplatne\n")

    if jednotkad == "cm":
        match b:
            case "km":
                print(a / 100000)
            case "m":
                print(a / 100)
            case "dm":
                print(a / 10)
            case "cm":
                print(a * 1)
            case "mm":
                print(a * 10)
            case _:
                print("neplatne\n")

    if jednotkad == "mm":
        match b:
            case "km":
                print(a / 1000000)
            case "m":
                print(a / 1000)
            case "dm":
                print(a / 100)
            case "cm":
                print(a / 10)
            case "mm":
                print(a * 1)
            case _:
                print("neplatne\n")


pokracovat = "ano"
while pokracovat == "ano":
    print("Kalkulacku nebo prevodnik?\n")
    kalkulacka = input("kal - pre\n")

    match kalkulacka:
        case "kal":

            vysledek = input("cislo: \n")

            if vysledek == "pi":
                vysledek = math.pi
            else:
                vysledek = float(vysledek)

            while True:
                operace = input("Operace [+, -, *, /, (, =]: \n")
                match operace:
                    case "+":
                        b = nacti_cislo()
                        vysledek += b
                        print(vysledek)

                    case "-":
                        b = nacti_cislo()
                        vysledek -= b
                        print(vysledek)

                    case "*":
                        b = nacti_cislo()
                        vysledek *= b
                        print(vysledek)

                    case "/":
                        b = nacti_cislo()
                        if b != 0:
                            vysledek /= b
                            print(vysledek)
                        else:
                            print("Deleni nulou nejde\n")
                    case "(":
                        c = nacti_cislo()
                        while True:
                            operace = input("Operace [+, -, *, /, =]: \n")
                            match operace:
                                case "+":
                                    b = nacti_cislo()
                                    c += b
                                    print(vysledek, "(", c, ")\n")

                                case "-":
                                    b = nacti_cislo()
                                    c -= b
                                    print(vysledek, "(", c, ")\n")

                                case "*":
                                    b = nacti_cislo()
                                    c *= b
                                    print(vysledek, "(", c, ")\n")

                                case "/":
                                    b = nacti_cislo()
                                    if b != 0:
                                        c /= b
                                        print(vysledek, "(", c, ")\n")
                                    else:
                                        print("Deleni nulou nejde\n")
                                case ")":
                                    jak = input("jak to chces pripocitat?\n")
                                    match jak:
                                        case "+":
                                            vysledek += c
                                            print(vysledek)
                                        case "-":
                                            vysledek -= c
                                            print(vysledek)
                                        case "*":
                                            vysledek *= c
                                            print(vysledek)
                                        case "/":
                                            if c != 0:
                                                vysledek /= c
                                                print(vysledek)
                                            else:
                                                print("Deleni nulou nejde\n")
                                        case _:
                                            print("neplatne\n")
                                    break

                                case _:
                                    print("neplatne\n")

                    case "=":
                            print(vysledek)
                            break

                    case _:
                        print("neplatne")

        case "pre":
            prevadet = input("Co chces prevadet: delku\n")
            match prevadet:
                case "delku":
                    jednotkad = input("Jakou jednotu chces prevadet? (km, m, dm, cm, mm)\n")
                    prevadec(jednotkad)
                case _:
                    print("neplatne\n")




        case _:
            print("neplatne\n")

    pokracovat = input("chces znova (ano/ne)\n")