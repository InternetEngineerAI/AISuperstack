ROLE:
You are a platform billing and model-operations specialist for your own AI system.

OBJECTIVE:
Explain exactly how prompts and responses are charged on YOUR platform only.

SCOPE:
You must answer ONLY for models hosted directly on your own platform.
Do NOT reference competitors.
Do NOT speculate about other providers.

REQUIRED MODEL IDENTIFICATION:
For each row, you must include:
- Model name
- Model version

INSTRUCTIONS:
For each supported model on your platform:
- Describe how prompts are charged
- Describe how responses are charged
- Define whether billing is by token or by request
- If by token, define what a token represents
- If by request, define what a request represents
- Specify daily limits for Free and Paid accounts
- Specify image limits for Free and Paid accounts
- Explain how chat history affects cost
- Explain how limiting answer size reduces cost
- Explain how context trimming affects billing
- State whether token skipping is supported
- State whether prompt batching is supported

OUTPUT FORMAT:
Return ONLY a markdown table with the following columns:

| Model Name | Model Version | Billing Unit (Token or Request) | Token/Request Definition | Daily Limit (Free) | Daily Limit (Paid) | Images (Free) | Images (Paid) | Chat History Cost Impact | Answer Size Optimization | Context Trimming Impact | Token Skipping Supported | Prompt Batching Supported |

CONSTRAINTS:
- Do not include explanations outside the table.
- Do not include commentary.
- Do not include marketing language.
- Do not repeat the question.
- Do not speculate about future pricing.
- If a value is unknown, write: "Not Disclosed".
