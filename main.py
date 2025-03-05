import translator as tr

t = tr.Translator()
continua = True
while continua:
    t.printMenu()
    t.loadDictionary("dictionary.txt")

    txtIn = input()

    if int(txtIn) == 1:
        print(f"Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        riga = txtIn.split()
        parola = riga[0]
        riga.pop(0)
        traduzione = riga
        print(traduzione)
        t.handleAdd([parola, traduzione])
    elif int(txtIn) == 2:
        print(f"Ok, quale parola devo cercare?\n")
        txtIn = input()
        t.handleTranslate(txtIn)
    elif int(txtIn) == 3:
        print(f"Ok, quale parola devo cercare?\n")
        txtIn = input()
        print(t.handleWildCard(txtIn))

    elif int(txtIn) == 4:
        print(t.stampaDizionario())
    elif int(txtIn) == 5:
        continua = False
    else:
        print(f"opzione non valida")
