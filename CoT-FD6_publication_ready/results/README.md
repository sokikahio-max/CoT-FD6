# Results

This directory contains compact summary tables extracted from the reported experiment.

Included in this cleaned package:

- `paper_reported_summary.csv` — headline manuscript values.
- `api_summary_reported.csv` — API call/token/latency/cost summary from the executed notebook.
- `trace_sensitivity_reported.csv` — reported N=3/5/10 trace sensitivity summary.
- `baseline_reported.csv` — conventional baseline metrics from the reported run.
- `ablation_reported_summary.csv` — compact ablation summary.
- `explanation_reported_summary.csv` — grounding and RF-SHAP correspondence.
- `nasa_confusion_reported.csv` — like-for-like NASA confusion counts.
- `temporal_reported_summary.csv` — per-engine temporal summary.
- `figures/` — destination for regenerated paper figures.

## Before the GitHub/Zenodo release

For maximum reproducibility, copy the **authoritative result files from the original
reported run** into this directory. The cleaned notebook expects/produces files including:

- `baseline_metrics.csv`
- `cotfd6_main_predictions.csv`
- `cotfd6_main_raw_traces.csv`
- `cotfd6_main_metrics_by_repeat.csv`
- `cotfd6_main_metrics_mean_sd.csv`
- `trace_sensitivity_predictions.csv`
- `trace_sensitivity_metrics.csv`
- `ablation_predictions.csv`
- `ablation_metrics.csv`
- `secondary_experiment_raw_traces.csv`
- `memory_only_full100_predictions.csv`
- `memory_only_full100_summary.csv`
- `rf_shap_top_features.csv`
- `rf_shap_global_importance.csv`
- `explanation_grounding_summary.csv`
- `nasa_raw_confusion_counts.csv`
- `nasa_cost_sensitivity.csv`
- `nasa_governance_accepted_confusion.csv`
- `nasa_temporal_diagnostic_stability.csv`
- `nasa_temporal_raw_traces.csv`
- `nasa_temporal_unit_summary.csv`
- `nasa_temporal_overall_summary.csv`
- `api_cost_latency_summary.csv`

Do **not** use the removed legacy `export_all()` helper from the exploratory notebook.
That helper serialized in-memory runtime lists and could overwrite persistent authoritative
checkpoints after a runtime restart.

### Trace-count sensitivity

The executed trace-sensitivity experiment used `use_memory=True`; training-only analogical
memory remained enabled while N was varied. The API audit also records
`trace_sensitivity` with `use_memory=True`.
