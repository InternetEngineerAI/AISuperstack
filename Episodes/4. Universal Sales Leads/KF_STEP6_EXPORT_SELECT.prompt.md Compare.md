# KF_STEP6_EXPORT_SELECT — Export Selection (Dialer or Driving Route)

===================================================
STEP PURPOSE
===================================================
This step allows the user to choose how the cleaned leads
(from STEP 5 executed in Gemini) will be exported.

The user must select ONE export option:
1) Export to Dialer
2) Export to Driving Route

===================================================
EXECUTION RULES
===================================================
- STEP 6 can only execute after STEP 5 is completed.
- A cleaned master CSV is assumed to exist in Gemini.
- This step displays COPY-READY prompts only.
- All exports are executed INSIDE Gemini.
- Do NOT execute exports inside ChatGPT.
- Do NOT infer or fabricate data.
- Field names MUST remain in English.
- Dialer field definitions MUST be loaded from JSON schemas.

===================================================
USER SELECTION
===================================================

If Language = "EN":
"How would you like to export your leads?
1) Export to Dialer
2) Export to Driving Route"

If Language = "ES":
"¿Cómo te gustaría exportar tus leads?
1) Exportar a marcador (Dialer)
2) Exportar a ruta de manejo"

===================================================
OPTION A — EXPORT TO DIALER
===================================================

This option exports the cleaned leads into a dialer-specific CSV format.

Supported dialers:
- RingOver
- ReadyMode
- Generic

The user must select ONE dialer.

Dialer field definitions are NOT hard-coded.
They are loaded from JSON schema files:

- RingOver → DIALER_RINGOVER.schema.json
- ReadyMode → DIALER_READYMODE.schema.json
- Generic → DIALER_GENERIC.schema.json

===================================================
RENDERING REQUIREMENT (CRITICAL)
===================================================
When a dialer is selected, you MUST render
the Gemini export prompt in FULL
inside a single triple-backtick code block.
Do NOT summarize it.
Do NOT reference it.
Render it in full.

===================================================
COPY AND PASTE INTO GEMINI — DIALER EXPORT
===================================================

--------------------------------
IF Language = "EN"
--------------------------------

