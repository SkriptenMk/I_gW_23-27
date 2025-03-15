# Die pandas Bibliothek

(Das Arbeitsblatt zu den pandas Series findet sich [hier](https://colab.research.google.com/github/I-gW-23-27/Skript/blob/main/docs/240916/timeline.ipynb).)

pandas ist eine Python Bibliothek zur Datenanalyse. Sie stellt die
beiden Datenstrukturen *Series* und *DataFrame* zur verfügung. Eine
pandas Series ist eine eindimensionale und ein pandas DataFrame eine
zweidimensionale Datenstruktur.

Damit mit diesen Datenstrukturen gearbeitet werden kann, muss pandas in
die Jupyter Notebooks importiert werden. Wie dies geht, wird im
folgenden dargestellt.

## Vorbereiten der Arbeitsumgebung

Die Anleitung für die Vorbereitung der Arbeitsumgebung gib es in zwei
Versionen. Eine Version für das Arbeiten mit Jupyter Notebooks in Google
Colab und eine Version für das Arbeiten auf dem eigenen Rechner.

### Arbeiten in Google Colab

Die Vorbereitung für die Arbeit in Google Colab ist denkbar einfach. Es
braucht nichts als das import-Statement in der ersten Code Zelle:

```python
import pandas as pd
```

Damit wird die pandas Bibliothek in das Notebook importiert und die
pandas Funktionen können mit `pd.funktion()` aufgerufen werden.

### Lokales Arbeiten auf dem eigenen Rechner

Um Konflikte zu vermeiden ist es gute Praxis, für jedes Python Projekt
eine virtuelle Arbeitsumgebung anzulegen. Dazu geht man Schrittweise
folgendermassen vor:

1. Einen Ordner für das neue Projekt anlegen.
2. Eine virtuelle Arbeitsumgebung anlegen. Dazu sind folgende Schritte
   abzuarbeiten: 
   1. Ein Terminal im Ordner öffnen.
   2. Den Befehl 
      
      ```shell
      ...\ihr_ordner>python -m venv venv
      ```

      eingeben.
3. Die virtuelle Arbeitsumgebung mit dem Befehl:
   
   ```shell
   ...\ihr_ordner>venv\Scripts\activate
   ```

   starten.

4. pandas und den Jupyter Server mit dem Befehl
   
   ```shell
   ...\ihr_ordner>python -m pip install pandas jupyter
   ```

   installieren. Das dauert ein Moment.

5. Jupyter Server mit

   ```shell
   ...\ihr_ordner>jupyter notebook
   ```

   starten. Dies öffnet ein Fenster in Ihrem Standardserver.

6. Im von Ihnen gewählten Notebook mit
   
   ```python
   import pandas as pd
   ```

   in der ersten Zelle pandas importieren.