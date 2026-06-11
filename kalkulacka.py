import math

vysledek = input("cislo: ")

if vysledek == "pi":
        vysledek = math.pi
else:
        vysledek = float(vysledek)


while True:
    operace = input("Operace [+, -, *, /, (, =]: ")
    match operace:
        case "+":
            b = input("cislo: ")
            if b == "pi":
                b = math.pi
            else:
                b = float(b)
            vysledek += b
            print(vysledek)

        case "-":
            b = input("cislo: ")
            if b == "pi":
                b = math.pi
            else:
                b = float(b)
            vysledek -= b
            print(vysledek)

        case "*":
            b = input("cislo: ")
            if b == "pi":
                b = math.pi
            else:
                b = float(b)
            vysledek *= b
            print(vysledek)

        case "/":
            b = input("cislo: ")
            if b == "pi":
                b = math.pi
            else:
                b = float(b)
            if b != 0:
                vysledek /= b
                print(vysledek)
            else:
                print("Deleni nulou nejde")
        case "(":
            c = input("cislo: ")
            while True:
                c = float(c)
                operace = input("Operace [+, -, *, /, =]: ")
                match operace:
                    case "+":
                        b = input("cislo: ")
                        if b == "pi":
                            b = math.pi
                        else:
                            b = float(b)
                        c += b
                        print(vysledek,"(",c,")")

                    case "-":
                        b = input("cislo: ")
                        if b == "pi":
                            b = math.pi
                        else:
                            b = float(b)
                        c -= b
                        print(vysledek,"(",c,")")

                    case "*":
                        b = input("cislo: ")
                        if b == "pi":
                            b = math.pi
                        else:
                            b = float(b)
                        c *= b
                        print(vysledek, "(", c, ")")

                    case "/":
                        b = input("cislo: ")
                        if b == "pi":
                            b = math.pi
                        else:
                            b = float(b)
                        if b != 0:
                            c /= b
                            print(vysledek, "(", c, ")")
                        else:
                            print("Deleni nulou nejde")
                    case ")":
                        jak = input("jak to chces pripocitat?")
                        match jak:
                            case "+":
                                vysledek+=c
                                print(vysledek)
                            case "-":
                                vysledek-=c
                                print(vysledek)
                            case "*":
                                vysledek*=c
                                print(vysledek)
                            case "/":
                                if c != 0:
                                    vysledek/=c
                                    print(vysledek)
                                else:
                                    print("Deleni nulou nejde")
                            case _:
                                print("neplatne")
                        break

                    case _:
                        print("neplatne")

        case "=":
            if operace == "=":
                print("VYSLEDEK:",vysledek)
            break

        case _:
            print("neplatne")



