# Einführung in Computernetzwerke

Computernetzwerke ermöglichen die Kommunikation zwischen Computern. In dieser
Unterrichtseinheit soll gezeigt werden, wie das technisch funktioniert.

Um die Bedeutung dieser technischen Grundlagen für die Gesellschaft aufzuzeigen,
sei hier auf ein Artikel aus der 
[NZZ vom 24. Oktober 2022](wie-china-unter-xi-das-internet-kontrolliert-ld.html) 
zur Zensur des
Internets in China verwiesen.

## OSI Layer Modell

Das OSI (Open System Interconnection) Modell ermöglicht es, die Kommunikation
über verschiedene technische Systeme hinweg zu beschreiben. Dieses theoretische
Modell beschreibt sieben Schichten (Layer) der Kommunikation. Die unterste
Schicht beschäftigt sich mit der Ebene der physikalischen Verbindung, die
oberste mit der Kommunikation innerhalb einer spezifischen Anwendung. Eine
detaillierte Beschreibung der einzelnen Schichten findet sich im entsprechenden
[Eintrag der Wikipedia](https://de.wikipedia.org/wiki/OSI-Modell).

## Das TCP/IP Protokoll

Vom OSI Layer Modell werden technisch nicht alle Ebenen umgesetzt. Durchgesetzt
hat sich das 
[TCP/IP
Referenzmodell](https://de.wikipedia.org/wiki/Internetprotokollfamilie#TCP/IP-Referenzmodell)
(Transmission Control Protocol/Internet Protocol). Dieses benutzt lediglich vier
der im OSI Modell beschriebenen Schichten. Eine Netzwerkschicht für die
physikalische Verbindung, eine Internetschicht für die Vermittlung zwischen den
Computern, eine Transportschicht für die eigentliche Übermittlung der Daten
sowie eine Anwendungsschicht für die Auslieferung der Daten an die konkrete
Anwendung auf dem Computer.

## IP Adressen

Aktuell soll hier vor Allem die Internetschicht betrachtet werden. Ausgangspunkt
für die entsprechenden Beobachtungen ist dabei die IP-Adresse. IP-Adressen geben
jedem mit einem Computernetzwerk verbundenen Computer eine eindeutige Adresse.
Über diese Adresse ist der Computer im Netzwerk erreichbar.

Aktuell bestehen zwei Versionen von IP-Adressen nebeneinander - IPv4- und
IPv6-Adressen. Eigentlich sollten die IPv6-Adressen die IPv4-Adressen ablösen.
Dieser Prozess geht allerdings nur sehr langsam vonstatten. Daher muss man sich
derzeit mit beiden Versionen der IP-Adressen auseinandersetzten.

### IPv4

IPv4-Adressen bestehen aus 32 Bits und werden in der Form 255.255.255.255
dargestellt. Das ergibt total $2^{32} = 4'294'967'296$ Adressen. 

Knapp 4.3 Mia Adressen reichen nicht aus, damit alle mit dem Internet
verbundenen Rechner erreicht werden können. Um dieses Problem zu adressieren
wurde einerseits die Adressierung mit IPv6-Adressen begonnen und andererseits
innerhalb der IPv4-Adressen zwei Tricks angewendet.

Der erste Trick im Adressraum von IPv4 ist die vergabe dynamischer
IPv4-Adressen. Das bedeutet, dass die Internetanbieter eine IPv4-Adresse
mehreren Kunden gleichzeitig zuteilen. Der Anbieter ist bei diesem Verfahren
dafür verantwortlich, den Überblick zu behalten, welcher Rechner gerade unter
welcher Adresse erreichbar ist.

Der zweite Trick besteht in der Aufteilung der IPv4-Adressen in öffentliche und
private Adressen. Dabei wird das Netzwerk in Subnetzwerke unterteilt. Das
Subnetzwerk als ganzes wird dabei unter einer öffentlichen IPv4-Adresse
erreicht. Innerhalb des Subnetzwerkes werden dann private Adressen vergeben.
Diese sind aus dem Internet nicht direkt erreichbar. Das
macht es theoretisch möglich, zu jeder öffentlichen Adresse nochmals alle
privaten Adressen zu vergeben. Dies erhöht die Zahl verfügbarer Adressen
deutlich. 

Die privaten Interessen sind die drei
Blöcke

* 10.0.0.0 – 10.255.255.255
* 172.16.0.0 – 172.31.255.255
* 192.168.0.0 – 192.168.255.255.

Alle anderen Adressen sind öffentliche Adressen.

### IPv6

Diese (neueren) Adressen bestehen aus 128 Bits und werden 
[hexadezimal](https://de.wikipedia.org/wiki/Hexadezimalsystem)
dargestellt. Eine IPv6-Adresse hat für die Darstellung das Format 
2001:0db8:85a3:0000:0000:8a2e:0370:7344.

Insgesamt stehen $2^{128}$, eine Zahl mit 39 Stellen, IPv6-Adressen zur
Verfügung.

Die Umstellung auf IPv6 wird noch einige Zeit in Anspruch nehmen.

## Domain Name System

Für den Endnutzer sind IP-Adressen - weder IPv4 und schon gar nicht IPv6 - kaum
direkt zu nutzen. Um dies zu umgehen wird eine dezentrale Datenbank betrieben,
welche die Übersetzung von
[URL](https://de.wikipedia.org/wiki/Uniform_Resource_Locator),
wie zum Beispiel www.kbw.ch in IP-Adressen ermöglicht. Der Vorgang der
Übersetzung einer URL in eine IP-Adresse wird als Namensauflösung (name
resolution) bezeichnet. Das Datenbanksystem mit dem Adressverzeichnis
hat den Namen *Domain Name System* (DNS).

Damit einer der dezentralen DNS-Server erreicht werden kann, muss dessen Adresse
auf dem lokalen Computer in der Systemeinstellung abgelegt sein. Welcher das auf
einem konkreten Computer ist, findet sich in den Netzwerkeinstellungen des
entsprechenden Computers (Netzwerk und Internet > Netzwerkzugang > Eigenschaften
\> DNS-Server).

## Beobachtung des Verbindungsaufbaus mit Wireshark

Der Netzwerkverkehr eines Computers kann mit Hilfe von Wireshark beobachtet
werden. 
[Die Anleitung für die Installation von Wireshark findet sich hier.](https://www.wireshark.org/download.html)