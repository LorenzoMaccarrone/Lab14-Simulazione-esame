import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {self._model.getNumNodi()} "
                    f"Numero di archi:{self._model.getNumArchi()}"))
        self._view.txt_result.controls.append(
            ft.Text(f"Informazioni sui pesi degli archi: arco con valore minimo {self._model.getValMin()} "
                    f"arco con valore massimo: {self._model.getValMax()}"))
        self._view.btn_countedges.disabled= False
        self._view.update_page()


    def handle_countedges(self, e):
        if self._view.txt_name.value == "":
            self._view.create_alert("Inserire soglia")
            self._view.update_page()
            return
        nStr = self._view.txt_name.value

        try:
            nFlt = float(nStr)
        except ValueError:
            self._view.create_alert("Il valore inserito nel campo soglia non è un float.")
            self._view.update_page()
            return
        min=self._model.getValMin()
        max=self._model.getValMax()
        print(nFlt)
        if nFlt> max or nFlt< min:
            self._view.create_alert("Il valore inserito non è nei limiti")
            return
        self._view.update_page()
        archiMinori=self._model.archiMinori(nFlt)
        archiMaggiori=self._model.archiMaggiori(nFlt)
        self._view.txt_result2.controls.append(
            ft.Text(f"Numero di archi con peso minore della soglia:{archiMinori}"))
        self._view.txt_result2.controls.append(
            ft.Text(f"Numero di archi con peso maggiore della soglia:{archiMaggiori}"))
        self._view.update_page()




    def handle_search(self, e):
        pass