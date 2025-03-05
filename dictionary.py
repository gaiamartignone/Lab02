class Dictionary:
    def __init__(self):
        self.parole = {}

    def leggiDict(self, leggi):
        with open(leggi, "r") as f:
            riga = f.readline()  # Legge la prima riga
            while riga:
                riga = riga.replace("\n", "").split(" ")
                self.parole[riga[0]] = [riga[1]]
                riga = f.readline()

    def addWord(self, parola, traduzione):
        if self.parole.get(parola) is not None:
            self.parole[parola].append(traduzione)
        else:
            self.parole[parola] = [traduzione]

    def translate(self, parola):
        if self.parole.get(parola) is not None:
            print(self.parole.get(parola))
        else:
            print("Parola non esistente!")

    def translateWordWildCard(self, word, indice):
        temp = []
        for key in self.parole:
            nuova = key[:indice] + "." + key[indice+1:]
            print(f"{nuova}-{word}")
            if word == nuova:
                temp.__add__(self.parole.get(key))
        return temp

    def stampaDizionario(self):
        str = ""
        for key in self.parole:
            str += key + "-->"
            for value in self.parole.get(key):
                str += value + " "
            str += "\n"
        return str
