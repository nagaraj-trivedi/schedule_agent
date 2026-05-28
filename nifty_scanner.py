import yfinance as yf
import pandas as pd
import numpy as np

# Nifty 50 Tickers
nifty_50 = [
    'ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 
    'BAJFINANCE', 'BAJAJFINSV', 'BEL', 'BHARTIARTL', 'CIPLA', 'COALINDIA', 
    'DRREDDY', 'EICHERMOT', 'ETERNAL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 
    'HDFCLIFE', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDIGO', 'INFY', 
    'ITC', 'JIOFIN', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 
    'MAXHEALTH', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 
    'SBILIFE', 'SHRIRAMFIN', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 
    'TMPV', 'TATASTEEL', 'TECHM', 'TITAN', 'TRENT', 'ULTRACEMCO', 'WIPRO'
]

def get_nifty_data():
    results = {i: [] for i in range(1, 18)}
    dmas = [5, 10, 20, 50, 100, 150, 200]
    
    for ticker in nifty_50:
        try:
            df = yf.Ticker(f"{ticker}.NS").history(period="1y")
            if df.empty: continue
            
            # Ensure precision by rounding
            for d in dmas: df[f'DMA_{d}'] = df['Close'].rolling(window=d).mean()
            
            c = round(float(df['Close'].iloc[-1]), 4)
            vals = {d: round(float(df[f'DMA_{d}'].iloc[-1]), 4) for d in dmas}
            
            # Logic: Price relative to DMAs
            above = {d: c > vals[d] for d in dmas}
            count = sum(above.values())
            
            # Category 1-6 (Ascent)
            if count == 1 and above[5]: results[1].append(ticker)
            if count == 2 and above[5] and above[10]: results[2].append(ticker)
            if count == 3 and above[5] and above[10] and above[20]: results[3].append(ticker)
            if count == 4 and above[5] and above[10] and above[20] and above[50]: results[4].append(ticker)
            if count == 5 and above[5] and above[10] and above[20] and above[50] and above[100]: results[5].append(ticker)
            if count == 6 and above[5] and above[10] and above[20] and above[50] and above[100] and above[150]: results[6].append(ticker)
            
            # Categories 7-16 (Momentum & Filtered)
            if count == 7: results[7].append(ticker)
            if count == 0: results[11].append(ticker)
            if vals[10] > vals[20]: results[8].append(ticker)
            if vals[20] > vals[50]: results[9].append(ticker)
            if vals[50] > vals[100]: results[10].append(ticker)
            if df['Volume'].iloc[-1] < (0.5 * df['Volume'].rolling(20).mean().iloc[-1]): results[12].append(ticker)
            
            # Category 17: Mean-Reversion/Deep Value
            lt_avg = np.mean([vals[d] for d in [10, 20, 50, 100, 150, 200]])
            pct_diff = (c - lt_avg) / lt_avg
            if above[5] and -0.03 <= pct_diff <= 0:
                results[17].append(ticker)
                    
        except Exception: continue
    return results

# Execute and Display
scan_results = get_nifty_data()
for cat, stocks in scan_results.items():
    if stocks:
        print(f"Category {cat}: {', '.join(stocks)}")
