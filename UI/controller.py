import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler

    def mostra_automobili(self, e):
        self._view.lista_auto.controls.clear()
        automobili = self._model.get_automobili()

        if automobili:
            for auto in automobili:
                self._view.lista_auto.controls.append(ft.Text(str(auto)))
        else:
            self._view.lista_auto.controls.append(ft.Text("Nessuna automobie presente."))
        self._view.update()


    def mostra_automobili_per_modello (self, e) :
        self._view.lista_auto_ricerca.controls.clear ()
        modello = self._view.input_modello_auto.value

        if modello == "" :
            self._view.lista_auto_ricerca.controls.append (ft.Text ("Inserire un modello da cercare."))
            self._view.update ()
            return

        automobili_per_modello  = self._model.cerca_automobili_per_modello(modello)
        if automobili_per_modello :
            for auto in automobili_per_modello :
                self._view.lista_auto_ricerca.controls.append (ft.Text (str (auto)))
        else :
            self._view.lista_auto_ricerca.controls.append (ft.Text (f"Nessuna auto trovata per il modello: {modello}"))

        self._view.input_modello_auto.value = None
        self._view.update ()



