# FUH-LaTeX-2022-1

Materialien für den ersten LaTeX-Kurs 2022 an der Fernuni Hagen

Die Materialien können frei von jedermann genutzt und verändert werden, entsprechende Hinweise auf meine Urheberschaft werden aber gern gesehen.

## Wie kommt man an die Materialien?

git installieren und dann auf der Kommandozeile

git clone https://github.com/UweZiegenhagen/FUH-LaTeX-2022-1.git

Updates holt man so, dabei überschreibt man lokal geänderte Dateien

git fetch --all
git reset --hard origin/master

## Der Kurs

Der Kurs findet an mehreren Samstagen online statt, als Plattform nutzen wir BigBlueButton, der Link wird vorab per E-Mail versandt.

* **Tag 1**: 04.06.2021
* **Tag 2**: 11.06.2021
* **Tag 3**: 18.06.2021

Jeweils grundsätzlich von 10:00 Uhr bis 12:00 Uhr und 13:00 Uhr bis 16:20 Uhr, in Summe also 16 Stunden.

## Agenda der einzelnen Termine

### Tag 1

* Das erste LaTeX-Dokument
* Standard- und KOMA-Klassen
* Chapter, section und co.
* Bilder einbauen
* Tabellen
* Inhalts-, Bild- und Tabellenverzeichnisse

### Tag 2



### Tag 3


## Was wird benötigt

* Ein Rechner (Laptop, Desktop) mit Windows oder MacOS (Linux geht auch, wenn die Kommunikationssoftware dafür verfügbar ist)
* TeX Live 2022 herunterladen und installieren von tug.org/texlive. Eine Anleitung habe ich unter https://www.youtube.com/watch?v=k9KhuZz7k-Q veröffentlicht.
* Wenn ihr unter Linux arbeitet: Bitte nicht aus den Distributionsquellen nehmen, sondern auch von tug.org installieren. Das TeX Live in den Distributionen ist oft nicht aktuell. Mac-User installieren bitte MacTeX (auch auf der tug.org Seite frei verfügbar)
* Ein Editor zur Bearbeitung der TeX-Dateien: TeX Live bringt für Mac und Windows TeXworks mit, einen guten Editor, den ich gern benutze. TeX Studio und Visual Studio Code (mit der ``LaTeX Workshop`` Erweiterung von James Yu) kann ich ebenfalls sehr empfehlen.
* Emacs mit AucTeX ist ebenfalls eine mächtige Kombination, auch für vim gibt es wohl LaTeX-Erweiterungen, die ich aber nicht kenne.
* Grundkenntnisse von Git bzw. Github sind nicht verkehrt, da alle Dateien im Github liegen.

## Kursinhalte

Die Kursinhalte sind flexibel und orientieren sich am Bedarf der Teilnehmerinnen und Teilnehmer, mit dem folgenden Ablauf plane ich:

### Tag 1 - Grundlagen

* Vorstellung der Beteiligten, wer bin ich und wer seid ihr, was sind eure Lernziele
* Historie von TeX und LaTeX
* Check der Umgebungen bzw. Installationen mittels "Hallo \LaTeX" Dokument
* Klassen, Pakete, Umgebungen und Befehle
* Warum man article, report und book nicht nutzen sollte -- die KOMA Klassen
* Strukturierte Dokumente, ``\chapter``, ``\section`` & Co, Inhaltverzeichnisse
* Referenzen mit ``\label`` und ``\ref``
* Float-Objekte in LaTeX
* Einfache Bilder einbetten, Bilderverzeichnisse
* Einfacher Tabellensatz und Tabellenverzeichnisse
* Präsentationen mit ``Beamer``
* LaTeX automatisieren mit ``Arara``
* Schneller TeX mit Autohotkey & Co
* Einfache Bibliografien -- die ``thebibliography`` Umgebung


### Tag 2 - Tabellen, Mathematik, und mehr

* Vorstellung von DANTE e.V.
* Wiederholung vom 1. Tag, Fragen beantworten
* Wir bauen eine Vorlage für Seminar- und Abschlussarbeiten: ``titlepage``, ``scrpage``
* Komplexe Bibliografien mit ``biblatex``, ``biber`` und ``jabref``

Bitte Jabref von www.jabref.org installieren, kostet nichts und ist sehr gut.

* Briefe setzen mit ``scrlttr2``
* Quellcode-Listings einfügen mit dem ``Listings`` Paket
* Mehr zu Mathematiksatz (mit ``amsmath``)
* ``nicefrac`` und ``nicematrix``
* Mehr zum Bilder einbetten: ``subfigure`` und ``subcaption`` 


### Tag 3 - Bibliografien und Präsentationen

* Zusammenfassung vom 2. Termin, Wiederholung
* Lebensläufe mit ``moderncv``
* Andere Editoren: ``TeXworks`` und ``Visual Studio Code``
* Einheitensatz mit ``siunitx``
* Fuß- und Randnoten -- ``\footnote`` and ``\marginpar``
* Fonts für ``pdflatex``, der LaTeX Font Katalog (https://tug.org/FontCatalogue/)
* Liste wichtiger Pakete: https://ctan.mc1.root.project-creative.net/info/first-packages/first-packages.html
* Umrahmte (farbige) Boxen mit ``tcolorbox`` (``texdoc tcolorbox``), alternativ siehe das ``mdframed`` Paket
* Grafiken erstellen mit LaTeX-Paketen, Kurzeinführung ``TikZ``
* Grundlagen der Automatisierung von Textsatz mit Python (Ein Weg, Serienbriefe zu erzeugen...)
* Von ``pdflatex`` zu ``lualatex``, Systemschriften nutzen
* Frage-und-Antwort-Teil


## Literaturempfehlungen

Empfohlen werden:

* Alle Bücher von Herbert Voß (https://www.lehmanns.de/search/quick?PHPSESSID=mi28bh61dhv2nu8keg4hjnkunumgi5ah&mediatype_id=&q=herbert+vo%C3%9F), insbesondere die Einführung
* Der LaTeX Begleiter in der 2. Auflage (ist auch nicht mehr brandaktuell, bietet aber einen guten Überblick über LaTeX)

## Weitere Links

* https://open.hpi.de/courses/git2020 Git Kurs beim HPI
* Meine Briefvorlage https://www.uweziegenhagen.de/?p=3290
* Biblatex Cheat Sheet, https://www.ctan.org/tex-archive/info/biblatex-cheatsheet

