# CoT-FD6: Chain-of-Thought Fault Diagnosis for Industry 6.0

This repository contains the core code and data used in the experiments for:

> **CoT-FD6: A Chain-of-Thought Reasoning Framework for Cognitive Fault Diagnosis in Industry 6.0**

Two main experimental pipelines are included:

- **Synthetic motor fault dataset**  
  `notebooks/CoTFD6_synthetic_data_working_09122025.ipynb`

- **NASA C-MAPSS Turbofan Engine Dataset (FD001)**  
  `notebooks/CoTFD6_NASAdataset_09122015.ipynb`  
  with data in `data/NASA_CMAPSS/train_FD001.txt`

Both pipelines implement the four-layer CoT-FD6 architecture:

> Perception → Reasoning → Verification → Learning (analogical memory)

## Repository structure

```text
.
├── notebooks/
│   ├── CoTFD6_synthetic_data_working_09122025.ipynb
│   └── CoTFD6_NASAdataset_09122015.ipynb
├── data/
│   └── NASA_CMAPSS/
│       └── train_FD001.txt
├── requirements.txt
├── .gitignore
└── LICENSE



