import math

def kalkulackao():
    def nacti_cislo():
        b = input("cislo: \n")
        if b == "pi":
            return math.pi
        return float(b)

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

def prevadec():
    prevadet = input("Co chces prevadet: delku\n")
    match prevadet:
        case "delku":
            jednotkad = input("Jakou jednotu chces prevadet?\nµ - alt + 0181\nmetricky = [km, m, dm, cm, mm, µm, nm]\namericke = [in, ft, yd, mi]\n")

            na_metry = {
                "km": lambda a: a * 1000,
                "m":  lambda a: a,
                "dm": lambda a: a / 10,
                "cm": lambda a: a / 100,
                "mm": lambda a: a / 1000,
                "µm": lambda a: a / 1000000,
                "nm": lambda a: a / 1000000000,
                "in": lambda a: a * 0.0254,
                "ft": lambda a: a * 0.3048,
                "yd": lambda a: a * 0.9144,
                "mi": lambda a: a * 1609.344,
            }

            z_metru = {
                "km": lambda m: m / 1000,
                "m":  lambda m: m,
                "dm": lambda m: m * 10,
                "cm": lambda m: m * 100,
                "mm": lambda m: m * 1000,
                "µm": lambda m: m * 1000000,
                "nm": lambda m: m * 1000000000,
                "in": lambda m: m / 0.0254,
                "ft": lambda m: m / 0.3048,
                "yd": lambda m: m / 0.9144,
                "mi": lambda m: m / 1609.344,
            }

            if jednotkad in na_metry:
                a = float(input("kolik?\n"))
                b = input("Na co to chces? (km, m, dm, cm, mm, µm, nm, in, ft, yd, mi)\n")
                if b in z_metru:
                    metry = na_metry[jednotkad](a)
                    print(z_metru[b](metry))
                else:
                    print("neplatne\n")
            else:
                print("neplatne\n")
        case _:
            print("neplatne\n")



pokracovat = "ano"
while pokracovat == "ano":
    print("Kalkulacku nebo prevodnik?\n")
    kalkulacka = input("kal - pre\n")

    match kalkulacka:
        case "kal":
            kalkulackao()

        case "pre":
            prevadec()

        case _:
            print("neplatne\n")

    pokracovat = input("chces znova (ano/ne)\n")