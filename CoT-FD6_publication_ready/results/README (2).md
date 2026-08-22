# CoT-FD6 Curated Experimental Results

This directory contains the manuscript-facing result files selected from the full experiment archive for public GitHub/Zenodo release. The selection keeps the files needed to support the main predictive, retrieval, ablation, explanation, governance, temporal, and computational-cost analyses while excluding pilot, duplicate, and legacy aggregate exports.

## Contents

- `results/` — 28 authoritative CSV result files plus a public experiment configuration.
- `MANIFEST.csv` — row/column counts, file sizes, SHA-256 hashes, and a short purpose statement for every published file.

## Result groups

**Main experiment:** `cotfd6_main_predictions.csv`, `cotfd6_main_raw_traces.csv`, `cotfd6_main_metrics_by_repeat.csv`, `cotfd6_main_metrics_mean_sd.csv`, `baseline_metrics.csv`.

**Trace sensitivity and ablation:** `trace_sensitivity_predictions.csv`, `trace_sensitivity_metrics.csv`, `ablation_predictions.csv`, `ablation_metrics.csv`, `secondary_experiment_raw_traces.csv`.

**Training-only retrieval and leakage checks:** `full100_memory_only_predictions.csv`, `full100_memory_only_summary.csv`, `full100_llm_vs_memory_by_repeat.csv`, `memory_integrity_instance_audit.csv`, `memory_integrity_summary.csv`.

**Explanation analyses:** `rf_shap_top_features.csv`, `rf_shap_global_importance.csv`, `llm_shap_feature_overlap.csv`, `llm_shap_feature_overlap_summary.csv`, `explanation_grounding_summary.csv`.

**NASA governance and cost analysis:** `nasa_raw_confusion_counts.csv`, `nasa_cost_sensitivity.csv`, `nasa_governance_accepted_confusion.csv`.

**Temporal analysis:** `nasa_temporal_diagnostic_stability.csv`, `nasa_temporal_unit_summary.csv`, `nasa_temporal_overall_summary.csv`, `nasa_temporal_raw_traces.csv`.

**Computational reporting:** `api_cost_latency_summary.csv`.

**Configuration:** `experiment_config.json`. The public configuration contains only parameters active in the manuscript-facing workflow. The original exploratory notebook contained a legacy `BETA=0.5` setting associated with an earlier verifier-selection implementation; the final governance rule does not use this parameter, so it is intentionally omitted here.

## Files intentionally excluded from the public results set

The following files from the full working archive were not copied because they are pilot outputs, redundant summaries, narrow debugging/audit derivatives already represented by retained files, or a legacy aggregate export:

- `a4_memory_disagreement_summary.csv`
- `a4_memory_per_repeat_comparison.csv`
- `a4_vs_memory_only.csv`
- `full100_like_for_like_baselines.csv`
- `nasa_cost_sensitivity_summary.csv`
- `nasa_main_final_metrics_by_repeat.csv`
- `nasa_pilot_verification_audit.csv`
- `real_pilot_predictions.csv`
- `real_pilot_summary.csv`
- `reasoning_traces_and_grounding.csv`
- `synthetic_main_final_metrics_by_repeat.csv`


## Reproducibility note

The raw main, secondary, and temporal trace files are retained so the stochastic summaries can be independently audited without publishing the much larger legacy combined `reasoning_traces_and_grounding.csv` export. The NASA C-MAPSS FD001 source dataset is not redistributed here; users should obtain it from the NASA Prognostics Data Repository.
