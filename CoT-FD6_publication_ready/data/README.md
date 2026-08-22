# Data

## NASA C-MAPSS FD001

The NASA C-MAPSS FD001 source file is **not redistributed in this repository**.

Download the turbofan degradation data from the NASA Prognostics Data Repository:

https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/

Place the FD001 training file here as:

```text
data/train_FD001.txt
```

Alternatively set:

```bash
COTFD6_NASA_PATH=/absolute/path/to/train_FD001.txt
```

The paper uses the run-to-failure training trajectories and constructs retrospective
Healthy/Degraded labels at each window end using:

```text
degraded: RUL <= 30 cycles
healthy : RUL > 30 cycles
```

RUL is used only to construct the retrospective benchmark label. It is not supplied
to the LLM, analogical retrieval, prototype verifier, or conventional classifiers.

## Synthetic motor-fault data

The synthetic dataset is generated programmatically by the reproducibility notebook.
No separate source file is required.
