<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Dies ist eine detaillierte Anleitung, basierend auf dem Video, wie man in Power Automate das 30-Tage-Timeout-Problem bei Genehmigungen (Approvals) umgeht.

Das Video zeigt zwei verschiedene Lösungswege:
Neustart mit neuer Genehmigung: Nach dem Timeout wird eine komplett neue Anfrage gesendet.
Neustart mit derselben Genehmigung: Der Flow startet neu, wartet aber weiterhin auf die ursprüngliche Genehmigung (der Link in der E-Mail bleibt gültig).

Voraussetzung: SharePoint Listen-Setup

Bevor der Flow erstellt wird, müssen in der SharePoint-Liste zwei Hilfsspalten angelegt werden (wie im Video bei 00:03 - 00:10 zu sehen):
TriggerFlow:
Typ: Ja/Nein (Boolean)
Standardwert: Ja (Yes)
Zweck: Diese Spalte steuert, wann der Flow starten darf, und verhindert Endlosschleifen.
ApprovalID:
Typ: Textzeile (Single line of text)
Zweck: Speichert die ID der laufenden Genehmigung (nur für Methode 2 notwendig).

Schritt 1: Der Trigger und die Endlosschleifen-Prävention

Damit der Flow sich bei Updates nicht selbst ständig neu startet (Endlosschleife), wird eine Trigger-Condition gesetzt.
Trigger: „When an item is created or modified“ (SharePoint).
Trigger Conditions (Einstellungen):
Klicke auf die drei Punkte (...) beim Trigger -> Settings.
Füge ganz unten unter „Trigger Conditions“ folgende Formel ein:
@equals(triggerOutputs()?['body/TriggerFlow'], true)
Erklärung: Der Flow startet nur, wenn die Spalte TriggerFlow auf "Ja" steht.
Erste Aktion: Update item:
Setze die Spalte TriggerFlow sofort auf No (False).
Erklärung: Dies „sperrt“ den Flow, damit Änderungen während des Laufs keinen neuen Flow auslösen.

Methode 1: „Everytime NEW Approval“ (Immer neue Genehmigung)

(Im Video links: Scope „Everyone NEW Approval“)
Diese Methode ist einfacher. Wenn nach 30 Tagen (oder einer definierten Zeit) keine Antwort kommt, bricht der Flow ab und startet sich selbst neu. Der Genehmiger erhält eine neue E-Mail.
Aktion: Füge „Start and wait for an approval“ hinzu.
Konfiguriere Titel, Zugewiesen an, etc. wie gewohnt.
Timeout-Logik einbauen:
Füge nach der Genehmigung eine Aktion „Update item“ hinzu.
Setze in dieser Aktion TriggerFlow wieder auf Yes (True).
„Configure Run After“ (Laufzeit-Konfiguration):
Klicke auf die drei Punkte (...) der „Update item“-Aktion (die, die auf True setzt).
Wähle Configure run after.
Wähle nur has timed out aus (entferne den Haken bei is successful).
Ergebnis: Diese Aktion wird nur ausgeführt, wenn die Genehmigung das Zeitlimit (Standard 30 Tage) überschreitet.
Effekt: Der Flow läuft ins Timeout -> Das Item wird auf „TriggerFlow = Ja“ gesetzt -> Der Trigger (Schritt 1) erkennt dies und startet einen neuen Flow mit einer neuen Genehmigung.

Methode 2: „Start and Wait for the SAME Approval“ (Dieselbe Genehmigung behalten)

(Im Video rechts: Scope „Start and Wait for the SAME Approval“)
Das ist die elegantere Methode. Wenn der Flow nach 30 Tagen abläuft, startet er neu, merkt aber, dass es schon eine Genehmigung gibt, und wartet weiter auf diese. Der Link in der ersten E-Mail bleibt gültig.
Der Ablauf im Detail:
Bedingung (Condition): Prüfen, ob es schon eine Genehmigung gibt.
Prüfe: Ist die SharePoint-Spalte ApprovalID leer (null/empty)?
WENN JA (True) – Wir brauchen eine neue Genehmigung:
Aktion: Create an approval (Wichtig: Create, nicht Start and wait!).
Aktion: Update item (SharePoint).
Schreibe die „Approval ID“ aus dem vorherigen Schritt in die SharePoint-Spalte ApprovalID.
Hinweis: Damit ist die ID für den nächsten Durchlauf gesichert.
WENN NEIN (False) – Eine Genehmigung existiert bereits:
Aktion: Compose (Verfassen).
Füge hier den Wert der SharePoint-Spalte ApprovalID ein.
Zusammenführung \& Warten:
Unterhalb der Bedingung (außerhalb der Ja/Nein-Boxen) füge die Aktion Wait for an approval hinzu.
Wichtig: Im Feld „Approval ID“ nutzt du nun die ID aus der Create an approval-Aktion (aus dem Ja-Zweig) ODER die aus dem Compose (aus dem Nein-Zweig).
Tipp: In Power Automate wählt man hier oft das Output des Schrittes, der die ID liefert. Da es zwei Quellen gibt, muss man sicherstellen, dass er die vorhandene nimmt. (Im Video wird impliziert, dass man die ID aus der Variablen/Spalte nimmt).
Timeout-Logik (Der Restart-Loop):
Füge nach „Wait for an approval“ die Aktion Update item hinzu.
Setze TriggerFlow auf Yes (True).
Gehe wieder auf Configure run after bei diesem Update-Item.
Wähle nur has timed out.
Erfolgs-Logik (Wenn genehmigt wurde):
Füge einen parallelen Zweig oder eine Aktion hinzu für den Fall is successful.
Hier führst du die Aktionen aus, die passieren sollen, wenn wirklich genehmigt wurde (z.B. E-Mail senden, Status ändern).
Ganz wichtig am Ende: Update item, um ApprovalID wieder zu leeren und TriggerFlow auf False zu lassen, damit der Loop endet.

Zusammenfassung der Unterschiede

Feature
Methode 1 (Everytime NEW)
Methode 2 (SAME Approval)
Verhalten nach 30 Tagen
Flow bricht ab, startet neu.
Flow bricht ab, startet neu.
Genehmigungs-E-Mail
Der Chef bekommt eine neue E-Mail.
Keine neue E-Mail nötig (alter Link geht noch).
Approval Center
Es taucht ein neuer Eintrag auf.
Der ursprüngliche Eintrag bleibt bestehen.
Komplexität
Niedrig
Mittel (Benötigt ID-Speicherung).
Welche Methode sollten Sie wählen?
Nutzen Sie Methode 2, wenn Sie Manager nicht mit Erinnerungs-E-Mails nerven wollen und die Genehmigung oft länger als 30 Tage dauern kann.
Nutzen Sie Methode 1, wenn Sie möchten, dass die Anforderung als "Erinnerung" neu ganz oben im Postfach erscheint.

Title:
PowerPlatformTip – Infinite Approvals

2–3 Sentence Summary:
This tip shows how to build long-running approval flows in Power Automate that survive the 30‑day timeout by safely restarting themselves. You learn two patterns: always send a fresh approval after timeout, or keep waiting on the original approval so the first email link and Approval Center entry remain valid.[^1_1][^1_2]

💡 Challenge:
Standard approval actions in Power Automate time out after 30 days, which breaks long-running business processes like HR, legal, or management approvals. Without extra logic, the approval is left in an inconsistent state and you cannot keep waiting on it or automatically restart the flow.[^1_2][^1_1]

