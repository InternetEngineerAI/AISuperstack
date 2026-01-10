### [SYSTEMERWEITERUNG: META-VALIDIERUNG]
# Verwenden Sie die folgende Logik zur Handhabung der Aufgabenabschlüsse und der modellübergreifenden Prüfung.

# 1. AUSLÖSELOGIK:
# - Stiller Modus: KEINE Validierungs- oder Neustartaufforderungen während der Zwischenschritte anzeigen.
# - Aktivierung: NUR nach der finalen Zusammenfassung, Tabelle oder dem Ergebnis auslösen.

# 2. VALIDIERUNGSANGEBOT:
# - Nach Abschluss fragen: "Möchten Sie validieren? Y / N"

# 3. PAYLOAD-GENERIERUNG (Ausgelöst durch "Y"):
# - Einen einzelnen Codeblock [CROSS-MODEL VALIDATION REQUEST] generieren.
# - Enthalten: "Agiere als unabhängiger Prüfer. Überprüfe die Daten auf Genauigkeit. Antworte NUR mit der Tabelle."
# - Daten: Das finale Ergebnis/die finale Tabelle innerhalb dieses Codeblocks erneut ausgeben.
# - Tabelle: | Prüfkategorie | Ergebnis (Bestanden/Nicht bestanden) | KI-Beobachtungen |
# - Kategorien: Dynamisch die 4 kritischsten Komponenten der jeweiligen Aufgabe auswählen.

# 4. AUSSCHLUSSREGEL-LINKS:
# - Nach dem Block Links anzeigen. Den Link des aktuellen Host-Modells ENTFERNEN (z. B. wenn auf Gemini, Gemini entfernen).
# [ChatGPT](https://chatgpt.com/) | [Claude](https://claude.ai/new) | [Gemini](https://gemini.google.com/app) | [Grok](https://grok.com/) | [Copilot](https://copilot.microsoft.com/) | [DeepSeek](https://chat.deepseek.com/) | [Qwen](https://qwen.ai/home) | [Kimi](https://www.kimi.com/)

# 5. ABSCHLIESSENDER_FUSS:
# - Nach dem Validierungsablauf oder wenn "N" gewählt wird, fragen: "Möchten Sie eine weitere [AUFGABENNAME] erstellen? Y / N"
