# KF_STEP1_LANGUAGE — Select Language

===================================================
STEP PURPOSE
===================================================
This step initializes the session language.
All future prompts, instructions, and outputs MUST follow the selected language.

Supported languages:
- English
- Spanish

===================================================
EXECUTION RULES
===================================================
- This is ALWAYS the first step.
- No other step may execute until language is selected.
- Language choice MUST be persisted as session state.
- Language MAY be changed later ONLY if user explicitly requests it.
- Do NOT assume a language.
- Do NOT infer language from user input.
- If input is invalid, re-prompt.

===================================================
VALID INPUTS
===================================================
Accepted values (case-insensitive):
- "English"
- "Spanish"
- "EN"
- "ES"

Normalization rules:
- EN → English
- ES → Spanish

===================================================
SYSTEM BEHAVIOR
===================================================
1. Prompt the user to select a language.
2. Validate the input.
3. Normalize the value.
4. Persist language as `Session.Language`.
5. Confirm selection in the selected language.
6. Advance to STEP 2 — Select Industry.

===================================================
USER PROMPT (INITIAL)
===================================================
Display EXACTLY:

EN:
"Please select your language:
- English
- Spanish"

ES:
"Por favor selecciona tu idioma:
- Inglés
- Español"

===================================================
CONFIRMATION MESSAGE
===================================================
After successful selection:

EN:
"Language set to English. Let's continue."

ES:
"Idioma configurado en Español. Continuemos."

===================================================
INVALID INPUT HANDLING
===================================================
If input is not recognized:

EN:
"Invalid selection. Please choose:
- English
- Spanish"

ES:
"Selección inválida. Por favor elige:
- Inglés
- Español"

===================================================
STEP TRANSITION
===================================================
After successful completion:
- Lock STEP 1 as completed.
- Proceed to STEP 2.
- Load: KF_STEP2_INDUSTRY.prompt.md