✅ Solution:
Use a SharePoint list with two helper columns (TriggerFlow and ApprovalID) plus a trigger condition to prevent infinite loops. Then implement either “Everytime NEW Approval” (restart with a brand‑new approval) or “Start and Wait for the SAME Approval” (restart the flow but keep waiting on the existing approval using its Approval ID).[^1_3][^1_4][^1_2]

🔧 How it’s done:

1) Prepare SharePoint and the trigger:
🔸 Add a Yes/No column TriggerFlow (default Yes) and a Single line of text column ApprovalID (for method 2) to your SharePoint list, then use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is Yes.[^1_4][^1_5][^1_3]
🔸 Immediately after the trigger, add an Update item action that sets TriggerFlow to No, so any further list changes during the run cannot re-trigger the flow and cause recursion.[^1_5][^1_3]
2) Method 1 – Everytime NEW Approval:
🔸 Add Start and wait for an approval, configure it as usual, and optionally set the Timeout in the action’s Settings to something like 29 days so the timeout branch runs just before the global 30‑day limit.[^1_6][^1_3]
🔸 After the approval action, add an Update item that sets TriggerFlow back to Yes and configure run after to only run on has timed out; when this happens, the item flip to Yes re-fires the trigger and a completely new approval is sent.[^1_3][^1_2]
3) Method 2 – Start and Wait for the SAME Approval:
🔸 Add a Condition that checks if ApprovalID is empty; if empty, use Create an approval (not Start and wait) and then Update item to store the Approval ID in the ApprovalID column, otherwise use a Compose step that outputs the existing ApprovalID from SharePoint.[^1_6][^1_3]
🔸 Below the condition, add Wait for an approval and feed it the Approval ID (either directly from Create an approval or via the Compose), then add an Update item after it that sets TriggerFlow to Yes with run after configured only for has timed out, plus a separate success branch that executes the real post‑approval logic and finally clears ApprovalID and leaves TriggerFlow as No to end the loop.[^1_2][^1_3][^1_6]

🎉 Result:
Your approval flows can now run effectively without a time limit, because each timeout only restarts the flow instead of killing the process. Depending on the chosen method, approvers either receive a fresh reminder email every cycle or keep working with the original approval task and email link.[^1_1][^1_3][^1_2]

🌟 Key Advantages:
🔸 Avoids broken approval processes by handling the 30‑day timeout explicitly instead of letting the run fail.[^1_1][^1_2]
🔸 Gives you a choice between “new reminder email every cycle” and “single clean task in the Approvals center” depending on business preference.[^1_3][^1_2]
🔸 Uses only standard SharePoint and Approvals actions, so the pattern is easy to govern and fits common Power Automate limits and licensing.[^1_6][^1_1]

🛠️ FAQ:
Q1: Why can’t I just increase the approval timeout beyond 30 days?
A: The 30‑day limit is a platform limit for flow actions; pending steps time out after this period, so you must design around it using restarts or separate flows.[^1_7][^1_1]

Q2: Why use Create an approval plus Wait for an approval in method 2?
A: Splitting creation and waiting gives you access to the Approval ID, which you can store in SharePoint and reuse after a restart so the same approval task is monitored across multiple runs.[^1_3][^1_6]

Q3: How do I avoid infinite trigger loops with TriggerFlow?
A: The trigger condition ensures the flow only starts when TriggerFlow is Yes, and the very first Update item sets it to No, so only the deliberate flip back to Yes in the timeout branch can re-trigger the flow.[^1_4][^1_5]

Hashtags:
\#PowerPlatform \#PowerAutomate \#SharePoint \#Approvals \#PowerPlatformTip
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://learn.microsoft.com/en-us/power-automate/limits-and-config

[^1_2]: https://tomriha.com/how-to-process-power-automate-approval-task-after-30-days/

[^1_3]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^1_4]: https://citizendevelopmentacademy.com/blog/power-automate-trigger-conditions/

[^1_5]: https://watfordconsulting.com/2023/06/28/power-automate-trigger-conditions/

[^1_6]: https://learn.microsoft.com/en-us/power-automate/wait-for-approvals

[^1_7]: https://ideas.powerautomate.com/d365community/idea/9d116106-76e4-4f00-85be-1b3568fa0c84

[^1_8]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md

[^1_9]: https://www.matthewdevaney.com/extend-a-power-automate-approval-over-the-30-day-limit/

[^1_10]: https://www.youtube.com/watch?v=h6Eb-F0P6Hs

[^1_11]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^1_12]: https://community.dynamics.com/blogs/post/?postid=526f1f85-d10f-4701-b3b7-312eb262fc29

[^1_13]: https://www.youtube.com/watch?v=frkhd6eAjC8

[^1_14]: https://members.collab365.com/c/microsoft365_forum/overcoming-power-automate-30-day-limits

[^1_15]: https://alrafayglobal.com/power-automate-trigger-conditions/

[^1_16]: https://community.powerplatform.com/forums/thread/details/?threadid=c7d10d0e-ed96-4b96-a1fd-f302afedae73

[^1_17]: https://www.youtube.com/watch?v=VgC2jcIM3XY

[^1_18]: https://community.powerplatform.com/forums/thread/details/?threadid=1fe882d7-9c0a-44ce-893c-1c6217e1c28d

[^1_19]: https://learn.microsoft.com/en-us/power-automate/triggers-introduction

[^1_20]: https://www.matthewdevaney.com/reassign-an-approval-in-power-automate/

[^1_21]: https://nboldapp.com/5-power-automate-approval-flow-errors-fix-guide/


---

# ok, weiter

Alles klar, gehen wir in deinen Orchestrator‑Flow A und bauen den REVIEW‑Tipp sauber fertig.

Title:
PowerPlatformTip – Infinite Approvals

2–3 Sentence Summary:
Infinite Approvals lets you run Power Automate approval flows über die 30‑Tage‑Grenze hinaus, indem der Flow sich kontrolliert selbst neu startet. Du kannst wählen, ob nach dem Timeout stets eine neue Genehmigung versendet wird oder ob der Flow weiter auf dieselbe Approval wartet und damit den ursprünglichen Link gültig hält.[^2_1][^2_2][^2_3]

💡 Challenge:
Standard-Approvals in Power Automate brechen nach 30 Tagen ab, wodurch langfristige Genehmigungen ins Leere laufen. Ohne zusätzliches Design kannst du weder sauber neu starten noch weiter auf die bestehende Aufgabe warten, was zu hängenden Prozessen und frustrierten Fachbereichen führt.[^2_2][^2_3][^2_4]

✅ Solution:
Nutze eine SharePoint-Liste mit den Spalten TriggerFlow (Ja/Nein) und ApprovalID (Text), um den Flow-Start zu steuern und die laufende Approval-ID zu speichern. Darauf aufbauend implementierst du entweder die einfache Variante „Everytime NEW Approval“ mit neuen E-Mails nach Timeout oder die fortgeschrittene Variante „Start and Wait for the SAME Approval“, die dieselbe Approval über mehrere Flow-Runs hinweg weiter überwacht.[^2_3][^2_5][^2_1]

🔧 How it’s done:

