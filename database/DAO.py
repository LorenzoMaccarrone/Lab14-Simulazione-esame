from database.DB_connect import DBConnect
from model.cromosoma import Cromosoma
from model.interaction import Interaction


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(g.Chromosome)
                    from genes g 
                    where g.Chromosome >0"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["Chromosome"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from genes g """

        cursor.execute(query, )

        for row in cursor:
            result.append(Cromosoma(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllInteractions(c1, c2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.Chromosome as c1, g2.Chromosome as c2, i.GeneID1 ,i.GeneID2 , i.Expression_Corr 
                    from interactions i, genes g , genes g2 
                    where i.GeneID1 = g.GeneID
                    and i.GeneID2 = g2.GeneID 
                    and g.Chromosome != g2.Chromosome 
                    and i.GeneID1 != i.GeneID2 
                    and g.Chromosome=%s
                    and g2.Chromosome=%s
                    group by i.GeneID1 , i.GeneID2
                                        """
        #l'errore per cui ho perso molto tempo è stato aver scritto i.GeneID1<i.GeneID2, ma così
        #andiamo a perdere tutte qulle coppie di geni valide in cui GeneID1 è maggiore di GeneID2
        #Quindi la cosa giusta da fare era garantire che fossero diversi l'uno dall'altro e non uno minore
        #dell'altro. Con il mio approccio precedente perdevamo una parte della soluzione
        cursor.execute(query, (c1, c2) )

        for row in cursor:
            result.append(Interaction(**row))

        cursor.close()
        conn.close()
        return result
