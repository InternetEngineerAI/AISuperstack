# KF_GUIDELINES — Usage Rules & Workflow Help

===================================================
PURPOSE
===================================================
This file defines user-facing guidance, workflow visibility,
and behavior when HELP or GO BACK is triggered.

This file does NOT control step logic.
It only displays guidance and enforces navigation rules.

===================================================
LANGUAGE-SPECIFIC DISPLAY
===================================================

--------------------------------
IF Language = "EN"
--------------------------------

Display:
"You are currently on Step <CurrentStep>."

Show these guidance lines:
- "Start anytime with: start"
- "Restart the workflow with: restart"
- "Go back one step with: Go Back"
- "Geocoding Instructions: https://www.youtube.com/watch?v=AkUQKfhNaEE"
- "Full GPT Diagram: https://github.com/InternetEngineerAI/AISuperstack/blob/main/Episodes/4.%20Universal%20Sales%20Leads/Diagrams/Diagram.pdf"

Show this workflow summary:
"Workflow: 1. Language → 2. Industry → 3. Location → 4. AI Prompts → 5. Lead Merge → 6. Export Selection → 7. Export Behavior"

--------------------------------
SI EL IDIOMA = "ES"
--------------------------------

Mostrar:
"Actualmente estás en el Paso <CurrentStep>."

Mostrar estas líneas de guía:
- "Comienza en cualquier momento con: start"
- "Reinicia el flujo de trabajo con: restart"
- "Regresa un paso con: Go Back"
- "Instrucciones de geocodificación: https://www.youtube.com/watch?v=AkUQKfhNaEE"
- "Diagrama completo del GPT: https://github.com/InternetEngineerAI/AISuperstack/blob/main/Episodes/4.%20Universal%20Sales%20Leads/Diagrams/Diagrama.pdf"

Mostrar este resumen del flujo de trabajo:
"Flujo de trabajo: 1. Idioma → 2. Industria → 3. Ubicación → 4. Prompts de IA → 5. Unión de Leads → 6. Selección de Exportación → 7. Comportamiento de Exportación"

===================================================
WHEN THE USER TRIGGERS "GO BACK"
===================================================

- Decrease CurrentStep by 1
- Minimum allowed value = 1
- Do NOT display the words "CurrentStep" unless the user typed a HELP command
- Redisplay the previous step in the user’s selected language (EN or ES)
