# File Handling in Python

Bisher wurden die verarbeiteten Daten immer direkt in den zu Übungszwecken
erstellten Jupyter Notebooks abgelegt. Dies ist nicht immer Hilfreich. Python
stellt daher Möglichkeiten zur Verfügung, Files zu lesen und zu Schreiben.

Mit der `open()` Funktion stellt Python eine Möglichkeit zur Verfügung, Daten
von einem File zu lesen und sie in ein File zu schreiben.  
Um Daten in ein File zu schreiben, wird die `open()` Funktion folgendermassen
verwendet:

```Python
with open('file.txt', 'w') as myfile:
    myfile.write('text')
```

Das Listing macht der Reihe nach folgendes:

* `with` stellt sicher, dass das geöffnete File auch im Falle eines Fehlers im
  Programm korrekt geschlossen wird.
* `open` öffnet das File, welches mit Pfad in der Klammer identifiziert wird.
  Das File muss dabei noch nicht bestehen. Wenn es schon besteht wird es mit dem
  Attribut `'w'` überschrieben. Wenn es ergänzt werden soll, muss das Attribut
  `'a'` verwendet werden.
* `as myfile` ermöglicht es, innerhalb des Python Programmes einen frei
  gewählten Namen für das geöffnete File zu verwenden.
* `myfile.write(...)` schreibt den Inhalt in der Klammer in das geöffnete File.

Um Daten aus einem File zu lesen, wird die `open()` Funktion wie im folgenden
Listing dargestellt verwendet:

```Python
with open('file.txt', 'r') as myfile:
    inhalt = myfile.read()
    print(inhalt)
```

Der Reihe nach, was beim Lesen anders ist als beim Schreiben:

* `open` erhält neben dem Pfad zum File das Attribut `r` für *read*.
* `inhalt = myfile.read()` weist den ausgelesenen Inhalt der Variabeln `inhalt` zu.

Falls der Inhalt der Datei zeilenweise gelesen werden soll, kann der Code
folgendermassen abgeändert werden:

```Python
with open('file.txt', 'r') as myfile:
    for zeile in myfile:
        print(zeile)
```

Für die Berechnung betriebswirtschaftlicher Kennzahlen, liegen die Daten oft in
Form von .csv Dateien vor. Da es sich dabei um eine generell häufig verwendetes
Dateiformat handelt, stellt Python mit der csv-Library eine Library zur
Verfügung, welche besonders gut mit den Eigenheiten dieses Dateiformates umgehen
kann.

Die csv-Library muss allerdings zuerst mit `import csv` importiert werden.

Nachdem die csv-Library importiert ist, kann beispielsweise ein Dictionary in
ein .csv File geschrieben werden.

```Python
beispiel_dictionary = {
    'Mue': ['Müller', 'Anton', 'Rektor'],
    'Hub': ['Huber', 'Vreni', 'Prorektorin']
}
```

Dieses `beispiel_dictionary` wird folgendermassen in ein .csv File geschrieben:

```Python
with open('schulleitung.csv', 'w', newline='') as destination:
    destinationwriter = csv.writer(destination)
    for key, value in beispiel_dictionary.items():
        tmp = [key, value[0], value[1], value[2]]
        destinationwriter.writerow(tmp)
```

Dabei übernehmen die einzelnen Zeilen im Listing die folgenden Aufgaben:

* `with open('schulleitung.csv', 'w', newline='') as destination:` leistet das
  gleiche, wie oben.
* `destinationwriter = csv.writer(destination)` legt für die Funktion
  `csv.writer()` einen Namen fest damit diese weiter unten im Code verwendet
  werden kann. Es wäre auch möglich gewesen in der letzten Zeile
  `csv.writer(destination).writerow(tmp)` zu schreiben.
* Mit dem `for`-Loop wird über das Dictionary iteriert.
* Die einzelnen Elemente eines jeden Eintrags des Dictionary werden in eine
  temporäre Liste `tmp` geschrieben.
* Mit `destinationwriter.writerow(tmp)` werden die Listen ins .csv File geschrieben.

Falls ein .csv File gelesen werden soll, ist folgendermassen vorzugehen:

```Python
with open('schulleitung.csv', 'r') as source:
    reader = csv.reader(source, delimiter=',')
    for line in reader:
        print(line)
```

Dabei kann mit den Zeilen selbstverständlich auch etwas anderes gemacht werden,
als sie anzuzeigen. Zu beachten ist, dass jede Zeile des .csv Files eine Liste
mit Strings ist.