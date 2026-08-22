#!/usr/bin/env python3
"""Lightweight pre-release audit for the CoT-FD6 repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED = [
    "README.md",
    "requirements.txt",
    "CITATION.cff",
    ".zenodo.json",
    "config/experiment_config.json",
    "notebooks/CoTFD6_Reproducibility.ipynb",
    "docs/REPRODUCIBILITY.md",
    "prompts/system_prompt.txt",
    "prompts/user_prompt_template.txt",
    "results/paper_reported_summary.csv",
]

SECRET_PATTERNS = {
    "OpenAI-like key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
}

TEXT_EXTENSIONS = {
    ".py", ".md", ".txt", ".json", ".cff", ".yaml", ".yml",
    ".toml", ".cfg", ".ini", ".csv", ".ipynb"
}

missing = [p for p in EXPECTED if not (ROOT / p).exists()]

secret_hits = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if ".git" in path.parts:
        continue
    if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {
        ".env.example", ".zenodo.json", "CITATION.cff"
    }:
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            secret_hits.append((label, str(path.relative_to(ROOT))))

print("CoT-FD6 pre-release check")
print("=" * 60)

if missing:
    print("Missing expected files:")
    for item in missing:
        print("  -", item)
else:
    print("Expected repository files: OK")

if secret_hits:
    print("\nPotential secrets detected:")
    for label, path in secret_hits:
        print(f"  - {label}: {path}")
else:
    print("Secret-pattern scan: OK")

nasa = ROOT / "data" / "train_FD001.txt"
print("NASA source data committed:", nasa.exists())
if nasa.exists():
    print("  NOTE: the package is configured not to redistribute this file.")

raw_expected = [
    "cotfd6_main_predictions.csv",
    "cotfd6_main_raw_traces.csv",
    "trace_sensitivity_predictions.csv",
    "ablation_predictions.csv",
    "nasa_temporal_diagnostic_stability.csv",
]
missing_raw = [x for x in raw_expected if not (ROOT / "results" / x).exists()]
if missing_raw:
    print("\nAuthoritative raw/checkpoint files not yet added:")
    for item in missing_raw:
        print("  - results/" + item)
    print("Add the original reported-run CSVs before the definitive Zenodo release.")

if missing or secret_hits:
    sys.exit(1)

print("\nBasic repository audit passed.")
