# Refactoring

Programmieren dient im wesentlichen der Automatisierung repetitiver Tätigkeiten.
Dies soll auch beim Programmiren selber berücksichtigt werden. Aus diesem Grund
sind Wiederholungen in Programmen zu vermeiden (don't repeat yourself, DRY).  
Dieser Grundsatz hilft dabei, Computerprogramme einfacher überarbeiten zu
können. Wenn eine Funktionalität in einem Programm durch 'Copy Paste' an
verschiedenen Stellen wiederverwendet wird und diese Funktionalität verändert
werden soll, besteht das Risiko, dass nicht alle Kopien überarbeitet werden und
das Programm dadurch fehlerhaft wird.

Wenn ein Programm mit neuen Funktionalitäten versehen wird, kann es sein, dass
diese Funktionalität zuerst nur einem Teil des Programms zur Verfügung gestellt
wird und erst wenn sie erfolgreich getestet worden ist für das ganze Programm
implementiert wird. Ein Beispiel dafür ist das Programm zum Leverage Effekt.
Dort wurde der Import von Kontendaten aus einem CSV-File zuerst nur für die
Bilanz implementiert. Erst als das Funktioniert hat, wurde die Funktionalität
auf der Ebene Unternehmen und somit für Bilanz und Erfolgsrechnung zur Verfügung
gestellt. Dabei wurden ausserdem Wiederholungen eliminiert.

Die Vorgehensweise kann als 'Code aufräumen' umschrieben werden. Der
Fachausdruck dafür ist Refactoring.