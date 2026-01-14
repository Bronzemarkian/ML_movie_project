import unicodedata
import re
import pandas as pd

# directing_jobs = ["Director", "Co-Director", "Assistant Director", 
#                   "Second Unit Director", "Additional Director", "Unit Director", "Segment Director"]
directing_jobs = ["Director", "Co-Director"]

def normalize_title(s: str) -> str:
    # 1. Normalize Unicode (NFKC handles compatibility chars)
    s = unicodedata.normalize("NFKC", s)

    # 2. Lowercase
    s = s.lower()

    # 3. Replace all Unicode whitespace with a normal space
    s = re.sub(r"\s+", " ", s)

    # 4. Normalize dash variants (after NFKC, many are already unified)
    s = s.replace("–", "-").replace("—", "-")

    # 5. Strip leading/trailing space
    return s.strip()


import pycountry
def normalize_country(country):
    """
    Accepts:
    - ISO alpha-2 (US)
    - ISO alpha-3 (USA)
    - English names (United States, Japan)
    Returns:
    - ISO alpha-3 (USA, JPN, ...)
    """
    if not country:
        return None

    try:
        # alpha-2
        c = pycountry.countries.get(alpha_2=country)
        if c:
            return c.alpha_3

        # alpha-3
        c = pycountry.countries.get(alpha_3=country)
        if c:
            return c.alpha_3

        # name
        c = pycountry.countries.search_fuzzy(country)[0]
        return c.alpha_3
    
    except Exception:
        return country
    
# turn categorical values in list into a list of strings
import ast
from typing import List
def cat_to_list(df: pd.DataFrame, columnnames: List[str]):
    for column in columnnames:
        if type(df.loc[0,column]) == str:
            print(column, type(df.loc[0,column]))
            df[column] = df[column].apply(lambda x: ast.literal_eval(x))
    return df


