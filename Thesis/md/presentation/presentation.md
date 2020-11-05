---
title: Modernizing Exams — Designing a Tool for Valid and Scalable Decentralized E-Exams
author: Eine Bachelorarbeit von Jasper Anders
date: 30.10.2020
theme: metropolis
---

# Motivation

## Im Allgemeinen

Klausuren sind einer der wenigen Teile der Bildung die nicht im großen Stil von digitalisierung profitiert haben. Die Digitalisierung birgt dabei folgende Vorteile:

- Verbesserte **Auswertung** von Klausurergebnissen
- Erhebliche **Vereinfachung der logistischen Planung** von Klausuren; während des Testens und der Korrektur
- **Archivierung** ist deutlich effizienter und sicherer

- Erweiterung des Klausur-Mediums erlaubt **anwendungsorientiertere Fragen**
- Das **Corona Virus** schränkt zudem Präsenzklausuren erheblich ein

## Wo stehen wir

- E-Klausuren existieren bereits, dann aber oft unter folgenden restriktiven Bedingungen. E-klausuren...
  - nutzen **Infrastruktur der Unis**, also z.B. Computer-Räume
  - finden auf Geräten der Studenten statt, weiterhin aber **zentralisiert**, also z.B. in einem Hörsaal
  - finden unter Einsatz von **Proctoring** statt
  - werden als Möglichkeit der **Selbsteinschätzung** genutzt
- E-Klausuren Tools sind oft in den **LMS** (Learn-Management-Systemen) integriert, die die Instutionen nutzen, um Lernmaterial zu verwalten.

<!-- ## Warum Proctoring keine gute Idee ist

_Proctoring_, meint das **digitale Beaufsichtigen** von Prüflingen über Webcam & Mikrofon durch einen Menschen.

Folgende Problem ergeben sich:

- Schlechte **Skalierbarkeit**, jeder Proctor kann nur eine kleine Gruppe an Prüflingen überwachen
- **Rahmenbedingungen** werden weiterhin von Studenten definiert; somit sind sie offen für Manipulation

$\rightarrow$ schlechtes Aufwand/Leistungs Verhältnis. -->

## Warum Tools, die wir schon haben nicht ausreichen

Prominente Tools haben unterschiedliche **Stärken und Schwächen**. Besonders gravierend sind exemplarisch folgende Themen:

- Schlechte Handhabung von **Verbindungsabbrüchen** $\rightarrow$ Gegebene Antworten müssen u.U. wiederholt werden.
- Keine Möglichkeit der **Identitätsüberprüfung**
- Unzulängliche Maßnahmen gegen **Betrugsversuche**

# Was brauchen wir für eine valide Klausur? -- Anforderungen und Ausgestaltung

## Anforderungen an Klausuren {.shrink}

Klausuren sind mehr als nur eine Summe von Fragen. Unabhängig von Inhalten, müssen Klausuren **Rahmenbedingungen erfüllen**. Diese Rahmenbedingen können mit folgenden Anforderungen abgesteckt werden. Nämlich Anforderungen an ...

- Generelle Validität
- Anfechtungsschutz
- Gleichbehandlung
- Schutz vor Betrugsversuchen
- Transparenz
- Datenschutz
- Integrität
- _und_ Zuordbarkeit

Diese **Anforderung werden durch konkrete Ausgestaltungen erfüllt**. Im Folgenden werden diese Ausgestaltungen skizziert; teilweise in einem **theoretischen** Kontext, teils ganz **praktisch**.

## Generelle Validität {.allowframebreaks}

### Meint:

Klausurergebnisse sollten möglichst genau den **Kenntnis und Fähigkeitenstand** eines Prüflings wiederspiegeln.

### Lässt sich erreichen mit:

- Verschiedene **Fragetypen**
- **Zeitbeschränkung** auf Fragenbasis

### Bedeutet in der Umsetzung:

- Einbinden von **Kontrollzeiten** in der Benutzeroberfläche
  - Automatische Abgabe der Frage nach Ablauf der Zeit
  - Serverzeiten und Zeiten des Gerätes abgleichen
- Erstellen von _partiellen Open-Book_ Klausuren

## Anfechtungsschutz {.allowframebreaks}

### Meint:

