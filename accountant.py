import sys

balance = 0
change = 0
magazyn = {}
data = []
account = {"balance": balance}


while True:
    action = input().strip()                       # WYWOŁANIE: python <nazwa_programu> saldo <plik_wejsciowy>
    if action == "saldo":
        change = int(input())
        comment = str(input())
        if balance + change < 0:
            print("error")
            break
        balance += change
        account["balance"] =+ balance
        data.append(["saldo", change, comment])

    elif action == "zakup":               # WYWOŁANIE: python <nazwa_programu> zakup <plik_wejsciowy>
        item_id = str(input())
        price = int(input())
        quantity = int(input())
        if (price * quantity) < account["balance"]:
            balance =- price * quantity
            account["balance"] += balance
            if item_id in magazyn:
                magazyn[item_id] += quantity
            else:
                magazyn[item_id] = quantity
            data.append(["zakup", item_id, price, quantity])
        if price < 0 or quantity <= 0:
            print("Nieprawidłowe wartości.")
            break

    elif action == "sprzedaz":
        item_id = str(input())
        price = int(input())
        quantity = int(input())
        if item_id in magazyn:
            magazyn[item_id] -= quantity
            balance = + price * quantity
            account["balance"] += balance
            data.append(["sprzedaz", item_id, price, quantity])
        elif item_id not in magazyn:
            print("Pusty magazyn")
            break

    elif action == "stop":
        break


if sys.argv[1] == "sprzedaz":                     # WYWOŁANIE: python <nazwa_programu> sprzedaz <plik_wejsciowy>
    item_id = sys.argv[2]
    price = int(sys.argv[3])
    quantity = int(sys.argv[4])
    if item_id in magazyn:
        balance = + price * quantity
        account["balance"] += balance
        data.append([sys.argv[1], item_id, price, quantity])
        magazyn[item_id] -= ilosc
    else:
        print("Brak towaru")
    for list in data:
        for item in list:
            print(item)
    print("stop")

if sys.argv[1] == "zakup":
    item_id = sys.argv[2]
    price = int(sys.argv[3])
    quantity = int(sys.argv[4])
    if (price * quantity) < account["balance"]:
        balance = - price * quantity
        account["balance"] += balance
        if item_id in magazyn:
            magazyn[item_id] += quantity
        else:
            magazyn[item_id] = quantity
        data.append(["zakup", item_id, price, quantity])
    if price < 0 or quantity <= 0:
        print("Nieprawidłowe wartości.")
    for list in data:
        for item in list:
            print(item)
    print("stop")

if sys.argv[1] == "magazyn":                    # WYWOŁANIE: python <nazwa_programu> magazyn <plik_wejsciowy>
    item_id = str(sys.argv[4])
    quantity = 0
    if item_id not in magazyn:
        magazyn[item_id] = ilosc
    if item_id in magazyn:
        for produkt, quantity in magazyn.items():
            print("{}: {}".format(produkt, quantity))


if sys.argv[1] == "przeglad":
    start = 0
    end = 0
    if len(sys.argv) > 2:
        start = sys.argv[2]
        koniec = sys.argv[3]
    for list in data[int(start):int(end)]:
        for item in list:
            print(item)
    print("stop")

                                                # WYWOŁANIE: python <nazwa_programu> balance <plik_wejsciowy>
if sys.argv[1] == "saldo":
    print(account["balance"])

if sys.argv[1] == "balance":
    print(account["balance"])

