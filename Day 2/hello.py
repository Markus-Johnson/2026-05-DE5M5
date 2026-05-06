import pandas as pd

print("hello world")

import pandas as pd
import os

os.chdir(r"C:\Users\Admin\Desktop\DE5M5\2026-05-DE5M5\Day 2")

books_df = pd.read_csv("03_Library Systembook.csv")
customers_df = pd.read_csv("03_Library SystemCustomers.csv")

print("Books loaded (raw):", books_df.shape)

# ── Remove all empty rows before anything else ──────────────────
books_df = books_df.dropna(how='all')
customers_df = customers_df.dropna(how='all')

print("Books loaded (after removing empty rows):", books_df.shape)
print("Customers loaded (after removing empty rows):", customers_df.shape)

# ── Functions ───────────────────────────────────────────────────
def clean_dates(df):
    df['Book checkout'] = df['Book checkout'].str.replace('"', '')
    df['Book checkout'] = pd.to_datetime(df['Book checkout'], dayfirst=True, errors='coerce')
    df['Book Returned'] = pd.to_datetime(df['Book Returned'], dayfirst=True, errors='coerce')
    return df

def calculate_borrow_days(df):
    df['Days Borrowed'] = (df['Book Returned'] - df['Book checkout']).dt.days
    return df

def flag_late_returns(df):
    df['Returned Late'] = df['Days Borrowed'] > 14
    return df

def flag_errors(df):
    df['Date Error'] = df['Days Borrowed'] < 0
    return df

# ── Call the functions ──────────────────────────────────────────
books_df = clean_dates(books_df)
books_df = calculate_borrow_days(books_df)
books_df = flag_late_returns(books_df)
books_df = flag_errors(books_df)

# ── Remove rows where dates are still missing after cleaning ────
books_df = books_df.dropna(subset=['Book checkout', 'Book Returned'])

print("Books final row count:", books_df.shape)

# ── Print results ───────────────────────────────────────────────
print("\nCleaned books preview:")
print(books_df[['Books', 'Book checkout', 'Book Returned', 'Days Borrowed', 'Returned Late', 'Date Error']].to_string())