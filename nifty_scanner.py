from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

import yfinance as yf
import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIGURATION ---
SHEET_NAME = 'nifty50_n50_trading_dry_test'
WORKSHEET_NAME = 'category'
JSON_KEYFILE = JSON_KEYFILE = '/content/drive/MyDrive/ai_agent/silicon-synapse-371016-63e6efa16ed3.json'



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

