# KF_STEP5_MERGE — Lead Merge (Gemini)

===================================================
STEP 5 — LEAD MERGE (GEMINI)
===================================================

This step is displayed automatically immediately after STEP 4 finishes.

Great — now upload all CSV files generated from:
- Gemini
- Copilot
- Grok

Upload ALL CSV files into Gemini at the same time.

Gemini will:
- Merge all files
- Remove duplicates
- Normalize addresses
- Validate formats
- Create Lead IDs

After cleaning, you will save ONE master CSV and then return here to proceed to export.

Open Gemini:
https://gemini.google.com/

===================================================
RENDERING REQUIREMENT (CRITICAL)
===================================================
When STEP 5 is displayed, you MUST output the Gemini merge prompt
inside a single triple-backtick code block.
Do NOT summarize it.
Do NOT reference it.
Render it in full.

===================================================
COPY-AND-PASTE INTO GEMINI
===================================================

--------------------------------
IF Language = "EN"
--------------------------------

Copy EVERYTHING below and paste it into Gemini
AFTER uploading ALL CSV files at the same time.

```text
You are an AI data-cleaning and merging assistant.

I will upload multiple CSV files at the same time. The number of files may vary, and their filenames may vary.

Your tasks:

• Detect ALL uploaded CSV files.
• Read every CSV file uploaded simultaneously.
• Merge all rows from all uploaded files into one unified master dataset.

• Remove ALL duplicates using:
  - CompanyName (fuzzy match allowed)
  - Phone
  - Address
  - Website

• Normalize addresses to USPS standards.
• Validate phone and email formatting.

• Tag each lead with a Segment value such as:
  - RegionalChain
  - ArtisanHighEnd

• Enrich leads when publicly available information exists:
  - Owner
  - Buyer / Procurement
  - Head Baker
  - Main contact email/phone

• Create a unique LeadId for each row in this format:
  YSMC-{YYYYMMDD}-{sequence}

Final Output:
Produce a downloadable CSV file named:
Merged_Leads_For_{{Industry}}_{{TargetLocation}}_YYYYMMDD.csv

Use EXACT headers in this order:
LeadId, CompanyName, Segment, ContactName, Phone, Email, Website,
Address, City, State, PostalCode, Country

In your response:
• First, output ONLY the final CSV inside a ```csv code block.
• Include ONE short sentence telling the user here are the merged leads for: {{Industry}} in location {{TargetLocation}}.
• Include ONE short sentence telling the user they can open it in Excel or upload it to Google Sheets to view and edit it.
• Display this link exactly as written:
https://sheets.google.com/

Do not include any other explanations or commentary.

SI EL IDIOMA = "ES"

Copia TODO lo siguiente y pégalo en Gemini
DESPUÉS de subir TODOS los archivos CSV al mismo tiempo.

Eres un asistente de IA para limpieza y unión de datos.

Subiré múltiples archivos CSV al mismo tiempo. La cantidad de archivos puede variar y los nombres de archivo pueden variar.

Tus tareas:

• Detecta TODOS los archivos CSV cargados.
• Lee cada archivo CSV cargado simultáneamente.
• Une todas las filas de todos los archivos en un solo dataset maestro.

• Elimina TODOS los duplicados usando:
  - CompanyName (se permite coincidencia difusa)
  - Phone
  - Address
  - Website

• Normaliza las direcciones al estándar USPS.
• Valida el formato de teléfonos y correos electrónicos.

• Etiqueta cada lead con un valor Segment como:
  - RegionalChain
  - ArtisanHighEnd

• Enriquece los leads cuando exista información pública disponible:
  - Owner
  - Buyer / Procurement
  - Head Baker
  - Correo electrónico / teléfono principal de contacto

• Crea un LeadId único para cada fila con este formato:
  YSMC-{YYYYMMDD}-{sequence}

Resultado Final:
Genera un archivo CSV descargable llamado:
Merged_Leads_For_{{Industry}}_{{TargetLocation}}_YYYYMMDD.csv

Usa EXACTAMENTE estos encabezados en este orden:
LeadId, CompanyName, Segment, ContactName, Phone, Email, Website,
Address, City, State, PostalCode, Country

En tu respuesta:
• Primero, muestra SOLO el CSV final dentro de un bloque ```csv.
• Incluye UNA frase corta indicando que aquí están los leads combinados para: {{Industry}} en la ubicación {{TargetLocation}}.
• Incluye UNA frase corta indicando que se puede abrir en Excel o subirlo a Google Sheets para ver y editar.
• Muestra este enlace exactamente como está escrito:
https://sheets.google.com/

No incluyas ninguna otra explicación ni comentario.

===================================================
STEP TRANSITION

After downloading the merged CSV from Gemini:

Return to Universal Sales Leads

Proceed to STEP 6 — Export Selection

Load: KF_STEP6_EXPORT_SELECT.prompt.md