from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_is_failo()

    def nuskaityti_is_failo(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_i_faila(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamas(self):
        suma = abs(float(input("Suma: ")))
        irasas = PajamuIrasas(suma)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def prideti_islaidas(self):
        suma = abs(float(input("Suma: ")))
        irasas = IslaiduIrasas(suma)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def atspaudinti_zurnala(self):
        print("------------------------")
        for irasas in self.zurnalas:
            print(irasas)
        print("------------------------")

    def atspausdinti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        print("Balansas:", balansas)