1. Richte den SharePoint-Trigger When an item is created or modified mit der Triggerbedingung `@equals(triggerOutputs()?['body/TriggerFlow'], true)` ein und setze direkt danach per Update item die Spalte TriggerFlow auf No, um Endlosschleifen zu verhindern.[^2_6][^2_7][^2_1]
2. Für „Everytime NEW Approval“ verwendest du Start and wait for an approval und fügst danach ein Update item hinzu, das TriggerFlow auf Yes setzt und nur bei has timed out läuft, sodass nach jedem Timeout ein komplett neuer Approval-Lauf mit neuer E-Mail startet.[^2_5][^2_1][^2_3]
3. Für „SAME Approval“ prüfst du zuerst, ob ApprovalID leer ist, erzeugst bei Bedarf mit Create an approval eine neue Genehmigung und speicherst die Approval ID, oder liest bei vorhandener ID diese mit Compose aus und übergibst sie anschließend an Wait for an approval, um dieselbe Approval weiter zu überwachen.[^2_1][^2_3][^2_5]
4. Hinter Wait for an approval baust du zwei Pfade: einen Timeout-Pfad mit Update item (TriggerFlow = Yes, run after = has timed out) zum Neustart sowie einen Erfolgs‑Pfad (is successful) für deine Geschäftslogik, der am Ende ApprovalID leert und TriggerFlow auf No belässt, damit der Loop sauber endet.[^2_3][^2_5][^2_1]

🎉 Result:
Mit Infinite Approvals laufen deine Genehmigungsprozesse praktisch unbegrenzt, ohne gegen die 30‑Tage‑Plattformgrenze zu prallen. Fachanwender entscheiden je nach Szenario, ob sie bei jedem Zyklus eine frische Erinnerungs‑Mail möchten oder einen einzigen stabilen Approval‑Eintrag im Approval Center bevorzugen.[^2_2][^2_1][^2_3]

🌟 Key Advantages:

- Stabil laufende Langzeit-Approvals trotz harter 30‑Tage‑Action-Limits in Power Automate.[^2_4][^2_2]
- Frei wählbares Verhalten: neue Reminder‑E-Mails oder ununterbrochene Weiterverfolgung derselben Approval.[^2_1][^2_3]
- Einfache Implementierung mit Standard-Connectors (SharePoint + Approvals) und klar kontrollierter Trigger-Logik ohne versteckte Endlosschleifen.[^2_8][^2_6][^2_1]

🛠️ FAQ:
Q1: Kann ich die 30‑Tage‑Grenze direkt erhöhen statt neu zu starten?
A: Nein, die 30‑Tage‑Frist gehört zu den Plattform-Limits für Flow-Actions, daher musst du das Problem über Restart-Patterns wie in diesem Tipp lösen.[^2_9][^2_2]

Q2: Warum brauche ich bei Methode 2 unbedingt ApprovalID in SharePoint?
A: Die Approval ID verknüpft mehrere Flow-Runs mit derselben Genehmigung; ohne diese Speicherung könnte der neu gestartete Flow nicht mehr wissen, auf welche bestehende Approval er warten soll.[^2_5][^2_1]

Q3: Was passiert, wenn während des Flows jemand das Item bearbeitet?
A: Durch die Triggerbedingung auf TriggerFlow und das frühe Zurücksetzen auf No löst diese Bearbeitung keinen neuen Run aus; nur das gezielte Setzen auf Yes im Timeout-Pfad startet den Flow erneut.[^2_7][^2_6]

Wenn du magst, geht es als nächstes mit Phase 2 (Jekyll‑Markdown‑Datei) weiter.
<span style="display:none">[^2_10][^2_11][^2_12]</span>

<div align="center">⁂</div>

[^2_1]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^2_2]: https://learn.microsoft.com/en-us/power-automate/limits-and-config

[^2_3]: https://tomriha.com/how-to-process-power-automate-approval-task-after-30-days/

[^2_4]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^2_5]: https://learn.microsoft.com/en-us/power-automate/wait-for-approvals

[^2_6]: https://citizendevelopmentacademy.com/blog/power-automate-trigger-conditions/

[^2_7]: https://watfordconsulting.com/2023/06/28/power-automate-trigger-conditions/

[^2_8]: https://learn.microsoft.com/en-us/power-automate/triggers-introduction

[^2_9]: https://ideas.powerautomate.com/d365community/idea/9d116106-76e4-4f00-85be-1b3568fa0c84

[^2_10]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md

[^2_11]: mach-einen-tip-wie-ich-jede-be-30z4ZTFNST66j_g9DHDWcQ.md

[^2_12]: ich-mache-einen-tipp-uber-das-QmsNzMlXTvGb7fkgFLHj.w.md


---

# weiter, aber in englisch

Here is the same tip in English, keeping your two-method structure and the SharePoint prerequisites.

Title:
PowerPlatformTip – Infinite Approvals in Power Automate

2–3 Sentence Summary:
This tip shows how to design approval flows in Power Automate that safely bypass the 30‑day timeout limit. You will learn two patterns: restarting with a brand‑new approval request, or restarting the flow while still waiting on the original approval so the first email link and task remain valid.[^3_1][^3_2][^3_3]

## SharePoint setup

Create or extend a SharePoint list that will drive your approval flow.[^3_4][^3_1]
Add two helper columns:

- TriggerFlow: Yes/No, default Yes. Controls whether the flow is allowed to start.
- ApprovalID: Single line of text. Stores the current Approval ID (needed only for method 2).[^3_1][^3_4]


## Step 1 – Trigger and loop protection

Use the SharePoint trigger When an item is created or modified and add a trigger condition so the flow only starts when TriggerFlow is Yes.[^3_5][^3_6][^3_1]

- Trigger condition (in Settings → Trigger conditions):
`@equals(triggerOutputs()?['body/TriggerFlow'], true)`
- First action in the flow: Update item and set TriggerFlow to No to “lock” the record while the flow is running and avoid infinite trigger loops.[^3_5][^3_1]


## Method 1 – “Everytime NEW Approval”

This method restarts with a completely new approval whenever the previous one times out.[^3_2][^3_1]

Steps:

- Add Start and wait for an approval and configure Title, Assigned to, etc. as usual. Optionally set a custom Timeout in the action settings (for example 29 days).[^3_7][^3_1]
- After the approval action, add Update item and set TriggerFlow to Yes. In Configure run after for this Update item, tick only has timed out and uncheck is successful. This means: only if the approval timed out will the list item be flipped back to TriggerFlow = Yes, which retriggers the flow and sends a new approval.[^3_2][^3_1]

Effect:

- After 30 days with no response, the approval action times out.
- The timeout branch sets TriggerFlow to Yes.
- The SharePoint trigger fires again and creates a brand‑new approval email and Approval Center entry.[^3_8][^3_1]


## Method 2 – “Start and Wait for the SAME Approval”

This method is more elegant: the flow restarts on timeout, but it keeps waiting on the original approval using its Approval ID.[^3_4][^3_1][^3_2]
The first email link and the original Approvals task continue to work across restarts.[^3_3][^3_7]

1) Check if an approval already exists

- Add a Condition that checks if the ApprovalID column in SharePoint is empty (null/empty).[^3_1][^3_4]
- If Yes (no approval yet):
    - Add Create an approval (important: Create, not Start and wait).
    - Add Update item and write the Approval ID from Create an approval into the ApprovalID column. This persists the approval across flow runs.[^3_9][^3_4][^3_1]
