from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='pl-PL', tz=360)

keywords = [
    "mieszkanie na sprzedaż kraków",
    "wynajem mieszkania kraków",
    "kawalerka kraków",
    "apartament kraków",
    "dom na sprzedaż kraków",
    "ceny mieszkań kraków",
    "rynek nieruchomości kraków",
    "agencja nieruchomości kraków",
    "studio kraków",
    "kupno mieszkania kraków",
    "wynajem pokoju kraków",
]

pytrends.build_payload(
    keywords
    geo='PL',
    timeframe='today 12-m'
)

if 'isPartial' in df.columns:
    df = df.drop(columns=['isPartial'])

output_path = 'krakow_housing_search_trends.csv'
df = pytrends.interest_over_time()

print(f'Saved {len(df)} rows to {output_path}')