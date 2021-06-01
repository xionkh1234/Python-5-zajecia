import sys

# UWAGA!!! W plikach wejściowych NIE UŻYWAĆ polskich znaków!

if (sys.argv[1] == "saldo"):  # WYWOŁANIE: python <nazwa_programu> saldo <plik_wejsciowy>

    argWartosc = input("Wprowadz wartosc: ")
    argKomentarz = input("Wprowadz komentarz: ")

    inPlik = open(sys.argv[2], "r")
    outPlik = open("out.txt", "w")

    linijki = inPlik.readlines()

    for linijka in linijki:
        if (linijka != "stop"): outPlik.write(linijka)

    outPlik.write(sys.argv[1] + "\n" + argWartosc + "\n" + argKomentarz + "\n" + "stop")

    inPlik.close()
    outPlik.close()

elif (sys.argv[1] == "zakup"):  # WYWOŁANIE: python <nazwa_programu> zakup <plik_wejsciowy>

    argIdentyfikator = input("Wprowadz identyfikator: ")
    argCena = input("Wprowadz cene: ")
    argSprzedane = input("Wprowadz liczbe kupionych sztuk: ")

    inPlik = open(sys.argv[2], "r")
    outPlik = open("out.txt", "w")

    linijki = inPlik.readlines()

    for linijka in linijki:
        linijka = linijka.replace("\n", "").replace(" ", "")
        if (linijka != "stop"): outPlik.write(linijka + "\n")

    outPlik.write(sys.argv[1] + "\n" + argIdentyfikator + "\n" + argCena + "\n" + argSprzedane + "\n" + "stop")

    inPlik.close()
    outPlik.close()

elif (sys.argv[1] == "sprzedaz"):  # WYWOŁANIE: python <nazwa_programu> sprzedaz <plik_wejsciowy>

    argIdentyfikator = input("Wprowadz identyfikator: ")
    argCena = input("Wprowadz cene: ")
    argSprzedane = input("Wprowadz liczbe sprzedanych sztuk: ")

    inPlik = open(sys.argv[2], "r")
    outPlik = open("out.txt", "w")

    linijki = inPlik.readlines()

    for linijka in linijki:
        linijka = linijka.replace("\n", "").replace(" ", "")
        if (linijka != "stop"): outPlik.write(linijka + "\n")

    outPlik.write(sys.argv[1] + "\n" + argIdentyfikator + "\n" + argCena + "\n" + argSprzedane + "\n" + "stop")

    inPlik.close()
    outPlik.close()

elif (sys.argv[1] == "magazyn"):  # WYWOŁANIE: python <nazwa_programu> magazyn <plik_wejsciowy>

    argumenty = {}

    argArgument = ""
    while (True):
        argArgument = input("Wprowadz kolejny identyfikator, wpisz 'KONIEC' aby zakonczyc: ")
        if (argArgument == "KONIEC"):
            break
        argumenty[argArgument] = 0

    inPlik = open(sys.argv[2], "r")
    outPlik = open("out.txt", "w")

    linijki = inPlik.readlines()

    for i, linijka in enumerate(linijki):
        linijka = linijka.replace("\n", "").replace(" ", "")
        if (linijka in argumenty):
            typTransakcji = linijki[i - 1].replace("\n", "")
            if (typTransakcji == "zakup"):
                argumenty[linijka] += int(linijki[i + 2])
            elif (typTransakcji == "sprzedaz"):
                argumenty[linijka] -= int(linijki[i + 2])

    for argument in argumenty:
        print(argument + ": " + str(argumenty[argument]))
        outPlik.write(argument + ": " + str(argumenty[argument]) + "\n")

    inPlik.close()
    outPlik.close()

elif (sys.argv[1] == "konto"):  # WYWOŁANIE: python <nazwa_programu> konto <plik_wejsciowy>

    inPlik = open(sys.argv[2], "r")
    outPlik = open("out.txt", "w")

    suma = 0
    sumowanieSaldo = False
    sumowanieZakup = False
    sumowanieSprzedaz = False

    linijki = inPlik.readlines()

    for i, linijka in enumerate(linijki):
        linijka = linijka.replace("\n", "").replace(" ", "")

        if (sumowanieSaldo == True):
            suma += int(linijka)
            sumowanieSaldo = False
        elif (sumowanieZakup == True):
            if (int(linijki[i + 1]) < 0 or int(linijki[i + 2]) < 0): print("Blad!")
            suma -= int(linijki[i + 1]) * int(linijki[i + 2])
            sumowanieZakup = False
        elif (sumowanieSprzedaz == True):
            if (int(linijki[i + 1]) < 0 or int(linijki[i + 2]) < 0): print("Blad!")
            suma += int(linijki[i + 1]) * int(linijki[i + 2])
            sumowanieSprzedaz = False

        if (linijka == "saldo"):
            sumowanieSaldo = True
        elif (linijka == "zakup"):
            sumowanieZakup = True
        elif (linijka == "sprzedaz"):
            sumowanieSprzedaz = True

    if (suma < 0): print("Blad!")

    print(suma)
    outPlik.write(str(suma))
    inPlik.close()
    outPlik.close()

elif (sys.argv[1] == "przeglad"):  # WYWOŁANIE: python <nazwa_programu> przeglad <index_od> <index_do> <plik_wejsciowy>
    inPlik = open(sys.argv[4], "r")
    outPlik = open("out.txt", "w")

    linijki = inPlik.readlines()

    licznik = 0
    for i, linijka in enumerate(linijki):
        if (i < int(sys.argv[2])): continue
        linijka = linijka.replace("\n", "")
        if (linijka in ["saldo", "zakup", "sprzedaz", "stop"]):
            licznik += 1
            if (licznik > int(sys.argv[3]) + 1):
                break
        print(linijka)
        outPlik.write(linijka + "\n")

    inPlik.close()
    outPlik.close()

else:
    print("Upewnij sie, ze wprowadzone argumenty sa poprawne!")

print("python", end=" ")
for arg in sys.argv:
    print(arg, end=" ")