- If No (ApprovalID contains a value):
    - Add a Compose action and put the ApprovalID value from the SharePoint item into it. This represents the existing approval to continue waiting on.[^3_4][^3_1]

2) Wait for the correct approval

- Under the Condition (outside both branches), add Wait for an approval.[^3_7][^3_9]
- In the Approval ID field, reference the ID of the approval you want to wait for. In practice, you use the stored ApprovalID value (from Update item / Compose) so that every restarted run waits on the same approval task.[^3_9][^3_1][^3_4]

3) Build the restart loop (timeout path)

- After Wait for an approval, add Update item and set TriggerFlow to Yes.
- In Configure run after for this Update item, tick only has timed out.
- When the approval times out, this Update item runs, flips TriggerFlow back to Yes, and the trigger starts a new run which again finds the existing ApprovalID and continues waiting on it.[^3_10][^3_2][^3_1]

4) Handle successful approvals and clean up

- Add a separate branch or parallel action from Wait for an approval with run after set to is successful.
- In this branch, execute your business logic (emails, status changes, etc.).
- At the end, add Update item to:
    - Clear ApprovalID (empty string or null) so no approval is considered active.
    - Leave TriggerFlow as No so the loop stops and the item no longer retriggers the flow.[^3_11][^3_1][^3_4]


## When to use which method

- Use Method 2 (SAME Approval) if you want a clean user experience: one approval task in Approvals, one email link that stays valid, and no extra reminder emails caused by new tasks.[^3_3][^3_4]
- Use Method 1 (Everytime NEW) if you explicitly want a fresh approval request to appear at the top of the approver’s inbox and Approval Center after each timeout, acting as a reminder.[^3_2][^3_1]
<span style="display:none">[^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18][^3_19][^3_20][^3_21]</span>

<div align="center">⁂</div>

[^3_1]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^3_2]: https://tomriha.com/how-to-process-power-automate-approval-task-after-30-days/

[^3_3]: https://www.matthewdevaney.com/extend-a-power-automate-approval-over-the-30-day-limit/

[^3_4]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^3_5]: https://citizendevelopmentacademy.com/blog/power-automate-trigger-conditions/

[^3_6]: https://alrafayglobal.com/power-automate-trigger-conditions/

[^3_7]: https://learn.microsoft.com/en-us/power-automate/modern-approvals

[^3_8]: https://nboldapp.com/5-power-automate-approval-flow-errors-fix-guide/

[^3_9]: https://learn.microsoft.com/en-us/power-automate/wait-for-approvals

[^3_10]: https://members.collab365.com/c/microsoft365_forum/overcoming-power-automate-30-day-limits

[^3_11]: https://tomriha.com/build-a-restartable-approval-flow-in-power-automate/

[^3_12]: https://community.powerplatform.com/forums/thread/details/?threadid=7b33a264-e800-4fde-a7d4-bf11510e79e4

[^3_13]: https://www.youtube.com/watch?v=h6Eb-F0P6Hs

[^3_14]: https://community.powerplatform.com/forums/thread/details/?threadid=c10829ae-811b-474b-984d-e2b0b0bd3931

[^3_15]: https://www.iwmentor.com/pages/blog/sharepoint-approval-requests-in-power-automate

[^3_16]: https://community.powerplatform.com/forums/thread/details/?threadid=6932a9bd-4225-42f2-b96b-d7e4178b8641

[^3_17]: https://www.youtube.com/watch?v=qc9M7BjL9Jk

[^3_18]: https://www.reddit.com/r/PowerPlatform/comments/1ag4kr9/best_practice_help_for_approval_workflows/

[^3_19]: https://community.dynamics.com/blogs/post/?postid=526f1f85-d10f-4701-b3b7-312eb262fc29

[^3_20]: https://www.youtube.com/watch?v=tiLyIL6Q2Wk

[^3_21]: https://community.dynamics.com/blogs/post/?postid=9539406b-594b-4c28-a6af-e46b41ba63c3


---

# weiter

Based on the template structure, here's the complete PowerPlatformTip in the standard format:[^4_1]

***

**Title:**
PowerPlatformTip – Infinite Approvals: Bypass the 30-Day Timeout

**2–3 Sentence Summary:**
Infinite Approvals shows you how to build Power Automate approval flows that survive beyond the 30-day timeout limit by automatically restarting themselves. You learn two implementation patterns: restart with a fresh approval request each cycle, or restart the flow while continuing to wait on the original approval so the email link and Approval Center task remain valid.[^4_2][^4_3][^4_4]

**💡 Challenge:**
Standard Power Automate approval actions time out after 30 days, breaking long-running business processes like HR onboarding, legal reviews, or executive sign-offs. Without extra design, the approval is left in an inconsistent state and you cannot automatically resume or restart the flow.[^4_4][^4_5][^4_2]

**✅ Solution:**
Use a SharePoint list with two helper columns (TriggerFlow and ApprovalID) plus a trigger condition to prevent infinite loops. Then implement either "Everytime NEW Approval" (restart with a brand-new approval) or "Start and Wait for the SAME Approval" (restart the flow but keep waiting on the existing approval using its stored Approval ID).[^4_3][^4_6][^4_4]

**🔧 How it's done:**

1. Prepare your SharePoint list and trigger
🔸 Add a Yes/No column TriggerFlow (default Yes) and a Single line of text column ApprovalID to your SharePoint list.[^4_6][^4_3]
🔸 Use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is Yes.[^4_7][^4_8][^4_3]
🔸 Immediately after the trigger, add Update item that sets TriggerFlow to No, preventing any further list changes during the run from re-triggering the flow.[^4_3][^4_7]
2. Method 1 – Everytime NEW Approval (simple restart)
🔸 Add Start and wait for an approval, configure it normally, and optionally set Timeout in Settings to 29 days so the timeout branch runs just before the platform limit.[^4_9][^4_10][^4_3]
🔸 After the approval action, add Update item that sets TriggerFlow back to Yes and configure run after to only execute on has timed out; when this happens, the item flip retriggers the flow and sends a completely new approval request.[^4_11][^4_4][^4_3]
3. Method 2 – Start and Wait for the SAME Approval (persistent approval)
🔸 Add a Condition checking if ApprovalID is empty; if empty, use Create an approval (not Start and wait) and then Update item to store the Approval ID in the ApprovalID column, otherwise use Compose to output the existing ApprovalID from SharePoint.[^4_6][^4_9][^4_3]
🔸 Below the condition, add Wait for an approval and feed it the Approval ID (from either Create an approval or Compose), then add Update item after it that sets TriggerFlow to Yes with run after configured only for has timed out.[^4_4][^4_9][^4_3]
🔸 Add a separate success branch (is successful) that executes your post-approval business logic and finally clears ApprovalID and leaves TriggerFlow as No to end the loop cleanly.[^4_11][^4_3][^4_6]

**🎉 Result:**
Your approval flows now run effectively without time limits, because each timeout safely restarts the flow instead of breaking the process. Depending on your chosen method, approvers either receive fresh reminder emails every cycle or work with the original approval task and email link throughout the entire process.[^4_2][^4_3][^4_4]

**🌟 Key Advantages:**
🔸 Eliminates broken approval processes by explicitly handling the 30-day timeout instead of letting runs fail silently.[^4_5][^4_2][^4_4]
🔸 Gives you control over user experience: new reminder emails every cycle versus a single clean task in the Approvals center.[^4_3][^4_6]
🔸 Uses only standard SharePoint and Approvals actions, making the pattern easy to govern and compatible with common Power Automate licensing.[^4_10][^4_9]

