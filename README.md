# MediAlert

**Predictive intelligence for a historical hospital readmission benchmark**

MediAlert is a research prototype that explores whether routinely recorded encounter characteristics can rank the likelihood of a recorded readmission within 30 days. It combines a reproducible data pipeline, four machine-learning classifiers, SHAP explanations, and a seven-view Streamlit application.

> **Research-only notice:** MediAlert is not a medical device and has not been clinically validated. Its probabilities and risk bands must not guide diagnosis, discharge, access to care, or treatment. SHAP values describe model behavior and do not show cause and effect.

## Dataset decision

The directory contains two different sources. The ZIP contains the UCI **Diabetes 130-US Hospitals for Years 1999–2008** benchmark: 101,766 encounters, 50 columns in the supplied CSV, and 71,518 unique patient identifiers. The independent `hospital-patient-records-sample.csv` contains 25 synthetic DataVix example rows. That small sample has no readmission target and is not used to train or evaluate the model. The project therefore studies the UCI benchmark rather than claiming to use a 55,500-row synthetic dataset.

The UCI field `readmitted` has `NO`, `>30`, and `<30` values. MediAlert labels `<30` as positive and the other two categories as negative. The source does not distinguish planned from unplanned returns. It is historical, de-identified health-record data, not synthetic DataVix data.

## What is included

- Seven app views: Overview, Patient Risk Assessment, Dataset Explorer, Analytics Dashboard, Model Performance, Explainable AI, and Research & About.
- Cleaning and feature engineering under `src/` with separate raw, interim, and processed data folders.
- Fifteen descriptive EDA figures, model evaluation plots, and global SHAP plots under `reports/figures/`.
- Four tuned classifiers with fold-contained preprocessing, stratified three-fold cross-validation, an untouched 20% holdout, and training-only out-of-fold threshold selection.
- Six reproducible Jupyter notebooks.
- Saved model, preprocessor, metadata, SHAP summary, and background sample under `models/`.
- A research manuscript in Markdown, DOCX, and PDF formats.
- `START_HERE.md` and `PROJECT_COMPLETION_REPORT.md` for launch and delivery details.

## Quick start

Use Python 3.11 or newer. From this directory, create an environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Launch the included trained app:

```powershell
python -m streamlit run app.py
```

The project ZIP includes the trained model and processed cohort, so the app is ready without retraining. To reproduce the pipeline from the extracted UCI files in `data/raw/`, run:

```powershell
python src/data_loader.py
python src/preprocessing.py
python src/feature_engineering.py
python src/eda.py
python src/train.py
python src/evaluate.py
python src/explainability.py
```

Training runs four three-fold parameter searches and a second set of out-of-fold predictions to select binary thresholds. It takes several minutes on a typical desktop. Model selection uses training-fold average precision only. The 20% stratified holdout is reserved for final metrics. One eligible row per patient is retained, so patient identifiers cannot occur in both partitions. The selected row is the first eligible row in source-file order; the source does not provide dates to verify chronology.

## Results and reproducibility

The selected XGBoost model achieved holdout PR-AUC 0.1479, ROC-AUC 0.6159, recall 0.4956, precision 0.1257, F1 0.2005, and accuracy 0.6452. The holdout positive prevalence is 8.98%, so the ranking performance is modest. Full results are in [`reports/model_comparison.csv`](reports/model_comparison.csv) and [`reports/evaluation_metrics.json`](reports/evaluation_metrics.json); run metadata is in [`models/model_metadata.json`](models/model_metadata.json). Confusion-matrix metrics use thresholds chosen from training out-of-fold predictions; ROC-AUC and average precision use holdout probability scores.

Run the automated checks from the project root:

```powershell
python -m unittest tests.test_pipeline -v
```

Streamlit interface checks and live-browser verification are documented in the completion report. The app has been launched and the patient prediction flow and local SHAP explanation have been exercised.

## Project map

```text
app.py                         Streamlit app entry point
config.py                      Paths, colors, target name, and settings
data/raw/                      Extracted UCI source tables
data/interim/                  Cleaned encounter records
data/processed/                Unique-patient model cohort
notebooks/                     Six workflow notebooks
pages/                         Seven app view implementations
src/                           Data, training, evaluation, prediction, SHAP modules
models/                        Trained model, preprocessing, and metadata
reports/                       Dataset profile, metrics, and 20 figures
research/                      Manuscript, DOCX, PDF, and BibTeX references
```

The source dataset and serialized `.pkl` artifacts are ignored by Git to reduce the risk of accidentally publishing demographic health records or executable model files. They are included in the delivered project ZIP. Retain the UCI citation when reusing the benchmark.

## References

- Strack, B. et al. (2014). “Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records.” *BioMed Research International*, 2014, 781670. https://doi.org/10.1155/2014/781670
- UCI Machine Learning Repository. *Diabetes 130-US Hospitals for Years 1999–2008*. https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
- Lundberg, S. M. and Lee, S.-I. (2017). “A Unified Approach to Interpreting Model Predictions.” *Advances in Neural Information Processing Systems*, 30.
- Chen, T. and Guestrin, C. (2016). “XGBoost: A Scalable Tree Boosting System.” *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785–794. https://doi.org/10.1145/2939672.2939785
