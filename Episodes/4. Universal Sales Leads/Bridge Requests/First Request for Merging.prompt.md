The next knowledge file we need to create the prompt for is KF_STEP5_MERGE.
We need to guide the user to execute this step inside Gemini since it can take advantage of Google Maps USPS Address normalization and other enrichment features.


I will upload multiple CSV files at the same time. The number of files may vary, and their filenames may vary.
Your tasks:
• Detect ALL uploaded CSV files.
• Read every CSV file uploaded simultaneously.
• Merge all rows from all uploaded files into one unified master dataset.
• Remove ALL duplicates using:

CompanyName (fuzzy match allowed)
Phone
Address
Website
• Normalize addresses to USPS standards.
• Validate phone and email formatting.
• Tag each lead with a Segment value such as:
• Enrich leads when publicly available information exists:
Owner
Buyer / Procurement
Main contact email/phone
• Create a unique LeadId for each row in this format:
YSMC-{YYYYMMDD}-{sequence}
Final Output:
Produce a downloadable CSV file named:
Cleaned_Leads_{YYYYMMDD}.csv
Use EXACT headers in this order:
LeadId, CompanyName, Segment, ContactName, Phone, Email, Website,
Address, City, State, PostalCode, Country
In your response:
• First, output ONLY the final CSV inside a ```csv:disable-run
• Include ONE short sentence telling the user here are the merged leads
• Include ONE short sentence telling the user they can open it in Excel or upload it to Google Sheets to view and edit it.
• Display this link exactly as written:
https://sheets.google.com/
Do not include any other explanations or commentary.


Please also create the neccesary instructions in Spanish, but leave the CSV column headers in English.