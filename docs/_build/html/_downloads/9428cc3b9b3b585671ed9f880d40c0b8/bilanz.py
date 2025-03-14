# bilanz.py
import pandas as pd

class Bilanz:
    def __init__(self, aktiven = {}, passiven = {}):
        self.aktiven  = aktiven
        self.passiven = passiven
        
      
                
        
    def get_verzinsliches_fk(self):
        '''
        Die Funktion get_verzinsliches_fk Filtert aus den Passiven das
        verzinsliche FK gemäss Kontenrahmen KMU aus und gibt die addierten Saldi
        zurück.
        
        Rückgabewert:
            float: Die Summe der Saldi des verzinslichen Fremdkapitals.
        '''
        verzinsliches_fk = {}
        for kto_nr, konto in self.passiven.items():
            if kto_nr >= 2400 and kto_nr < 2500:
                verzinsliches_fk[kto_nr] = konto
                
                      
        total_verzinsliches_fk = 0
        
        for kto_nr, konto in verzinsliches_fk.items():
            total_verzinsliches_fk += konto[1]
        
        return total_verzinsliches_fk
    
    def get_ek(self):
        '''
        Die Funktion get_ek Filtert aus den Passiven gemäss Kontentrahmen KMU
        das EK und gibt die addierten Saldi der entsprechenden Konti zurück.
        
        Rückgabewert:
            float: Die Summe der Saldi des Eigenkapitals.
        '''
        ek = {}
        for kto_nr, konto in self.passiven.items():
            if kto_nr >= 2800 and kto_nr < 3000:
                ek[kto_nr] = konto
        
        total_ek = 0
        
        for kto_nr, konto in ek.items():
            total_ek += konto[1]
            
        return total_ek
    
    def get_gk(self):
        '''
        Methode zur Berechnung des Gesamtkapitals.
        
        Rückgabewert:
            float: Die Summe der Saldi der gesammten Passiven.
        '''
        
        gk = 0
        
        for konto in self.passiven.values():
            gk += konto[1]
            
        return gk