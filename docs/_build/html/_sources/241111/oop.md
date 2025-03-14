# Objekt Orientierte Programmierung

Im bisherigen Unterricht wurden verschiedene Datenstrukturen vorgestellt sowie
einzelne Funktionen implementiert. Im folgenden wird es darum gehen, eigene
Datenstrukturen anzulegen und diese mit spezifischen Funktionen - man spricht in
diesem Zusammenhang von Methoden - zu versehen. Um Datenstrukturen und Methoden
zu kombinieren werden Klassen angelegt.

## Modellierung von Klassen

Klassen werden programmiert, um Objekte aus dem echten Leben abzubilden. Als
Beispiel soll hier eine Klasse zur Modellierung von Schülerinnen und Schülern
für eine Schule skizziert werden.  
Die für die Modellierung für die Schule wichtigen Eigenschaften sind die
erforderlichen Datenstrukturen und die Kontrolle der Bestehensvoraussetzungen
die Methoden.

Wichtige Eigenschaften neben den Personalien sind im Zusammenhang mit der
Schule die Noten und Absenzen. Die Bestehensvoraussetzungen werden mit einer
Methode Promotionsentscheid kontrolliert. Die Personalien können in einer
eigenen Klasse modelliert werden.

Wenn Klassen modelliert werden, können diese in der Entwurfsphase als
UML-Klassendiagramm graphisch dargestellt werden. Das obige Beispiel sieht dann
wie in der folgenden Grafik dargestellt aus.

![Beispiel UML-Klassendiagramm](beispiel.svg)

## Klassen in Python

Um eine Klasse in Python zu implementieren, kann ein eigenes Python File
angelegt werden (.py). Ein solches File hat für das Beispiel Personalien den
folgenden Inhalt:

```Python
# personalien.py

import datetime

class Personalien:
    def __init__(self, name : str, vorname : str, geburtsdatum : datetime.date):
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
```

Ein Klassenfile mit seinem (auskommentierten) Namen zu beginnen, erleichtert
später die Übersicht zu behalten.

Damit das Geburtsdatum als verarbeitbares Datum verwendet werden kann, wird als
erstes die Python Klasse datetime importiert. Dies ermöglicht es, die Klasse um
eine Methode `alter` zu ergänzen, welche das aktuelle Alter der modellierten
Person berechnet. Anschliessend folgt die
eigentliche Implementierung der Klasse Personalien.

`class` ist das Schlüsselwort um eine Klasse zu erstellen. Das Schlüsselwort
wird gefolgt vom Namen der Klasse. Dieser wird üblicherweise mit einem
Grossbuchstaben begonnen, ansonsten gelten die gleichen Regeln wie bei der
Vergabe von Namen für Variabeln.

Innerhalb der Klasse wird als erstes die von Python zur Verfügung gestellte
Methode `__init__` implementiert. Diese Methode wird auch als Konstruktor
bezeichnet. Sie ermöglicht es, eine konkrete Instanz - ein Objekt - der Klasse
Personalien anzulegen. Dazu werden ihr die Parameter self, name, vorname und
geburtsdatum übergeben. self bezieht sich dabei auf das neu zu erstellende
Objekt. Die Variabeln name, vorname und geburtsdatum sind das, was ihr Name
sagt. Die entsprechenden Werte werden in der Methode den jeweiligen Feldern des
Objekts zugewiesen.

Eine konkrete Person - ein Objekt in Python - wird folgendermassen angelegt:

```Python
geburtsdatum = datetime.date(2010, 11, 11)
mr_x = Personalien('Meier', 'Hans', geburtsdatum)
```