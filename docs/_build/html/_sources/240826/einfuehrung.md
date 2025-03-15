# Die Datenstruktur Python-Liste

Zu Beginn müssen ein paar Begrifflichkeiten geklärt werden. In der
Informatik wird generell zwischen den Datenstrukturen *Array* und
*Liste* unterschieden.  
Ein *Array* ist grundsätzlich eine Datenstruktur in welcher eine *fixe*
Anzahl Elemente des *gleichen Datentyps* abgespeichert werden. *Arrays*
werden in der Regel in einem zusammenhängenden Speicherbereich abgelegt.
In einem *Array* ist es möglich, auf jedes Element direkt zuzugreifen.    
*Listen* werden oft als *verkettete Listen* implementiert. In einer
solchen Datenstruktur kann eine *bliebige* Anzahl von Elementen des
*gleichen Datentyps*
abgespeichert werden. In einer *verketteten Liste* findet sich bei jedem
Element ein Verweis auf den Speicherplatz des nächsten Elements. Um in
einer *Liste* auf ein Element zuzugreifen, muss die Liste vom ersten bis
zum gesuchten Element durchlaufen werden.  
Der Zugriff auf die Daten in einem *Array* ist schneller als in einer
*verketteten Liste*, dafür ist das Einfügen neuer Elemente in einer
*verketteten Liste* einfacher als in einem (vollen) *Array*.

In Pyhton ist eine Liste eine Datenstruktur, welche Eigenschaften der
beiden beschriebenen Datenstrukturen kombiniert. Die Genaue Bezeichnung
für Listen in Python müsste eigentlich *dynamisches Array* lauten. In
einer Python-Liste können *bliebig viele* Elemente *unterschiedlicher Datentypen*
abgespeichert werden. Trotzdem ist der direkte Zugriff auf jedes dieser
Elemente möglich. Diese Flexibilität verursacht allerdings einen
erheblichen zusätlichen Speicherbedarf für Python-Listen.

[Hier findet sich ein Arbeitsblatt](listen.ipynb) 
mit Aufgaben zum Erstellen und Bearbeiten von Python-Listen. 