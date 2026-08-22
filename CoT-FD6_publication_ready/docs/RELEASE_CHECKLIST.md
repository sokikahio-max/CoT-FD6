# GitHub / Zenodo release checklist

1. **Correct the manuscript trace-sensitivity description before submission.**
   The executed N=3/5/10 sensitivity run used training-only analogical memory (`use_memory=True`).
   Replace any statement saying memory was disabled/no-memory for that experiment.

2. Replace the old GitHub repository contents with this cleaned package.

3. Add the authoritative reported-run result CSVs from the original persistent results folder.
   See `results/README.md`.

4. Do **not** upload:
   - `OPENAI_API_KEY` or any `.env` file;
   - `data/train_FD001.txt` unless NASA's redistribution terms explicitly permit your intended use;
   - exploratory pilot/smoke outputs that are not part of the paper.

5. Choose and add a software license if desired.

6. Run:
   ```bash
   python scripts/pre_release_check.py
   ```

7. Commit the cleaned repository and create a versioned tag/release, e.g. `v2.0.0`.

8. Archive the release with Zenodo.

9. After Zenodo issues the new DOI:
   - add the DOI to `CITATION.cff`;
   - add it to `README.md`;
   - update the manuscript Data and Code Availability statement;
   - if using `.zenodo.json`, add the DOI only after Zenodo has assigned it.

10. Re-run the pre-release check and inspect the public GitHub page from a logged-out/private browser session.
