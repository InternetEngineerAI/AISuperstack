# KF_GLOBAL_COMMANDS — Global Command Handling

===================================================
PURPOSE
===================================================
This file defines global commands that can be triggered
by the user at ANY time during the workflow.

Global commands override the current step logic and must
be handled immediately.

===================================================
SUPPORTED GLOBAL COMMANDS
===================================================

--------------------------------
HELP COMMANDS
--------------------------------

HELP TRIGGERS (case-insensitive):
- help
- ayuda

BEHAVIOR:
- Display the full help and usage guidance.
- Show current step number (if applicable).
- Show workflow overview.
- Display available global commands.
- Do NOT advance or change the current step.
- Do NOT repeat the current step prompt automatically.
- Load and display:
  KF_GUIDELINES.prompt.md

--------------------------------
GO BACK COMMANDS
--------------------------------

GO BACK TRIGGERS (case-insensitive):
- go back
- goback
- volver
- atrás
- atras
- regresar

BEHAVIOR:
- Decrease the current step by 1.
- Minimum allowed step value is 1.
- If already at STEP 1, remain at STEP 1.
- Do NOT display internal step variables unless HELP was requested.
- Redisplay the previous step prompt in the user’s selected language (EN or ES).
- Do NOT skip validation rules of the previous step.

===================================================
PRIORITY RULES
===================================================
- Global commands ALWAYS take priority over step logic.
- Global commands can be triggered at any time.
- Step execution MUST pause while a global command is handled.
- After handling a global command, return control to the workflow.

===================================================
LANGUAGE HANDLING
===================================================
- Detect the user’s selected language.
- Respond in EN or ES accordingly.
- Command keywords may be entered in either language.
- Command keywords must NEVER be translated internally.

===================================================
CONSTRAINTS
===================================================
- Do NOT invent new global commands.
- Do NOT ask the user to confirm global commands.
- Do NOT chain multiple global commands.
- Handle ONE command per user message.
- If multiple commands appear, prioritize HELP over GO BACK.

===================================================
ERROR HANDLING
===================================================
- If a command is partially matched but ambiguous, ignore it.
- If no valid global command is detected, continue normal step execution.

===================================================
END OF FILE
===================================================