**🛠️ FAQ:**

**Q1: Why can't I just increase the approval timeout beyond 30 days?**
A: The 30-day limit is a platform constraint for flow actions; pending steps automatically time out after this period, so you must design around it using restart patterns or separate flows.[^4_2][^4_4]

**Q2: Why split Create an approval and Wait for an approval in method 2?**
A: Separating creation from waiting gives you access to the Approval ID, which you store in SharePoint and reuse after restarts so the same approval task is monitored across multiple flow runs.[^4_9][^4_6][^4_3]

**Q3: How do I prevent infinite trigger loops with TriggerFlow?**
A: The trigger condition ensures the flow only starts when TriggerFlow is Yes, and the very first Update item sets it to No immediately, so only the deliberate flip back to Yes in the timeout branch can re-trigger the flow.[^4_8][^4_7][^4_11]

**Hashtags:**
\#PowerPlatform \#PowerAutomate \#SharePoint \#Approvals \#PowerPlatformTip

***

This completes the **Review Tip** phase. Would you like me to continue with **Phase 2 (Jekyll Markdown file)** or **Phase 3 (HTML Newsletter)**?[^4_1]

<div align="center">⁂</div>

[^4_1]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md

[^4_2]: https://www.matthewdevaney.com/extend-a-power-automate-approval-over-the-30-day-limit/

[^4_3]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^4_4]: https://tomriha.com/how-to-process-power-automate-approval-task-after-30-days/

[^4_5]: https://nboldapp.com/5-power-automate-approval-flow-errors-fix-guide/

[^4_6]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^4_7]: https://citizendevelopmentacademy.com/blog/power-automate-trigger-conditions/

[^4_8]: https://alrafayglobal.com/power-automate-trigger-conditions/

[^4_9]: https://learn.microsoft.com/en-us/power-automate/wait-for-approvals

[^4_10]: https://learn.microsoft.com/en-us/power-automate/modern-approvals

[^4_11]: https://tomriha.com/build-a-restartable-approval-flow-in-power-automate/


---

# phase 2

2025-11-25-powerplatformtip-001-infinite-approvals.md

```markdown
---
title: "#PowerPlatformTip 001 – 'Infinite Approvals beyond 30 days'"
date: 2025-11-25
categories:
    - Article
    - PowerPlatformTip
tags:
    - PowerAutomate
    - PowerApps
    - Dataverse
    - Governance
    - PowerPlatformTip
excerpt: "Infinite Approvals lets you build Power Automate approval flows that survive beyond the 30-day timeout limit by safely restarting themselves. You can either send a fresh approval request after each timeout or restart the flow while still waiting on the original approval so the first email link and task remain valid."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

Standard Power Automate approval actions time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals.[web:2][web:3] When the approval action times out, the flow run stops and you cannot continue to wait for the decision or automatically resume the process.[web:2][web:9]

## ✅ Solution

Use a SharePoint list with two helper columns to control when the flow is allowed to trigger and, for the advanced pattern, to store the current Approval ID.[web:3][web:6] On top of this, implement one of two patterns: either create a brand-new approval whenever the previous one times out or restart the flow and keep waiting on the same approval task by reusing its Approval ID.[web:3][web:6][web:9]

## 🔧 How It's Done

1. Prepare SharePoint and the trigger  
🔸 Add a Yes/No column TriggerFlow with default Yes and a Single line of text column ApprovalID to your SharePoint list, then use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is set to Yes.[web:3][web:7][web:13]  
🔸 Make the very first action after the trigger an Update item that sets TriggerFlow to No so any further edits during the run cannot re-trigger the flow and create infinite loops.[web:3][web:7]

2. Method 1: Everytime NEW Approval  
🔸 Add Start and wait for an approval, configure Title and Assigned to as usual, and optionally set a Timeout value (for example 29 days) in the action settings to control when the timeout should be raised.[web:3][web:8][web:25]  
🔸 After the approval action, add Update item that sets TriggerFlow back to Yes and configure its run after settings so it runs only when the approval action has timed out, which flips the list item and starts a new run that sends a fresh approval email and creates a new task.[web:3][web:9][web:26]

3. Method 2: Start and Wait for the SAME Approval  
🔸 Add a Condition that checks if the ApprovalID column in the SharePoint item is empty and, if it is, use Create an approval to build a new approval and then Update item to write the Approval ID into the ApprovalID column, otherwise use a Compose action to read the existing ApprovalID so it can be reused.[web:3][web:6][web:8]  
🔸 Under the condition, add Wait for an approval and supply the Approval ID value so the action always waits on the correct approval, then add an Update item with run after set only to has timed out that sets TriggerFlow to Yes to restart the flow when the wait action times out.[web:3][web:8][web:9]  
🔸 Add a separate success branch for Wait for an approval configured to run on is successful, place your real post-approval business logic there, and finish with an Update item that clears ApprovalID and keeps TriggerFlow as No so the loop ends cleanly and the item stops retriggering.[web:3][web:6][web:26]

## 🎉 Result

Your approval flows can now effectively run without a hard time limit, because each timeout simply restarts the flow instead of killing the business process.[web:2][web:3] Depending on which method you choose, approvers either receive a new reminder email and a fresh task each cycle or work with a single persistent approval that remains valid while the flow quietly restarts in the background.[web:2][web:3][web:9]

## 🌟 Key Advantages

🔸 Handles the 30-day approval timeout explicitly, avoiding broken runs and hanging approval tasks in long-running business processes.[web:2][web:9][web:21]  
🔸 Lets you choose between stronger visibility via repeated reminder emails or a cleaner user experience with one stable approval in the Approvals center.[web:3][web:6]  
🔸 Uses only standard SharePoint and Approvals capabilities so it works in typical Power Automate environments without special licenses or custom connectors.[web:6][web:8][web:25]

## 🛠️ FAQ

Q1: Why can approvals not simply run longer than 30 days?  
A: Approvals are subject to Power Automate action limits and long-running actions time out after 30 days, so you need restartable patterns like these to keep your business process alive.[web:2][web:5][web:9]

Q2: Why does method 2 split Create an approval and Wait for an approval?  
A: Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused by later runs so the same approval task is tracked across restarts instead of creating new tasks every time.[web:3][web:6][web:8]

Q3: How does TriggerFlow prevent the flow from retriggering endlessly?  
A: The trigger condition only fires when TriggerFlow is Yes and the first Update item immediately sets it to No, so only the dedicated timeout branch that sets TriggerFlow back to Yes can start a new run.[web:7][web:13][web:29]
```

<span style="display:none">[^5_1]</span>

<div align="center">⁂</div>

[^5_1]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md


---

# [https://youtu.be/iTGwT58amFs](https://youtu.be/iTGwT58amFs)

Perfect, then let’s wire this YouTube video into your Markdown tip (Phase 2) using the template rules.

Below is your updated `.md` file with the video section added at the end (using YouTube ID `iTGwT58amFs`):[^6_1][^6_2]

