# KF_STEP3_LOCATION — Target Location

===================================================
STEP PURPOSE
===================================================
This step captures the geographic target area from which
sales leads will be generated.

The location value is used for:
- AI lead extraction prompts
- Lead normalization and merging
- Routing or export logic in later steps

===================================================
EXECUTION RULES
===================================================
- STEP 3 can only execute after STEP 2 is completed.
- Language MUST already be set (EN or ES).
- Do NOT assume a location.
- Accept flexible location scopes.
- Do NOT perform live geocoding.
- Do NOT validate addresses against external services.
- Normalize formatting only.
- Persist location as session state.
- Re-prompt on missing or invalid input.

===================================================
VALID INPUTS
===================================================
Accepted formats include:
- City
- City + State / Region
- ZIP / Postal Code
- Metro Area
- Region or Country

Examples (EN):
- "Miami, FL"
- "90210"
- "Los Angeles Metro"
- "Texas"
- "New York City"

Examples (ES):
- "Miami, Florida"
- "28013"
- "Área Metropolitana de Madrid"
- "Bogotá, Colombia"
- "Ciudad de México"

===================================================
NORMALIZATION RULES
===================================================
- Trim whitespace.
- Preserve user wording.
- Do NOT translate the location.
- Do NOT expand abbreviations.
- Store exactly as provided after trimming.

Persist as:
Session.Location = "<NormalizedLocation>"

===================================================
SYSTEM BEHAVIOR
===================================================
1. Prompt user to enter the target location.
2. Validate that input is not empty.
3. Normalize formatting.
4. Persist location in session state.
5. Confirm the location in the user’s selected language.
6. Advance to STEP 4 — AI Lead Instructions.

===================================================
USER PROMPT
===================================================
If Language = "EN":
"What location would you like to generate leads from?"

If Language = "ES":
"¿Desde qué ubicación te gustaría generar leads?"

===================================================
CONFIRMATION MESSAGE
===================================================
If Language = "EN":
"Location set to: <NormalizedLocation>."

If Language = "ES":
"Ubicación configurada: <NormalizedLocation>."

===================================================
INVALID INPUT HANDLING
===================================================
If input is empty or unclear:

EN:
"Please enter a valid location (city, ZIP code, metro area, or region)."

ES:
"Por favor ingresa una ubicación válida (ciudad, código postal, área metropolitana o región)."

===================================================
STEP TRANSITION
===================================================
After successful completion:
- Lock STEP 3 as completed.
- Proceed to STEP 4.
- Load: KF_STEP4_AI_PROMPTS.prompt.md
