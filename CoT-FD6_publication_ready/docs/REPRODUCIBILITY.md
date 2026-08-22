# Reproducibility guide

## 1. Environment

The manuscript reports Python 3.12. Create a clean environment:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
python -m ipykernel install --user --name cotfd6 --display-name "CoT-FD6"
```

The original Google Colab run did not record exact package patch versions. The repository
therefore gives compatible package ranges rather than inventing a lock file that was not
used in the reported experiment.

## 2. NASA data

Download NASA C-MAPSS FD001 from the NASA Prognostics Data Repository and place:

```text
data/train_FD001.txt
```

See `data/README.md`.

## 3. OpenAI API

The reported experiments used:

- model snapshot: `gpt-4.1-mini-2025-04-14`
- temperature: `0.70`
- top-p: `1.0`
- maximum output tokens: `600`

Store the API key only in the environment:

```bash
export OPENAI_API_KEY="..."
export COTFD6_RUN_LLM=1
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="..."
$env:COTFD6_RUN_LLM="1"
```

Restart the notebook kernel after changing the run flag.

**The notebook does not execute paid API experiments by default.**

## 4. Main experiment

The reported main evaluation used the same fixed held-out 100-instance subset per dataset:

- 5 independently sampled traces per diagnostic instance;
- 5 complete stochastic repetitions;
- training-only analogical memory enabled;
- raw modal LLM diagnosis retained;
- independent prototype verification;
- LLM/verifier disagreement -> human review.

The verifier never overwrites the raw LLM prediction.

## 5. Trace-count sensitivity

The actual executed sensitivity run varied `N in {3,5,10}` while retaining the
training-only analogical memory (`use_memory=True`). Ten traces were generated once per
instance/repetition and nested prefixes of 3, 5, and 10 were compared.

## 6. Ablation

The four variants are:

- A1: one trace, no memory, no governance;
- A2: five traces, no memory, no governance;
- A3: the same five no-memory traces + independent verification/governance;
- A4: five separately generated memory-conditioned traces + verification/governance.

A1-A3 reuse the same stochastic no-memory trace set. A4 requires separate calls because
retrieved references change the prompt.

## 7. Temporal analysis

NASA temporal stability uses three held-out engines and five genuinely distinct windows
per engine around the retrospective healthy/degraded boundary. RUL is evaluation metadata
only and is never supplied to the LLM.

## 8. Costs and stochasticity

The reported cost estimate uses frozen historical rates of USD 0.40/1M input tokens and
USD 1.60/1M output tokens. Those values are experiment metadata, not current pricing.

Even with the same model snapshot and prompt, stochastic API outputs may not reproduce
bit-for-bit. The paper therefore reports mean ± SD across repeated sampling where applicable.

## 9. Frozen results vs rerunning

For exact manuscript verification, use the archived result CSVs from the reported run.
Rerunning the LLM experiments is a reproduction attempt, not a replacement for the archived
observations.
