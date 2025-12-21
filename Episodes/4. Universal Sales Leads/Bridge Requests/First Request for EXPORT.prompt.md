We are going to work on KF_STEP6_EXPORT_SELECT.prompt.md

Now we need to allow the end user to select an export option.
1. Export to dialer
2. Export to driving route

If the user chooses Export to dialer:
We will support 3 dialers (RingOver,ReadyMode,Generic)

These are the fields each dialer supports:
RingOver: number, name, company, email, address, city, state, zip, country, notes, custom_1, custom_2
ReadyMode: phone, first_name, last_name, company, address, city, state, postal_code, country, list_name, notes
Generic: phone, company, first_name, last_name, title, email, address, city, state, zip, country, timezone, notes, external_id

The export to dialer prompt will be executed inside of Gemini, right after the lead merge in Gemini. 
So we need to create a prompt for the user to copy and paste and execute in Gemini.

Also inside the prompt for Gemini include this text: 

Save the export to Google Sheets
https://sheets.google.com/



If the user chooses Export to driving route:
1. We need to inform the user that he needs to download the leads from Gemini
2. Then upload the leads to https://geocod.io and choose USPS ZIP+4 template
3. They can watch the instructions at https://www.youtube.com/watch?v=AkUQKfhNaEE
4. Once https://geocod.io is done attaching Latitude and Longitude we need to reupload the leads to Gemini in order to take advante of Google Maps functionality.
5. Gemini needs to reorganize the leads in order to optimize the driving route. Calculate the shortest distance from one lead to the next.
6. We also need to add the following fields to support step 4: StopNumber, DistanceToNext_miles, EstimatedDriveTime_minutes, GoogleMapsLink https://www.google.com/maps/search/?api=1&query={Latitude},{Longitude}
7. The export format needs to be in this order: CompanyName, ContactName, Address, City, State, PostalCode, Country, Phone, Email, Website, Geocodio Latitude, Geocodio Longitude, StopNumber, DistanceToNext_miles, EstimatedDriveTime_minutes, GoogleMapsLink

All of this needs to be in a prompt for the user to copy and paste and execute in Gemini.

We also need a version for Spanish, but keep the field names in English.