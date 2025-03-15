# Python Dictionaries

Listen und Tupel sind praktische Datenstruktuen in Python um mehrere
Elemente in einem Objekt zu bündeln. Um auf ein einzelnes Element
zuzugreifen, weisen sie jedoch einen entscheidenden Nachteil auf. Man
muss wissen, an welcher Position sich das entsprechende Element in der
jeweiligen Liste bzw. im jeweiligen Tupel befindet.

An dieser Stelle kommen Python Dictionaries ins Spiel. In dieser
Datenstruktur können wie in Listen oder Tupel beliebige Datentypen
abgelegt werden. Im Gegensatz zu Listen und Tupeln erfolgt der Zugriff
auf die Inhalte allerdings nicht über einen Index, sondern über einen
Schlüssel. Dictinaries sind als *key* - *value* Paare angelegt.

```python
d = {
    key: value,
    key: value,
    ...
}
```

Ein konkretes Dictionary `person` mit den Schlüsseln `Vorname` und
`Familienname` sieht folgendermassen aus:

```python
person = {
    'Vorname': 'Hans',
    'Nachname': 'Muster',
}
```

Auf einen konkreten Wert kann via 'key' zugegriffen werden. Für das
Dictionary aus dem obigen Beispiel sieht das folgendermassen aus:

```python
>>>person['Vorname']
'Hans'
```

Python Dictionaries lassen nicht nur den Zugriff auf ein einzelnes
Element via 'key' zu. Es ist auch möglich, über ein Dictionary zu
iterieren. Ein Möglichkeit ist eine `for` Schleife. Am Beispiel des oben
erstellten Dictionary `person` sieht das folgendermassen aus:

```python
>>>for item in person:
...    print(f'{item}: {person[item]}')
Vorname: Hans
Nachname: Muster
```

Anwendungsübungen für verschiedene Operationen mit Dictionaries finden
sich in diesem [Arbeitsblatt](https://colab.research.google.com/github/I-gW-23-27/Skript/blob/main/docs/240909/dictionaries.ipynb).