# KF_STEP4_AI_PROMPTS — Multi-AI Lead Extraction Prompts (Gemini / Grok / Copilot)

===================================================
STEP PURPOSE
===================================================
This step outputs copy-ready prompts for external AIs:
- Gemini
- Grok
- Copilot

Prompts MUST be displayed in code boxes for easy copy/paste.
Prompts MUST be selected based on the user’s session language (EN/ES).
Prompts MUST use the user’s selected Industry and Location.

===================================================
EXECUTION RULES
===================================================
- STEP 4 can only execute after STEP 3 is completed.
- Session.Language MUST be set ("EN" or "ES").
- Session.Industry MUST be set.
- Session.Location MUST be set.
- Do NOT modify the prompt text stored in JSON.
- Do NOT rewrite, reformat, translate, or “fix” prompt text.
- Only perform variable replacement at render time:
  - {{Industry}}        ← Session.Industry
  - {{TargetLocation}}  ← Session.Location

===================================================
PROMPT STORAGE (JSON FILES)
===================================================
All prompt text is stored as JSON “files” below.
Retrieval rules:
- If Session.Language = "EN":
  - Load: gemini_en.json, grok_en.json, copilot_en.json
- If Session.Language = "ES":
  - Load: gemini_es.json, grok_es.json, copilot_es.json

Then render the output for the user as:
1) AI Title line (Gemini / Grok / Copilot)
2) AI Link line directly under the title
3) One code block containing the retrieved prompt with variables replaced

IMPORTANT:
- The user-facing output MUST NOT include JSON.
- JSON is internal storage only.
- User sees ONLY the 3 prompts in 3 code blocks.

===================================================
USER-FACING OUTPUT FORMAT (MANDATORY)
===================================================
Output EXACTLY three sections, in this order:

1) Gemini
   Gemini → https://gemini.google.com/
   (prompt in one code block)

2) Grok
   Grok → https://grok.com/
   (prompt in one code block)

3) Copilot
   Copilot → https://copilot.microsoft.com/
   (prompt in one code block)

Code block rules:
- Use a plain triple-backtick code block (no language tag required).
- Do NOT add extra commentary outside the three sections.

===================================================
INTERNAL JSON PROMPT FILES (DO NOT DISPLAY TO USER)
===================================================