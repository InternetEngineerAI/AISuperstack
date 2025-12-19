# KF_STEP2_INDUSTRY — Select Industry

===================================================
STEP PURPOSE
===================================================
This step captures the target industry for which sales leads
will be generated.

The industry value is used across all downstream steps
(AI prompts, merging, exports, routing).

===================================================
EXECUTION RULES
===================================================
- STEP 2 can only execute after STEP 1 is completed.
- Language MUST already be set (EN or ES).
- Do NOT assume an industry.
- Accept free-form industry input.
- Do NOT limit the user to predefined industries.
- Normalize but do NOT reinterpret the industry.
- Persist the industry as session state.
- If input is missing or unclear, re-prompt.

===================================================
VALID INPUTS
===================================================
Accepted formats include:
- Single industry name
- Industry + specialization
- Industry in English or Spanish

Examples (EN):
- "Real Estate"
- "Marketing Agencies"
- "Construction Contractors"
- "Law Firms"
- "Medical Clinics"

Examples (ES):
- "Bienes Raíces"
- "Agencias de Marketing"
- "Contratistas de Construcción"
- "Despachos de Abogados"
- "Clínicas Médicas"

===================================================
NORMALIZATION RULES
===================================================
- Trim whitespace.
- Preserve user wording.
- Do NOT translate the industry.
- Store exactly as provided after trimming.

Persist as:
Session.Industry = "<NormalizedIndustry>"

===================================================
SYSTEM BEHAVIOR
===================================================
1. Prompt user to enter the target industry.
2. Validate that input is not empty.
3. Normalize input.
4. Persist industry in session state.
5. Confirm the industry in the user’s selected language.
6. Advance to STEP 3 — Target Location.

===================================================
USER PROMPT
===================================================
If Language = "EN":
"What industry would you like to generate leads for?"

If Language = "ES":
"¿Para qué industria te gustaría generar leads?"

===================================================
CONFIRMATION MESSAGE
===================================================
If Language = "EN":
"Industry set to: <NormalizedIndustry>."

If Language = "ES":
"Industria configurada: <NormalizedIndustry>."

===================================================
INVALID INPUT HANDLING
===================================================
If input is empty or unclear:

EN:
"Please enter a valid industry (for example: Real Estate, Law Firms, Contractors)."

ES:
"Por favor ingresa una industria válida (por ejemplo: Bienes Raíces, Despachos de Abogados, Contratistas)."

===================================================
STEP TRANSITION
===================================================
After successful completion:
- Lock STEP 2 as completed.
- Proceed to STEP 3.
- Load: KF_STEP3_LOCATION.prompt.md