Digitale Klausuren werden unter **_unsicheren_ Umständen** geschrieben. Gerade weil der Prüfer diese Umstände schlechter beeinflussen kann, müssen die Aspekte, die er beeinflussen kann besonders stabil sein. D.h.: **Technische und Formale Defekte**, die die Validität einer Klausur in Frage stellen, müssen **minimiert** werden.

### Lässt sich erreichen mit:

- Klare **Kommunikation und Einblicke**, wie die Klausur abläuft
- Fähigkeiten mit **Verbindungsabbrüchen** umzugehen

### Bedeutet in der Umsetzung:

- **Informationsfenster** vor jeder Klausur
- **Einführung** in das Tool vor der Klausur, z.B. anhand einer Testklausur
- **Offline Fähigkeiten** der Software. Lokales Speichern von Antworten

## Gleichbehandlung {.allowframebreaks}

### Meint:

Prüflinge müssen über den Verlauf des Klausur-Prozesses **gleich behandelt** werden.

### Lässt sich erreichen mit:

- Elektronische Klausursysteme müssen **Gerät agnostisch** sein. D.h. auf allen gängigen Betriebssystemen laufen.
- **Ungleichheiten**, die im Korrekturprozess auftreten müssen **eliminiert** werden

### Bedeutet in der Umsetzung:

- Nutzung von **Web-Technologien**, um ein Klausursystem _auszuliefern_
- Verwendung von **Automation**, um die Last auf Korrektoren zu mindern
- Angleichung der zu korrigierenden Klausuren durch **einheitliches Schriftbild**

## Schutz vor Betrugsversuchen {.allowframebreaks}

### Meint:

Einer der entscheiden Punkte im Prüfungsprozess ist das Sicherstellen, der **authentizität der Antwort**. Der Student, der die Antwort gegeben haben soll, muss sie auch in Wirklichkeit gegeben haben und zwar unter den festgelegten Bedingungen.

### Lässt sich erreichen mit:

- Verwendung von großen **Fragen-Pools**; Einzelne Fragen sind somit für Prüflinge nicht gut vorbereitbar
- **Zeitbeschränkung** auf Fragenbasis
- **Zufälligkeit** der Fragenreinfolge und Einschränkung der Navigationsmöglichkeiten; Erschwert Zusammenarbeit unter Prüflingen
- Erzeugung eines **Überwachungs- und Konsequenzgefühls**

### Bedeutet in der Umsetzung:

- Kooperation mit anderen Lehrstühlen; Nutzung von **Crowd Collaboration**, um _Fragen-Pools_ zu füllen
- Nutzung von Kamera- & Tondaten; nicht um eine Live-Überwachung möglich zu machen, sondern um ein **Überwachungsgefühl** zu schaffen
- [Einbinden von Kontrollzeiten in der Benutzeroberfläche]

## Transperenz {.allowframebreaks}

### Meint:

Der Klausurprozess muss **Nachvollziehbar** sein, das bezieht sich vor allem auf das Zustandekommen einer Note.

### Lässt sich erreichen mit:

- **Digitale Einsicht** in Korrektur und Bewertung
  $\rightarrow$ Prüfer muss in der Klausursoftware die Möglichkeit haben ein solches Feedback zu geben.

### Bedeutet in der Umsetzung:

- Durchdachtes **Design des Userinterfaces**, das vor allem für Korrektoren die Klickzahl minimiert.

## Daten Schutz, Integrität und Zuordbarkeit {.allowframebreaks}

### Meint:

Digitale Klausursystem sind **informationsstechnische Systeme** und müssen demnach nach gleichen Standards und Prinzipien gestaltet werden. Besondere Beachtung muss hier der **DSGVO** zuteil werden, denn Klausurdaten sind Personendaten. Auch der **Schutz vor Veränderung** von außen muss gegeben sein.

### Lässt sich erreichen mit:

- Konsequente **Nutzerrechte Verwaltung**; wer darf wo lesen/schreiben/löschen?
- Ausgeführte **Aktionen müssen Nachvollziehbar** sein. Welcher Nutzer ist dafür verantwortlich, dass ein Datenpunkt so aussieht, wie er es tut?
- Programmfehler müssen minimiert werden, der Programmcode muss damit Nachvollziehbar sein. Codebasen sollten also **quelloffen** sein.
