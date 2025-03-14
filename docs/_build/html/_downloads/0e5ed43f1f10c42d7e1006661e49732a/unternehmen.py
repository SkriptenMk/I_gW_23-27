# unternehmen.py

from bilanz import Bilanz
from erfolgsrechnung import Erfolgsrechnung

class Unternehmen:
    def __init__(self, bilanz, erfolgsrechnung) -> None:
        self.bilanz = bilanz
        self.erfolgsrechnung = erfolgsrechnung
        
    def get_roi(self) -> float:
        '''
        Methode zur Berehchnung der Gesamtkapitalrentabilität (RoI, return on investment).
        
        Rückgabewert:
            float: Gibt den RoI in Prozenten zurück.
        '''
        gk = self.bilanz.get_gk()
        ebit = self.erfolgsrechnung.get_ebit()
        
        return (ebit / gk) * 100
    
    def get_fk_zinssatz(self):
        '''
        Methode zur Berechnung des akutellen durchschnittlichen Zinsatzes auf dem FK.
        
        Rückgabewert:
            float: Gibt den durchschnittlich bezahlten Zinssatz in Prozenten zurück.
        '''
        zinsaufwand = self.erfolgsrechnung.get_zinsaufwand()
        verzinsliches_fk = self.bilanz.get_verzinsliches_fk()
        
        return (zinsaufwand / verzinsliches_fk) * 100
    
    def leverage_effekt(self, fk: float, fk_zinssatz: float) -> bool:
        '''
        Prüft, ob bei einer Erhöhung des Fremdkapitals (FK) der Leverage-Effekt ausgenutzt werden kann.

        Diese Methode berechnet den durchschnittlichen Zinssatz nach einer Kapitalerhöhung 
        und vergleicht ihn mit der Rendite (ROI) des Unternehmens. Der Leverage-Effekt 
        kann ausgenutzt werden, wenn die Rendite höher ist als der durchschnittliche Zinssatz 
        des gesamten Fremdkapitals.

        Eingabewerte:
            fk (float): Der Betrag des zusätzlich aufgenommenen Fremdkapitals.
            fk_zinssatz (float): Der Zinssatz des zusätzlich aufgenommenen Fremdkapitals.

        Rückgabewert:
            bool: Gibt zurück, ob der Leverage-Effekt ausgenutzt werden kann (True) 
                oder nicht (False).
        '''
        fk_alt = self.bilanz.get_verzinsliches_fk()
        fk_zinssatz_alt = self.get_fk_zinssatz()
        fk_neu = fk
        fk_zinssatz_neu = fk_zinssatz
        
        mittleren_fk_zinssatz_nach_kapitalerhoehung = ((fk_alt * fk_zinssatz_alt) + (fk_neu * fk_zinssatz_neu)) / (fk_alt + fk_neu)
        roi = self.get_roi()
        
        return roi > mittleren_fk_zinssatz_nach_kapitalerhoehung
        