```markdown
---
title: "#PowerPlatformTip 001 – 'Infinite Approvals beyond 30 days'"
date: 2025-11-25
categories:
    - Article
    - PowerPlatformTip
tags:
    - PowerAutomate
    - PowerApps
    - Dataverse
    - Governance
    - PowerPlatformTip
excerpt: "Infinite Approvals lets you build Power Automate approval flows that survive beyond the 30-day timeout limit by safely restarting themselves. You can either send a fresh approval request after each timeout or restart the flow while still waiting on the original approval so the first email link and task remain valid."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

Standard Power Automate approval actions time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals.[web:2][web:3] When the approval action times out, the flow run stops and you cannot continue to wait for the decision or automatically resume the process.[web:2][web:9]

## ✅ Solution

Use a SharePoint list with two helper columns to control when the flow is allowed to trigger and, for the advanced pattern, to store the current Approval ID.[web:3][web:6] On top of this, implement one of two patterns: either create a brand-new approval whenever the previous one times out or restart the flow and keep waiting on the same approval task by reusing its Approval ID.[web:3][web:6][web:9]

## 🔧 How It's Done

1. Prepare SharePoint and the trigger  
🔸 Add a Yes/No column TriggerFlow with default Yes and a Single line of text column ApprovalID to your SharePoint list, then use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is set to Yes.[web:3][web:7][web:13]  
🔸 Make the very first action after the trigger an Update item that sets TriggerFlow to No so any further edits during the run cannot re-trigger the flow and create infinite loops.[web:3][web:7]

2. Method 1: Everytime NEW Approval  
🔸 Add Start and wait for an approval, configure Title and Assigned to as usual, and optionally set a Timeout value (for example 29 days) in the action settings to control when the timeout should be raised.[web:3][web:8][web:25]  
🔸 After the approval action, add Update item that sets TriggerFlow back to Yes and configure its run after settings so it runs only when the approval action has timed out, which flips the list item and starts a new run that sends a fresh approval email and creates a new task.[web:3][web:9][web:26]

3. Method 2: Start and Wait for the SAME Approval  
🔸 Add a Condition that checks if the ApprovalID column in the SharePoint item is empty and, if it is, use Create an approval to build a new approval and then Update item to write the Approval ID into the ApprovalID column, otherwise use a Compose action to read the existing ApprovalID so it can be reused.[web:3][web:6][web:8]  
🔸 Under the condition, add Wait for an approval and supply the Approval ID value so the action always waits on the correct approval, then add an Update item with run after set only to has timed out that sets TriggerFlow to Yes to restart the flow when the wait action times out.[web:3][web:8][web:9]  
🔸 Add a separate success branch for Wait for an approval configured to run on is successful, place your real post-approval business logic there, and finish with an Update item that clears ApprovalID and keeps TriggerFlow as No so the loop ends cleanly and the item stops retriggering.[web:3][web:6][web:26]

## 🎉 Result

Your approval flows can now effectively run without a hard time limit, because each timeout simply restarts the flow instead of killing the business process.[web:2][web:3] Depending on which method you choose, approvers either receive a new reminder email and a fresh task each cycle or work with a single persistent approval that remains valid while the flow quietly restarts in the background.[web:2][web:3][web:9]

## 🌟 Key Advantages

🔸 Handles the 30-day approval timeout explicitly, avoiding broken runs and hanging approval tasks in long-running business processes.[web:2][web:9][web:21]  
🔸 Lets you choose between stronger visibility via repeated reminder emails or a cleaner user experience with one stable approval in the Approvals center.[web:3][web:6]  
🔸 Uses only standard SharePoint and Approvals capabilities so it works in typical Power Automate environments without special licenses or custom connectors.[web:6][web:8][web:25]

## 🛠️ FAQ

Q1: Why can approvals not simply run longer than 30 days?  
A: Approvals are subject to Power Automate action limits and long-running actions time out after 30 days, so you need restartable patterns like these to keep your business process alive.[web:2][web:5][web:9]

Q2: Why does method 2 split Create an approval and Wait for an approval?  
A: Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused by later runs so the same approval task is tracked across restarts instead of creating new tasks every time.[web:3][web:6][web:8]

Q3: How does TriggerFlow prevent the flow from retriggering endlessly?  
A: The trigger condition only fires when TriggerFlow is Yes and the first Update item immediately sets it to No, so only the dedicated timeout branch that sets TriggerFlow back to Yes can start a new run.[web:7][web:13][web:29]

## 🎥 Video Tutorial

{% include video id="iTGwT58amFs" provider="youtube" %}
```

If you want, next step is Phase 3: a standalone HTML newsletter version pointing to the same YouTube URL.
<span style="display:none">[^6_10][^6_11][^6_12][^6_13][^6_14][^6_15][^6_16][^6_17][^6_18][^6_19][^6_20][^6_21][^6_3][^6_4][^6_5][^6_6][^6_7][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: https://www.youtube.com/watch?v=h6Eb-F0P6Hs

[^6_2]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md

[^6_3]: https://www.galaxus.ch/de/s1/product/hpe-usv-5-intl-tower-ups-750va-525-va-525-w-line-interaktiv-usv-usv-21358246

[^6_4]: https://www.galaxus.ch/en/s1/product/rittal-ritt-wall-mounted-cooling-unit-server-cabinet-accessories-33917705

[^6_5]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^6_6]: https://learn.microsoft.com/en-us/power-automate/modern-approvals

[^6_7]: https://www.matthewdevaney.com/extend-a-power-automate-approval-over-the-30-day-limit/

[^6_8]: https://www.youtube.com/watch?v=aipuaVgoQLU

[^6_9]: https://www.youtube.com/watch?v=Tg5fIHYVUwQ

[^6_10]: https://manueltgomes.com/microsoft/power-automate-long-running-flows/

[^6_11]: https://www.youtube.com/watch?v=Vp570S6Plt8

[^6_12]: https://community.powerplatform.com/forums/thread/details/?threadid=67224820-73e8-46f3-9396-894b841d5a28

[^6_13]: https://www.youtube.com/watch?v=I9a40JD5Y0I

[^6_14]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^6_15]: https://www.youtube.com/watch?v=pIf0lqjJsbQ

[^6_16]: https://www.youtube.com/watch?v=r8jk5xigpQg

[^6_17]: https://www.youtube.com/watch?v=_FhVphEkgCA

[^6_18]: https://www.linkedin.com/pulse/approval-timeouts-microsoft-power-automate-petter-skodvin-hvammen

[^6_19]: https://www.youtube.com/watch?v=lH7rb9ZyM-c

[^6_20]: https://www.youtube.com/watch?v=J70yKyTjgJ0

[^6_21]: https://www.youtube.com/watch?v=owfZc2U7xtI


---

# lass [web:... weg

Alles klar, hier ist die bereinigte Markdown-Datei ohne die `[web:…]`‑Verweise:

