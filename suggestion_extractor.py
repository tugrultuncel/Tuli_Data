#suggestion_extractor.py is used once to identify stable Google Trends topic IDs.

from pytrends.request import TrendReq
import pandas as pd
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Create logger
logger = logging.getLogger(__name__)
logger.info("Starting suggestion extraction")

rows = []
failed_keywords = []

#Initialize pytrends and extract suggestions
pytrends = TrendReq(
    hl='pl-PL',
    tz=360,
)

kw_list = [
    "mieszkania",
    "wynajem",
    "apartment",
    "dom",
    "kavalerka",
    "pokoje"
]

for kw in kw_list:
    try:
        suggestions = pytrends.suggestions(keyword=kw)
        if not suggestions:
            raise ValueError("No suggestions returned")
        for s in suggestions:
            rows.append({
                "keyword":kw,
                "title": s.get('title'),
                "type": s.get('type'),
                "mid": s.get('mid')
            })
        logger.info(
            f'Keyword {kw} processed.\n'
            f'({len(suggestions)}) suggestions fetched.'
        )

    except Exception as e:
        failed_keywords.append(kw)
        logger.error(f'Failed to extract suggestions for keyword: {kw}. Error: {e}')

    time.sleep(1)  # Sleep to avoid hitting rate limits

#Log the number of extracted suggestions
logger.info(f'Extracted {len(rows)} suggestions')

if failed_keywords:
    logger.warning(f'Failed keywords: {failed_keywords}')

#DataFrame creation and saving to CSV
output_file_raw="suggestions_rav.csv"
if rows:
    df = pd.DataFrame(rows)
    df.to_csv(output_file_raw, index=False)
    logger.info(f"Saved raw suggestions to {output_file_raw}")

    if "type" in df.columns:
        df_topics = df[df["type"] == "Temat"].reset_index(drop=True)
        df_topics.to_csv("suggestions_topics_only.csv", index=False)
        logger.info(
            f"Saved {len(df_topics)} topic rows to suggestions_topics_only.csv"
        )
else:
    logger.error("No suggestions collected. CSV files were not created.")