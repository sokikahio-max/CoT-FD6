# Publication cleanup notes

The attached experimental notebook contained the complete working history of the major-revision
analysis. This repository version was cleaned for public release without changing the reported
scientific outputs.

## Removed from the public notebook

- exploratory smoke tests and pilot experiments not used in the manuscript;
- diagnostic/debug print cells;
- duplicated Figure 2 generation;
- personal Google Drive paths;
- saved notebook outputs and widget state;
- legacy `export_all()` code that could overwrite persistent checkpoints from partially populated
  in-memory lists.

## Methodological cleanup

A legacy `BETA`-weighted verifier-selection helper was present in the working notebook. It was
not the final manuscript governance rule: the final main experiment explicitly overwrote that
intermediate selection with the raw modal LLM label and applied the independent verifier only
for support/conflict/governance. The public notebook therefore removes `BETA` and the legacy
selection helper entirely. The public `aggregate()` function returns only the raw modal LLM
diagnosis; `governance_decision()` independently computes the verifier diagnosis and
accept/escalate disposition.

This makes the code directly match the final methodology while preserving the behaviour that
generated the reported main, ablation, and temporal results.

## Important trace-sensitivity provenance note

The actual executed trace-sensitivity code used training-only analogical memory (`use_memory=True`)
while varying only the number of sampled traces. This is also visible in the persistent API audit.
Any manuscript sentence describing that experiment as "no-memory" or "memory disabled" should
be corrected before submission; no rerun is needed because the reported values already correspond
to the memory-enabled experiment.
