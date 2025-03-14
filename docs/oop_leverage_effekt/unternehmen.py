# unternehmen.py

import csv
import pandas as pd

from bilanz import Bilanz
from erfolgsrechnung import Erfolgsrechnung

class Unternehmen:
    def __init__(self, konti = {}) -> None:
        if len(konti) == 0:
            self.bilanz = Bilanz()
            self.erfolgsrechnung = Erfolgsrechnung()
        else:
            self.bilanz = Bilanz()
            self.erfolgsrechnung = Erfolgsrechnung()
            self.set_konti(konti)
                    
        
    def berechne_fk_zinssatz(self):
        '''
        Methode zur Berechnung des durchscnittlichen Fremdkapitalzinssatzes.
        
        Rückgabewert:
            float: Durschnittlicher Zinssatz auf dem verzinslichen FK in Prozenten.
        '''
        verzinsliches_fk = self.bilanz.get_verzinsliches_fk()
        zinsaufwand = self.erfolgsrechnung.get_zinsaufwand()
        return (zinsaufwand/verzinsliches_fk) * 100
    
    def berechne_roi(self):
        '''
        Methode zur Berechnung des RoI.
        
        Rückgabewert:
            float: RoI in Prozenten.
        '''
        ebit = self.erfolgsrechnung.get_ebit()
        gk = self.bilanz.get_gk()
        
        return (ebit/gk) * 100
    
    def berechne_roe(self):
        '''
        Methode zur Berechnung des RoE.
        
        Rückgabewert:
            float: RoE in Prozenten.
        '''
        ek = self.bilanz.get_ek()
        erfolg = self.erfolgsrechnung.get_erfolg()
        
        return (erfolg/ek) * 100
    
    def set_konti(self, konti):
        if isinstance(konti, pd.DataFrame):
            self._set_konti_from_dataframe(konti)
        elif isinstance(konti, str):
            df = pd.read_csv(konti, index_col=0)
            self._set_konti_from_dataframe(df)
        elif isinstance(konti, dict):
            self._set_konti_from_dict(konti)
                    
    def _set_konti_from_dataframe(self, df):
        for index, row in df.iterrows():
            if index >= 1000 and index < 2000:
                self.bilanz.aktiven[index] = [row['Kto'], row['Saldo']]
            elif index >= 2000 and index < 3000:
                self.bilanz.passiven[index] = [row['Kto'], row['Saldo']]
            elif index >= 3000 and index < 4000:
                self.erfolgsrechnung.ertrag[index] = [row['Kto'], row['Saldo']]
            elif index >= 4000 and index < 9900:
                self.erfolgsrechnung.aufwand[index] = [row['Kto'], row['Saldo']]  
                
    def _set_konti_from_dict(self, konti):
        for ktonr, kto in konti.items():  
            if ktonr >= 1000 and ktonr < 2000:
                self.bilanz.aktiven[ktonr] = [kto[0], kto[1]]
            elif ktonr >= 2000 and ktonr < 3000:
                self.bilanz.passiven[ktonr] = [kto[0], kto[1]]
            elif ktonr >= 3000 and ktonr < 4000:
                self.erfolgsrechnung.ertrag[ktonr] = [kto[0], kto[1]]
            elif ktonr >= 4000 and ktonr < 9900:
                self.erfolgsrechnung.aufwand[ktonr] = [kto[0], kto[1]]    


    
    def save_data(self):
        with open('data.csv', mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)  # Übergabe des Dateiobjekts an csv.writer
            
            # Kopfzeile schreiben
            writer.writerow(['KtoNr', 'Kto', 'Saldo'])
            
            # Daten schreiben
            for ktonr, kto in self.bilanz.aktiven.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            for ktonr, kto in self.bilanz.passiven.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            for ktonr, kto in self.erfolgsrechnung.aufwand.items():
                writer.writerow([ktonr, kto[0], kto[1]])
            
            for ktonr, kto in self.erfolgsrechnung.ertrag.items():
                writer.writerow([ktonr, kto[0], kto[1]])
                
            