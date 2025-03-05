import dictionary as di

d = di.Dictionary()


class Translator:
    def __init__(self):
        pass

    def printMenu(self):
        print("-------------------------------------\n"
              "   Translator Alien-Italian\n"
              "-------------------------------------\n"
              "1. Aggiungi nuova parola \n2. Cerca una traduzione \n3. Cerca con wildcard\n4. Stampa tutto il Dizionario\n5. Exit\n"
              "-------------------------------------\n")

    def loadDictionary(self, file):
        d.leggiDict(file)
        # dict is a string with the filename of the dictionary

    def handleAdd(self, entry):
        alfabeto = "abcdefghijklmnopqrstuvz"
        parola = entry[0].lower()
        for word in parola:
            if word not in alfabeto:
                return print(f"impossibile aggiungere la parola")
        if isinstance(entry[1], list):
            for traduzione in entry[1]:
                traduzione = traduzione.lower()
                for wo in traduzione:
                    if wo not in alfabeto:
                        return print(f"impossibile aggiungere la parola")
                d.addWord(parola, traduzione)
        elif isinstance(entry[1], str):
            traduzione = entry[1].lower()
            for wo in traduzione:
                if wo not in alfabeto:
                    return print(f"impossibile aggiungere la parola")
            d.addWord(parola, traduzione)
        print("Aggiunta!")

    def handleTranslate(self, query):
        alfabeto = "abcdefghijklmnopqrstuvz"
        for word in query:
            if word not in alfabeto:
                return print(f"impossibile cercare la parola, contiene un carattere invalido")
        return d.translate(query)
        # query is a string <parola_aliena>

    def handleWildCard(self, query):
        if query.count("?") > 1:
            return "troppe lettere mancanti"
        query = query.replace("?", ".")
        print(query)
        indice = query.find(".")
        print(indice)
        return d.translateWordWildCard(query,indice)

    def stampaDizionario(self):
        return d.stampaDizionario()
