# Datenvisualisierung

In dieser Unterrichtssequenz geht es darum, eine Liste mit Noten in
geeigneter Form graphisch darzustellen. Ein vorbereiteter 
[Datensatz](data/notenliste.csv)
findet sich im Ordner `data`.

Um die Daten visualisieren zu können, ist als erstes die entsprechende
Arbeitsumgebung vorzubereiten.

1. Ordner Anlegen
   
   Vorschlag für die Benennung: `YYMMDD_stichwort`

2. Python Virtual Environment anlegen
   
   ```shell
   python -m venv venv
   ```
3. Python Virtual Environment aktivieren
   
   ```shell
   venv\Scripts\activate
   ```
4. Erforderliche Pakete installieren (jupyter, pandas, matplotlib)
   
   ```shell
   python -m pip install jupyter pandas matplotlib
   ```
5. Jupyter Server starten
6. Neues Notebook anlegen

Im neuen Notebook sind als erstes die erforderlichen Pakete zu
importieren.

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Die Daten aus der Notenliste werden in einem pandas Dataframe verfügbar
gemacht:

```python
df = pd.read_csv('Pfad/zur/Datei.csv')
```

Die unter `df` verfügbar gemachten Daten können dann als Histogramm
visualisiert werden:

```python
plt.figure()

plt.hist(df['Spaltentitel'])

plt.title('Titel')
plt.xlabel('Beschriftung der x-Achse')
plt.ylabel('Beschriftung der y-Achse')

plt.show()
```

Alternativ können die Noten auch in einem Boxplot visualisiert werden:

```python
plt.figure()

plt.boxplot(df['Spaltentitel']),
            vert=False,
            patch_artist=True, # ermöglicht Beeinflussung der Darstellung
            medianprops=dict(color='red'), # Darstellung der Medianlinie
            boxprops=dict(facecolor='powderblue'), # Darstellung der Box
            )
plt.gca().yaxis.set_visible(False) # unterdrückt die y-Achse

plt.title('Titel')
plt.xlabel('Beschriftung der x-Achse')

plt.show()
```

Für die Verwendung der Grafik in einem anderen Dokument kann sie mit
`plt.savefig('Pfad/zur/Datei.fte')` abgespeichert werden (`.fte` steht
für File Type Extension).