from model.model import Model
from database.DAO import DAO




listaCorretta= list()
listaDaCorreggere=DAO.getAllInteractions(5,11)
if len(listaDaCorreggere) > 0:
    # devo togliere le ripetizioni nella lista da correggere
    for c in listaDaCorreggere:
        if len(listaCorretta) == 0:
            listaCorretta.append(c)
        else:
            if c not in listaCorretta:
                listaCorretta.append(c)
    # ora ho le corrette coppie
    for speriamo in listaCorretta:
        print(speriamo)