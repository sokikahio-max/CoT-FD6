# CoT-FD6

Reproducibility resources for:

**Explainable LLM-Assisted Fault Diagnosis for Smart Manufacturing Using Multi-Trace Diagnostic Rationales and Verification**

Authors: **Kahiomba Sonia Kiangala** and **Zenghui Wang**  
Affiliation: University of South Africa (UNISA)

## Overview

CoT-FD6 is an LLM-assisted diagnostic-support framework for smart manufacturing. It combines:

1. training-derived standardized sensor features;
2. training-only analogical retrieval;
3. multiple explicit structured diagnostic rationales;
4. raw modal LLM diagnosis aggregation and cross-trace agreement;
5. an independent deterministic prototype verifier; and
6. accept-or-escalate governance based on LLM/verifier agreement.

The verifier **does not replace or correct the raw LLM diagnosis**. Disagreement triggers human
review. Generated rationales are treated as observable model outputs and are **not** claimed to
reveal hidden chain-of-thought.

## Main reported findings

On the common 100-instance NASA FD001 subset, Logistic Regression, SVM-RBF, and Random Forest
achieved 0.920, 0.920, and 0.930 accuracy, respectively. The raw LLM diagnosis achieved
`0.618 ± 0.018`. Agreement-based governance produced `0.900 ± 0.008` selective accuracy at
`0.660 ± 0.020` coverage. Retrieval-only classification achieved 0.860 accuracy.

On the controlled synthetic task, the raw LLM diagnosis achieved approximately
`0.998 ± 0.004` accuracy and macro-F1.

See `results/paper_reported_summary.csv` for compact reported values.

## Repository structure

```text
CoT-FD6/
├── README.md
├── requirements.txt
├── CITATION.cff
├── .zenodo.json
├── .env.example
├── config/
│   └── experiment_config.json
├── data/
│   └── README.md
├── docs/
│   ├── REPRODUCIBILITY.md
│   ├── PUBLICATION_CLEANUP.md
│   └── RELEASE_CHECKLIST.md
├── notebooks/
│   └── CoTFD6_Reproducibility.ipynb
├── prompts/
│   ├── system_prompt.txt
│   ├── user_prompt_template.txt
│   ├── training_reference_template.txt
│   ├── synthetic_task.txt
│   └── nasa_fd001_task.txt
├── results/
│   ├── README.md
│   ├── paper_reported_summary.csv
│   ├── api_summary_reported.csv
│   ├── trace_sensitivity_reported.csv
│   └── figures/
└── scripts/
    └── pre_release_check.py
```

## Quick start

```bash
git clone https://github.com/sokikahio-max/CoT-FD6.git
cd CoT-FD6

python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
jupyter lab
```

Open `notebooks/CoTFD6_Reproducibility.ipynb`.

### NASA FD001

NASA data are not redistributed. Download the C-MAPSS FD001 file from the NASA Prognostics
Data Repository and place `train_FD001.txt` in `data/`. See `data/README.md`.

### OpenAI API reruns

Paid LLM runs are disabled by default. To rerun them, set:

```bash
export OPENAI_API_KEY="..."
export COTFD6_RUN_LLM=1
```

Never commit API keys.

## Frozen LLM configuration

| Parameter | Value |
|---|---:|
| Model snapshot | `gpt-4.1-mini-2025-04-14` |
| Temperature | 0.70 |
| Top-p | 1.0 |
| Maximum output tokens | 600 |
| Main traces per instance | 5 |
| Main repetitions | 5 |
| Analogical neighbours | 3 |
| Self-trust alpha | 0.50 |
| Prototype temperature tau | 1.0 |
| Evidence-direction epsilon | 0.25 |

Full configuration: `config/experiment_config.json`.

## Important trace-sensitivity detail

The **executed** N=3/5/10 trace-sensitivity experiment retained training-only analogical memory
while varying only N. This is documented in the cleaned notebook and API audit. See
`docs/PUBLICATION_CLEANUP.md`.

## Result files

The compact reported summaries included here are not substitutes for the archived raw result
files. Before the definitive GitHub/Zenodo release, add the authoritative CSV checkpoints from
the reported run to `results/`. The expected files are listed in `results/README.md`.

## Reproducibility and interpretation

See `docs/REPRODUCIBILITY.md` for exact workflow, data partitioning, API-run safeguards,
stochasticity, checkpointing, and cost interpretation.

## Citation

A `CITATION.cff` file is included. Update it with the new Zenodo DOI after creating the release.

## License

No software license has been selected in this package. Choose and add a license before public
release if you want others to have explicit reuse rights. MIT is a common choice for research
code, but the licensing decision belongs to the authors.