```markdown
---
title: "#PowerPlatformTip 001 – 'Infinite Approvals beyond 30 days'"
date: 2025-11-25
categories:
    - Article
    - PowerPlatformTip
tags:
    - PowerAutomate
    - PowerApps
    - Dataverse
    - Governance
    - PowerPlatformTip
excerpt: "Infinite Approvals lets you build Power Automate approval flows that survive beyond the 30-day timeout limit by safely restarting themselves. You can either send a fresh approval request after each timeout or restart the flow while still waiting on the original approval so the first email link and task remain valid."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

Standard Power Automate approval actions time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals. When the approval action times out, the flow run stops and you cannot continue to wait for the decision or automatically resume the process.

## ✅ Solution

Use a SharePoint list with two helper columns to control when the flow is allowed to trigger and, for the advanced pattern, to store the current Approval ID. On top of this, implement one of two patterns: either create a brand-new approval whenever the previous one times out or restart the flow and keep waiting on the same approval task by reusing its Approval ID.

## 🔧 How It's Done

1. Prepare SharePoint and the trigger  
🔸 Add a Yes/No column TriggerFlow with default Yes and a Single line of text column ApprovalID to your SharePoint list, then use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is set to Yes.  
🔸 Make the very first action after the trigger an Update item that sets TriggerFlow to No so any further edits during the run cannot re-trigger the flow and create infinite loops.

2. Method 1: Everytime NEW Approval  
🔸 Add Start and wait for an approval, configure Title and Assigned to as usual, and optionally set a Timeout value (for example 29 days) in the action settings to control when the timeout should be raised.  
🔸 After the approval action, add Update item that sets TriggerFlow back to Yes and configure its run after settings so it runs only when the approval action has timed out, which flips the list item and starts a new run that sends a fresh approval email and creates a new task.

3. Method 2: Start and Wait for the SAME Approval  
🔸 Add a Condition that checks if the ApprovalID column in the SharePoint item is empty and, if it is, use Create an approval to build a new approval and then Update item to write the Approval ID into the ApprovalID column, otherwise use a Compose action to read the existing ApprovalID so it can be reused.  
🔸 Under the condition, add Wait for an approval and supply the Approval ID value so the action always waits on the correct approval, then add an Update item with run after set only to has timed out that sets TriggerFlow to Yes to restart the flow when the wait action times out.  
🔸 Add a separate success branch for Wait for an approval configured to run on is successful, place your real post-approval business logic there, and finish with an Update item that clears ApprovalID and keeps TriggerFlow as No so the loop ends cleanly and the item stops retriggering.

## 🎉 Result

Your approval flows can now effectively run without a hard time limit, because each timeout simply restarts the flow instead of killing the business process. Depending on which method you choose, approvers either receive a new reminder email and a fresh task each cycle or work with a single persistent approval that remains valid while the flow quietly restarts in the background.

## 🌟 Key Advantages

🔸 Handles the 30-day approval timeout explicitly, avoiding broken runs and hanging approval tasks in long-running business processes.  
🔸 Lets you choose between stronger visibility via repeated reminder emails or a cleaner user experience with one stable approval in the Approvals center.  
🔸 Uses only standard SharePoint and Approvals capabilities so it works in typical Power Automate environments without special licenses or custom connectors.

## 🛠️ FAQ

Q1: Why can approvals not simply run longer than 30 days?  
A: Approvals are subject to Power Automate action limits and long-running actions time out after 30 days, so you need restartable patterns like these to keep your business process alive.

Q2: Why does method 2 split Create an approval and Wait for an approval?  
A: Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused by later runs so the same approval task is tracked across restarts instead of creating new tasks every time.

Q3: How does TriggerFlow prevent the flow from retriggering endlessly?  
A: The trigger condition only fires when TriggerFlow is Yes and the first Update item immediately sets it to No, so only the dedicated timeout branch that sets TriggerFlow back to Yes can start a new run.

## 🎥 Video Tutorial

{% include video id="iTGwT58amFs" provider="youtube" %}
```

Wenn du willst, mache ich dir jetzt noch Phase 3 als HTML-Newsletter ohne die Referenzen.

---

# ja

