from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

import yfinance as yf
import pandas as pd
import numpy as np
import gspread
import os
from google.oauth2.service_account import Credentials

# --- CONFIGURATION ---
SHEET_NAME = 'nifty50_n50_trading_dry_test'
WORKSHEET_NAME = 'category'
#JSON_KEYFILE = JSON_KEYFILE = '/content/drive/MyDrive/ai_agent/silicon-synapse-371016-63e6efa16ed3.json'

# Instead of hardcoding the path '/content/drive/...', use this:
JSON_KEYFILE = os.getenv("JSON_KEYFILE", "credentials.json")

print("The script is invoked today Sunday at  \n")

current_time = datetime.now()
print(current_time)

current_time = datetime.now().time()
print(current_time)



# 1. Get the current time in UTC
utc_time = datetime.now(ZoneInfo("UTC"))

# 2. Convert it to IST
ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

print(f"UTC Time: {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"IST Time: {ist_time.strftime('%Y-%m-%d %H:%M:%S')}")

 # Setup authentication
scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
creds = Credentials.from_service_account_file(JSON_KEYFILE, scopes=scope)
if creds:
    print("Credentials object created successfully!")
    print(f"Service account email: {creds.service_account_email}")
else:
    print("Credentials object was not created.")
# 1. Authorize the client
client = gspread.authorize(creds)

# 2. Verify by listing sheets
try:
    # Attempt to fetch all spreadsheets the service account has access to
    # Note: Ensure you have shared your Google Sheet with the service account email
    sheets = client.openall()
    print(f"Connection successful! Found {len(sheets)} accessible sheets.")
    for s in sheets:
        print(f"Sheet found: {s.title}")
except Exception as e:
    print(f"Connection failed: {e}")
try:
 
    # Open the sheet
    sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)
    # Verification: Print success message and the sheet title
    print(f"Successfully connected to Spreadsheet: '{spreadsheet.title}'")
    print(f"Successfully connected to Worksheet: '{sheet.title}'")
    
   # Optional: Verify by reading the first cell
   # This proves the script has permission to actually READ the data
   first_cell = sheet.cell(1, 1).value
   print(f"Read test successful. Cell A1 contains: '{first_cell}'")

except gspread.exceptions.SpreadsheetNotFound:
    print(f"Error: The spreadsheet '{SHEET_NAME}' was not found.")
except gspread.exceptions.WorksheetNotFound:
    print(f"Error: The worksheet '{WORKSHEET_NAME}' was not found in '{SHEET_NAME}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

