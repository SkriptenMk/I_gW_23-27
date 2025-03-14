# erfolgsrechnung.py
import pandas as pd

class Erfolgsrechnung:
    def __init__(self, ertrag = {}, aufwand = {}) -> None:
        self.ertrag = ertrag
        self.aufwand = aufwand
        self.zinsaufwand = None
        
    def get_betrieblicher_ertrag(self):
        betrieblicher_ertrag = 0
        
        for kto_nr, konto in self.ertrag.items():
            if kto_nr >= 3000 and kto_nr < 4000:
                betrieblicher_ertrag += konto[1]
                
        return betrieblicher_ertrag

    
    def get_bruttoergebnis(self):        
        bruttoergebnis = self.get_betrieblicher_ertrag()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 4000 and kto_nr < 5000:
                bruttoergebnis -= konto[1]
                
        return bruttoergebnis
        
    
    def get_bruttoergebnis_inkl_personal(self):
        bruttoergebnis_inkl_personal = self.get_bruttoergebnis()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 5000 and kto_nr < 6000:
                bruttoergebnis_inkl_personal -= konto[1]
                
        return bruttoergebnis_inkl_personal
    
    
    def get_ebitda(self):
        ebitda = self.get_bruttoergebnis_inkl_personal()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 6000 and kto_nr < 6800:
                ebitda -= konto[1]
                
        return ebitda

        
    def get_ebit(self):
        ebit = self.get_ebitda()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 6800 and kto_nr < 6900:
                ebit -= konto[1]
                            
        return ebit
    
    
    def get_ebt(self):
        ebt = self.get_ebit()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 6900 and kto_nr < 6950:
                ebt -= konto[1]
            elif kto_nr >= 6950 and kto_nr < 7000:
                ebt += konto[1]
                
        return ebt
            
    
    def get_erfolg_vor_steuern(self):
        erfolg_for_steuern = self.get_ebt()
        
        for kto_nr, konto in self.aufwand.items():
            if (kto_nr >= 7000 and kto_nr < 7010 or # Etrag Nebenbetrieb
                kto_nr >= 7500 and kto_nr < 7510 or # Etrag betriebliche Liegenschaft
                kto_nr >= 8100 and kto_nr < 8500 or # Betriebsfremder Ertrag
                kto_nr >= 8510 and kto_nr < 8900):  # Ausserordentlicher, einmaliger oder periodenfremder Ertrag
                
                erfolg_for_steuern += konto[1]
                
            elif (kto_nr >= 7010 and kto_nr < 7500 or # Aufwand Nebenbetrieb
                  kto_nr >= 7510 and kto_nr < 8100 or # Aufwand betriebliche Liegenschaft & Betriebsfremder Aufwand
                  kto_nr >= 8500 and kto_nr < 8900):  # Ausserordentlicher, einmaliger oder periondenfremder Aufwand
                
                erfolg_for_steuern -= konto[1]
                
        return erfolg_for_steuern
                
    
    def get_erfolg(self):
        erfolg = self.get_erfolg_vor_steuern()
        
        for kto_nr, konto in self.aufwand.items():
            if kto_nr >= 8900 and kto_nr < 9200:
                erfolg -= konto[1]
                
        return erfolg
        
            
    def get_zinsaufwand(self):
        if self.zinsaufwand == None:
            zinsaufwand = self.aufwand[6900][1]
            self.zinsaufwand = zinsaufwand
            return zinsaufwand
        else:
            return self.zinsaufwand
    
    def set_zinsaufwand(self, zinsaufwand):
        self.zinsaufwand = zinsaufwand