Hier ist Phase 3: ein eigenständiger HTML-Newsletter (z.B. für systeme.io) ohne `[web:…]`, mit CTA auf dein YouTube‑Video.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>#PowerPlatformTip 001 – Infinite Approvals beyond 30 days</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
      color: #111827;
      background-color: #f9fafb;
      margin: 0;
      padding: 0;
    }
    .wrapper {
      max-width: 720px;
      margin: 0 auto;
      padding: 24px 16px 40px;
      background-color: #ffffff;
    }
    h1, h2, h3 {
      color: #0f172a;
      margin-top: 1.6em;
      margin-bottom: 0.4em;
    }
    h1 {
      font-size: 24px;
    }
    h2 {
      font-size: 20px;
    }
    h3 {
      font-size: 17px;
    }
    p {
      margin: 0.4em 0;
    }
    ul {
      padding-left: 1.2em;
      margin: 0.4em 0 0.8em;
    }
    li {
      margin: 0.2em 0;
    }
    .tagline {
      font-size: 14px;
      color: #4b5563;
      margin-bottom: 16px;
    }
    .badge {
      display: inline-block;
      padding: 2px 8px;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-radius: 999px;
      background-color: #ecfeff;
      color: #0f766e;
      margin-bottom: 8px;
    }
    .cta {
      display: inline-block;
      margin: 18px 0 8px;
      padding: 10px 18px;
      background-color: #0f766e;
      color: #ffffff !important;
      text-decoration: none;
      border-radius: 999px;
      font-size: 14px;
      font-weight: 600;
    }
    .cta:hover {
      background-color: #115e59;
    }
    .meta {
      font-size: 12px;
      color: #6b7280;
      margin-bottom: 8px;
    }
    .hashtags {
      font-size: 13px;
      color: #4b5563;
      margin-top: 18px;
    }
    .divider {
      border-top: 1px solid #e5e7eb;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <div class="badge">#PowerPlatformTip 001</div>
    <h1>Infinite Approvals beyond 30 days</h1>
    <p class="tagline">
      Build approval flows in Power Automate that safely survive the 30-day timeout limit – either with fresh reminders or by keeping the original approval task alive.
    </p>
    <p class="meta">
      Scenario: Long-running approvals for contracts, legal reviews, or executive decisions.
    </p>

    <h2>💡 Challenge</h2>
    <p>
      Standard approval actions in Power Automate time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals.
    </p>
    <p>
      Once the approval action times out, the flow run stops and you cannot continue to wait for the decision or automatically resume the business process.
    </p>

    <h2>✅ Solution</h2>
    <p>
      Use a SharePoint list with two helper columns to control when the flow is allowed to trigger and, for the advanced pattern, to store the current Approval ID.
    </p>
    <p>
      On top of this, implement one of two patterns: either create a brand-new approval whenever the previous one times out or restart the flow and keep waiting on the same approval task by reusing its Approval ID.
    </p>

    <h2>🔧 How it’s done</h2>

    <h3>1) Prepare SharePoint and the trigger</h3>
    <ul>
      <li>
        Add a Yes/No column <strong>TriggerFlow</strong> with default <strong>Yes</strong> and a Single line of text column <strong>ApprovalID</strong> to your SharePoint list.
      </li>
      <li>
        Use the trigger <strong>When an item is created or modified</strong> and configure a trigger condition like:<br />
        <code>@equals(triggerOutputs()?['body/TriggerFlow'], true)</code>
      </li>
      <li>
        Make the first action after the trigger an <strong>Update item</strong> that sets <strong>TriggerFlow</strong> to <strong>No</strong> so any edits during the run cannot re-trigger the flow and create infinite loops.
      </li>
    </ul>

    <h3>2) Method 1 – “Everytime NEW Approval”</h3>
    <p>
      This pattern restarts the process with a completely new approval whenever the previous one times out.
    </p>
    <ul>
      <li>
        Add <strong>Start and wait for an approval</strong>, configure Title and Assigned to, and optionally set a <strong>Timeout</strong> value (for example 29 days) in the action settings.
      </li>
      <li>
        After the approval action, add <strong>Update item</strong> that sets <strong>TriggerFlow</strong> back to <strong>Yes</strong>.
      </li>
      <li>
        In <strong>Configure run after</strong> for this Update item, choose only <strong>has timed out</strong> so it runs exclusively when the approval has timed out and then retriggers the flow.
      </li>
    </ul>
    <p>
      Result: If there is no response within the timeout window, the flow flips TriggerFlow to Yes, restarts, and sends a fresh approval email and task.
    </p>

    <h3>3) Method 2 – “Start and Wait for the SAME Approval”</h3>
    <p>
      This pattern restarts the flow on timeout but continues to wait on the original approval using its stored Approval ID.
    </p>
    <ul>
      <li>
        Add a <strong>Condition</strong> that checks if <strong>ApprovalID</strong> is empty.
      </li>
      <li>
        If empty:
        <ul>
          <li>Use <strong>Create an approval</strong> to create a new approval.</li>
          <li>Store the returned <strong>Approval ID</strong> in the SharePoint <strong>ApprovalID</strong> column via <strong>Update item</strong>.</li>
        </ul>
      </li>
      <li>
        If not empty:
        <ul>
          <li>Use a <strong>Compose</strong> action to read the existing <strong>ApprovalID</strong> from SharePoint.</li>
        </ul>
      </li>
      <li>
        Below the condition, add <strong>Wait for an approval</strong> and supply the Approval ID so the action always waits on the correct approval task.
      </li>
      <li>
        After <strong>Wait for an approval</strong>, add an <strong>Update item</strong> with run after configured only for <strong>has timed out</strong>, and set <strong>TriggerFlow</strong> back to <strong>Yes</strong> to restart the flow when the wait action times out.
      </li>
      <li>
        Add a separate success branch for <strong>Wait for an approval</strong> that runs on <strong>is successful</strong>, executes your post-approval logic, then clears <strong>ApprovalID</strong> and keeps <strong>TriggerFlow</strong> as <strong>No</strong>.
      </li>
    </ul>
    <p>
      Result: Each timeout only restarts the flow, while the original approval task and email link remain valid for the approver.
    </p>

    <div class="divider"></div>

    <h2>🎉 Result</h2>
    <p>
      Your approval flows can now run effectively without a hard time limit, because each timeout is handled by a controlled restart instead of breaking the process.
    </p>
    <p>
      Depending on your chosen method, approvers either receive fresh reminder emails and tasks every cycle or work with a single persistent approval that stays valid while the flow quietly restarts in the background.
    </p>

    <h2>🌟 Key Advantages</h2>
    <ul>
      <li>
        Explicitly handles the 30-day approval timeout and avoids broken runs in long-running processes.
      </li>
      <li>
        Lets you choose between more visibility (new reminder emails) and a cleaner user experience (one stable approval in the Approvals center).
      </li>
      <li>
        Uses only standard SharePoint and Approvals actions, so it works in typical Power Automate environments without special licenses.
      </li>
    </ul>

    <h2>🛠️ FAQ</h2>
    <p><strong>Q1: Why can approvals not simply run longer than 30 days?</strong></p>
    <p>
      Cloud flows and their actions have a maximum run duration, so long-running approval waits will time out after roughly 30 days. Restartable patterns like these are needed to keep the business process alive.
    </p>

    <p><strong>Q2: Why does method 2 split “Create an approval” and “Wait for an approval”?</strong></p>
    <p>
      Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused on every new run so the same approval task is tracked across restarts instead of creating new tasks each time.
    </p>

    <p><strong>Q3: How does TriggerFlow prevent the flow from retriggering endlessly?</strong></p>
    <p>
      The trigger condition only fires when TriggerFlow is set to Yes, and the very first Update item sets it to No. Only the dedicated timeout branch sets TriggerFlow back to Yes, so you stay in full control of when the flow restarts.
    </p>

    <div class="divider"></div>

    <h2>🎥 Watch the walkthrough</h2>
    <p>
      Want to see the pattern in action, step by step in the Power Automate designer?
    </p>
    <p>
      <a class="cta" href="https://youtu.be/iTGwT58amFs" target="_blank" rel="noopener noreferrer">
        Watch on YouTube
      </a>
    </p>
    <p style="font-size: 12px; color: #6b7280;">
      The video shows both variants: “Everytime NEW Approval” and “Start and Wait for the SAME Approval”, including TriggerFlow, ApprovalID and run-after configuration.
    </p>

    <p class="hashtags">
      #PowerPlatform #PowerAutomate #SharePoint #Approvals #PowerPlatformTip
    </p>
  </div>
</body>
</html>
```

Wenn du willst, passe ich dir jetzt noch Titel, Hashtags oder den CTA-Text auf deinen Newsletter-Stil an.
<span style="display:none">[^8_1][^8_10][^8_11][^8_12][^8_13][^8_14][^8_15][^8_16][^8_17][^8_18][^8_19][^8_2][^8_20][^8_3][^8_4][^8_5][^8_6][^8_7][^8_8][^8_9]</span>

<div align="center">⁂</div>

[^8_1]: https://365corner.pl/2020/12/02/how-to-overcome-the-power-automate-approvals-30-days-limit/

[^8_2]: https://learn.microsoft.com/en-us/power-automate/approvals-known-issues

[^8_3]: https://www.youtube.com/watch?v=h6Eb-F0P6Hs

[^8_4]: https://rapidcircle.com/how-to-configure-long-running-approvals-in-power-automate/

[^8_5]: https://www.matthewdevaney.com/extend-a-power-automate-approval-over-the-30-day-limit/

[^8_6]: https://community.powerplatform.com/forums/thread/details/?threadid=930fd4a4-5eb0-44cb-95c8-d30330b74d4f

[^8_7]: https://community.powerplatform.com/galleries/gallery-posts/?postid=e72ebe73-0201-4d20-977c-e42249cc3ad1

[^8_8]: https://www.linkedin.com/pulse/approval-timeouts-microsoft-power-automate-petter-skodvin-hvammen

[^8_9]: https://www.reddit.com/r/PowerPlatform/comments/1e7wwz3/approvals_infinite_loop/

[^8_10]: https://learn.microsoft.com/en-us/power-automate/modern-approvals

[^8_11]: https://www.youtube.com/watch?v=r8jk5xigpQg

[^8_12]: https://www.matthewdevaney.com/the-hidden-multi-level-approval-feature-in-power-automate/

[^8_13]: https://tomriha.com/how-to-handle-long-term-tasks-in-power-automate/

[^8_14]: https://members.collab365.com/c/microsoft365_forum/overcoming-power-automate-30-day-limits

[^8_15]: https://www.dev4side.com/en/casi-di-successo/power-automate-endless-approval-flows

[^8_16]: https://davegerrard.wordpress.com/2021/05/07/power-automate-long-running-approval-flow/

[^8_17]: https://nboldapp.com/5-power-automate-approval-flow-errors-fix-guide/

[^8_18]: https://learn.microsoft.com/en-us/power-automate/limits-and-config

[^8_19]: https://manueltgomes.com/microsoft/power-automate-long-running-flows/

[^8_20]: https://www.reddit.com/r/PowerPlatform/comments/1ag4kr9/best_practice_help_for_approval_workflows/

