import sys

for i, arg in enumerate(sys.argv):
    print(f'{i}: {arg}')

if (sys.argv[1] == "saldo"):
    try:

        if (len(sys.argv) == 3):  # Jeżeli wywołanie ma strukturę: python accountant.py saldo in.txt
            inPlik = open(sys.argv[2], 'r')
            outPlik = open("out.txt", 'w')

            suma = 0
            sumowanie = False
            linijki = inPlik.readlines()
            print(linijki)
            for linijka in linijki:
                print(linijka)
                if (len(linijka) > 0 and linijka != '\n'):
                    if (linijka == "saldo"):
                        sumowanie = True
                    if (sumowanie == True):
                        print(f'Zapisuję: {linijka}')
                        suma += int(linijka)
            outPlik.write(str(suma))

            outPlik.close()
            inPlik.close()

        elif (len(sys.argv) == 5):
            inPlik = open(sys.argv[5])

            for linijka in inPlik:
                outPlik.write(linijka)

            outPlik.write(sys.argv[2] + '\n' + sys.argv[3])
    except:
        print(f'Wystąpił błąd! Upewnij się, że podane argumenty ({sys.argv}) zostały wpisane poprawnie.')