# MediAlert Project Completion Report

**Prepared:** 16 November 2026  
**Status:** Reproducible research prototype and interactive demo completed.

## Dataset and scope

The project folder contains two distinct datasets. The 25-row `hospital-patient-records-sample.csv` is a synthetic DataVix example and has no readmission label. The analysis uses the supplied UCI Diabetes 130-US Hospitals for Years 1999–2008 archive. Its 101,766 encounters and 71,518 patient identifiers are historical de-identified records, not the requested synthetic dataset.

The target is the UCI `readmitted` value `<30`; `>30` and `NO` are grouped as negative. The source does not distinguish planned and unplanned readmissions. Cleaning removes terminal/hospice dispositions and three rows with unknown gender, producing 99,340 records. Feature engineering retains the first eligible record per patient in source-file order, yielding 69,987 rows and 6,285 positive labels (8.98%). Dates are unavailable to verify that source-file order is chronological. Age is available in decade bands and is mapped to band midpoints.

## Model and evaluation

Four classifiers were tuned: Logistic Regression, Decision Tree, Random Forest, and XGBoost. Preprocessing is fitted within each cross-validation fold. Model selection uses three-fold training-only average precision; XGBoost was selected (CV average precision 0.1396). A stratified 20% holdout contains 13,998 rows and was reserved for final scoring. Binary thresholds were selected from training out-of-fold predictions by F1; probability ranking metrics use the holdout scores.

| Model | Holdout PR-AUC | ROC-AUC | Recall | Precision | F1 | Accuracy |
|---|---:|---:|---:|---:|---:|---:|
| XGBoost (selected) | 0.1479 | 0.6159 | 0.4956 | 0.1257 | 0.2005 | 0.6452 |
| Logistic Regression | 0.1432 | 0.6126 | 0.5442 | 0.1217 | 0.1989 | 0.6064 |
| Random Forest | 0.1436 | 0.6101 | 0.3779 | 0.1343 | 0.1981 | 0.7253 |
| Decision Tree | 0.1221 | 0.5839 | 0.4081 | 0.1224 | 0.1884 | 0.6842 |

The holdout positive prevalence is 8.98%; the selected model's PR-AUC is modestly higher. Discrimination is limited and positive predictive value is low at the selected operating point. These results do not establish clinical usefulness, calibration, fairness, external validity, or benefit from intervention. SHAP explanations describe model associations, not causal drivers.

## Delivered components

- Seven-view Streamlit app with dataset, performance, and SHAP views; live risk form; and a local explanation flow.
- Cleaning, feature engineering, training, evaluation, and explainability modules.
- Six workflow notebooks, 15 descriptive EDA charts, three model evaluation charts, and two global SHAP charts.
- Saved XGBoost model, preprocessor, run metadata, SHAP summary, and background sample.
- Research manuscript in Markdown, DOCX, and PDF; bibliography; this completion report; and `START_HERE.md`.
- A project ZIP containing the runnable project and data/model artifacts, excluding unrelated personal CV documents.

## Verification performed

- Pipeline unit tests passed after final model and SHAP artifact regeneration: 8 tests, 0 failures.
- The Streamlit server was launched and the Overview and Patient Risk Assessment views were opened in a browser. A prediction and local SHAP explanation rendered.
- The Clear Form action restored clinical baseline values and removed the prior prediction result; verified in the browser.
- Navigation was exercised across the app views, and the Overview, Dataset Explorer, and Research & About screens were visually inspected.
- EDA and SHAP outputs were regenerated from the final cohort/model.

## Limitations and appropriate use

This is a retrospective benchmark exercise using records from 1999–2008. It lacks external validation and contemporary deployment evaluation. The row-per-patient strategy selects the first eligible source-file row, which may not be the earliest encounter chronologically. The simulated app input fields map to aggregated benchmark features and should not be interpreted as a validated bedside score. It is a research demonstration only and must not be used for diagnosis, discharge, treatment, or access decisions.

## Files to start with

- `START_HERE.md` for installation and run commands.
- `research/research_paper.pdf` for the formatted manuscript.
- `reports/evaluation_metrics.json` and `reports/model_comparison.csv` for holdout metrics.
- `reports/figures/` for analysis and model visualizations.

