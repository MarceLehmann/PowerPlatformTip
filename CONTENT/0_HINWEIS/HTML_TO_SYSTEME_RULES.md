# HTML zu Systeme.io Newsletter Konvertierung

Diese Anleitung beschreibt die Logik, mit der HTML-Newsletter in das Markdown-Format für systeme.io konvertiert werden. Diese Regeln sind im Skript `process-tip.py` implementiert.

## 1. Bereinigung
*   **Entfernen**: Komplette Blöcke von `<head>`, `<style>` und `<script>` werden entfernt.
*   **Entfernen**: Alle `<ul>` und `<ol>` Tags (die Listen-Struktur selbst) werden entfernt, die Inhalte bleiben erhalten.
*   **Normalisierung**: Zeilenumbrüche werden vereinheitlicht.

## 2. Spezielle Klassen-Konvertierung
Das Skript sucht nach spezifischen CSS-Klassen aus dem Newsletter-Template und wandelt diese in Markdown um:

| HTML Klasse | Konvertierung | Markdown Output |
| :--- | :--- | :--- |
| `<div class="section-title"> Titel </div>` | Überschrift | `**Titel**` |
| `<div class="step">...<span class="step-number">1</span><b>Titel</b>...Content...</div>` | Nummerierte Liste | `1. **Titel**: Content` |
| `<div class="use-case"> <div class="use-case-title">Titel</div> Content </div>` | Fettgedruckter Titel | `**Titel**` <br> `Content` |
| `<div class="faq-item"> <div class="faq-question">Frage</div> Antwort </div>` | Frage/Antwort Block | `**Frage**` <br> `Antwort` |

## 3. Standard HTML Tags
Allgemeine HTML-Tags werden wie folgt übersetzt:

*   **Links**: `<a href="url">Text</a>`  →  `[Text](url)`
*   **Listen-Elemente**: `<li>Text</li>`  →  `- Text`
*   **Überschriften**: `<h1>` bis `<h6>`  →  `**Text**` (Fett, da systeme.io Markdown begrenzt ist)
*   **Fett**: `<b>`, `<strong>`  →  `**Text**`
*   **Kursiv**: `<i>`, `<em>`  →  `*Text*`
*   **Absätze**: `</p>`  →  zwei Zeilenumbrüche (`\n\n`)
*   **Zeilenumbrüche**: `<br>`  →  ein Zeilenumbruch (`\n`)

## 4. Finalisierung
*   Alle übrigen HTML-Tags (z.B. `<div>`, `<span>` ohne spezielle Behandlung) werden entfernt.
*   Mehrfache Leerzeilen werden auf maximal zwei reduziert.
*   Kopf- und Fußzeilen (Titel, "Mehr erfahren"-Link) werden dem konvertierten Text hinzugefügt.
