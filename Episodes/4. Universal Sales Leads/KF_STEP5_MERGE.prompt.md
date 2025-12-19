# KF_STEP5_MERGE — Lead Merge, Dedup, Normalize, Enrich (Run in Gemini)

===================================================
STEP PURPOSE
===================================================
This step merges multiple uploaded CSV lead files into one cleaned master CSV.
This step is designed to be executed inside Gemini to leverage enrichment and
address normalization capabilities.

Run this step in Gemini:
https://gemini.google.com/

===================================================
EXECUTION RULES
===================================================
- STEP 5 can only execute after STEP 4 is completed.
- The user may upload multiple CSV files at once.
- The number of files may vary and filenames may vary.
- Detect ALL uploaded CSV files.
- Read every CSV file uploaded simultaneously.
- Merge ALL rows from ALL uploaded files into one unified master dataset.
- Remove ALL duplicates using:
  - CompanyName (fuzzy match allowed)
  - Phone
  - Address
  - Website
- Normalize addresses to USPS standards.
- Validate phone and email formatting.
- Tag each lead with a Segment value.
- Enrich leads when publicly available information exists:
  - Owner
  - Buyer / Procurement
  - Main contact email/phone
- Create a unique LeadId for each row in this format:
  YSMC-{YYYYMMDD}-{sequence}

===================================================
OUTPUT FILE REQUIREMENTS
===================================================
Produce a downloadable CSV file named:
Cleaned_Leads_{YYYYMMDD}.csv

Use EXACT headers in this order:
LeadId, CompanyName, Segment, ContactName, Phone, Email, Website, Address, City, State, PostalCode, Country

IMPORTANT:
- CSV column headers MUST remain in English for both EN and ES workflows.

===================================================
RESPONSE FORMAT (MANDATORY)
===================================================
In your response:

1) Include ONE short sentence telling the user here are the merged leads.
2) Output ONLY the final CSV inside a:
   ```csv:disable-run
   ...
3) Include ONE short sentence telling the user they can open it in Excel or upload it to Google Sheets to view and edit it.

4) Display this link EXACTLY as written:
https://sheets.google.com/

5) Do NOT include any other explanations or commentary.

===================================================
LANGUAGE-SPECIFIC INSTRUCTIONS
IF Language = "EN"

User-facing instructions (apply exactly):

Detect ALL uploaded CSV files.

Read every CSV file uploaded simultaneously.

Merge all rows from all uploaded files into one unified master dataset.

Remove ALL duplicates using:

CompanyName (fuzzy match allowed)

Phone

Address

Website

Normalize addresses to USPS standards.

Validate phone and email formatting.

Tag each lead with a Segment value.

Enrich leads when publicly available information exists:

Owner

Buyer / Procurement

Main contact email/phone

Create LeadId for each row:
YSMC-{YYYYMMDD}-{sequence}

Response text (EN) MUST be:
Sentence 1 (short):
"Here are the merged leads."

Then the CSV in ```csv:disable-run

Sentence 2 (short):
"You can open this in Excel or upload it to Google Sheets to view and edit."

Then show this link exactly:
https://sheets.google.com/

SI EL IDIOMA = "ES"

Instrucciones para el usuario (aplicar exactamente):

Detecta TODOS los archivos CSV cargados.

Lee cada archivo CSV cargado simultáneamente.

Une todas las filas de todos los archivos en un solo dataset maestro.

Elimina TODOS los duplicados usando:

CompanyName (se permite coincidencia difusa)

Phone

Address

Website

Normaliza las direcciones al estándar USPS.

Valida el formato de teléfonos y correos electrónicos.

Etiqueta cada lead con un valor Segment.

Enriquece los leads cuando exista información pública disponible:

Owner

Buyer / Procurement

Main contact email/phone

Crea un LeadId único por fila con este formato:
YSMC-{YYYYMMDD}-{sequence}

Texto de respuesta (ES) DEBE ser:
Frase 1 (corta):
"Aquí están los leads combinados."

Luego el CSV en ```csv:disable-run

Frase 2 (corta):
"Puedes abrir esto en Excel o subirlo a Google Sheets para ver y editar."

Luego muestra este enlace exactamente:
https://sheets.google.com/

===================================================
STEP TRANSITION

After outputting the merged CSV:

Lock STEP 5 as completed.

Proceed to STEP 6.

Load: KF_STEP6_EXPORT_SELECT.prompt.md