```text
You are an AI data-export assistant.

Dialer Selected: {{Dialer}}

You are provided with:
1) A cleaned lead dataset already loaded in this session
2) A JSON schema that defines the target dialer field structure

Selected Dialer Schema (JSON):
{{DialerSchemaJson}}

Your tasks:

• Load the selected dialer JSON schema.
• Read the field list and field order from the schema.
• Map the cleaned lead dataset to the schema fields.
• Preserve the field order EXACTLY as defined.
• Leave fields blank if no source data exists.
• Do NOT add, remove, or rename fields.

Produce ONE CSV that matches the schema exactly.

• Include ONE short sentence telling the user these are the export leads
in {{Dialer}} format for {{Industry}} location {{TargetLocation}}.
• Display this link exactly as written:
https://sheets.google.com/

Do not include explanations or commentary.

SI EL IDIOMA = "ES"

Eres un asistente de IA para exportación de datos.

Dialer Selected: {{Dialer}}

Se te proporciona:
1) Un dataset de leads ya limpio cargado en esta sesión
2) Un esquema JSON que define la estructura del marcador

Selected Dialer Schema (JSON):
{{DialerSchemaJson}}

Tus tareas:

• Cargar el esquema JSON del marcador seleccionado.
• Leer la lista y el orden de los campos desde el esquema.
• Mapear el dataset limpio a los campos del esquema.
• Respetar EXACTAMENTE el orden de los campos.
• Dejar los campos en blanco si no existe información.
• NO agregar, eliminar ni renombrar campos.

Produce UN solo archivo CSV compatible con el esquema.

• Incluye UNA frase corta indicando que estos son los leads exportados
en formato {{Dialer}} para {{Industry}} en la ubicación {{TargetLocation}}.
• Muestra este enlace exactamente como está escrito:
https://sheets.google.com/

No incluyas explicaciones ni comentarios.

===================================================
DIALER SCHEMA INJECTION (CRITICAL)

When rendering the Gemini dialer-export prompt above, you MUST inject
the correct JSON schema content into {{DialerSchemaJson}} based on the
selected dialer:

If {{Dialer}} = "RingOver", set {{DialerSchemaJson}} to the FULL content of:
DIALER_RINGOVER.schema.json

If {{Dialer}} = "ReadyMode", set {{DialerSchemaJson}} to the FULL content of:
DIALER_READYMODE.schema.json

If {{Dialer}} = "Generic", set {{DialerSchemaJson}} to the FULL content of:
DIALER_GENERIC.schema.json

===================================================
OPTION B — EXPORT TO DRIVING ROUTE

This option creates an optimized driving route.

===================================================
WORKFLOW OVERVIEW

Download your merged leads from Gemini so you can GeoCode them.

Upload the file to:
https://geocod.io

Choose the USPS ZIP+4 template.

Watch instructions:
https://www.youtube.com/watch?v=AkUQKfhNaEE

After Latitude and Longitude are added,
upload the updated file BACK into Gemini.

===================================================
OPEN GEMINI

Open Gemini:
https://gemini.google.com/

===================================================
RENDERING REQUIREMENT (CRITICAL)

When Driving Route is selected, you MUST render
the Gemini route-optimization prompt in FULL
inside a single triple-backtick code block.

===================================================
COPY AND PASTE INTO GEMINI — DRIVING ROUTE
IF Language = "EN"

You are an AI route-optimization assistant.

I have uploaded a CSV file that includes leads
with Latitude and Longitude added via Geocod.io.

Your tasks:

• Reorganize the leads to optimize the driving route.
• Calculate the shortest distance from one stop to the next.
• Determine the most efficient visit order.

Add the following fields:
- StopNumber
- DistanceToNext_miles
- EstimatedDriveTime_minutes
- GoogleMapsLink

GoogleMapsLink format:
https://www.google.com/maps/search/?api=1&query={Latitude},{Longitude}

Final Output Requirements (MANDATORY):

• Output the optimized route data INLINE.
• Do NOT provide a download link.
• Render the FULL optimized route as raw CSV
  inside a single ```csv code block.

• After the CSV code block, include:
  - ONE short sentence telling the user these are the optimized route leads
    for {{Industry}} in location {{TargetLocation}}.
  - ONE short sentence telling the user they can copy the CSV into Excel
    or upload it to Google Sheets to view and edit it.
  - Display this link exactly as written:
    https://sheets.google.com/

SI EL IDIOMA = "ES"

Eres un asistente de IA para optimización de rutas.

He subido un archivo CSV que contiene leads
con Latitud y Longitud agregadas por Geocod.io.

Tus tareas:

• Reorganizar los leads para optimizar la ruta de manejo.
• Calcular la distancia más corta entre cada parada.
• Determinar el orden de visita más eficiente.

Agrega los siguientes campos:
- StopNumber
- DistanceToNext_miles
- EstimatedDriveTime_minutes
- GoogleMapsLink

Formato de GoogleMapsLink:
https://www.google.com/maps/search/?api=1&query={Latitude},{Longitude}

Requisitos de Salida Final (OBLIGATORIOS):

• Muestra los datos de la ruta optimizada EN LÍNEA.
• NO proporciones enlaces de descarga.
• Renderiza la ruta optimizada COMPLETA como CSV
  dentro de un solo bloque ```csv.

• Después del bloque CSV, incluye:
  - UNA frase corta indicando que estos son los leads de ruta optimizada
    para {{Industry}} en la ubicación {{TargetLocation}}.
  - UNA frase corta indicando que el usuario puede copiar el CSV en Excel
    o subirlo a Google Sheets para ver y editar.
  - Muestra este enlace exactamente como está escrito:
    https://sheets.google.com/

===================================================
WORKFLOW COMPLETE

If Language = "EN":
"Your export is complete.
You may download your files or type restart to begin again."

If Language = "ES":
"Tu exportación está completa.
Puedes descargar tus archivos o escribir restart para comenzar de nuevo."