"""Find every capitalised word in sample_text.txt and list the different ones."""

import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
text = (DATA_DIR / "sample_text.txt").read_text(encoding="utf-8")

capital_words = re.findall(r"\b[A-Z][a-z]*\b", text)
print("Total capitalised words:", len(capital_words))
print("Different words:", sorted(set(capital_words)))
