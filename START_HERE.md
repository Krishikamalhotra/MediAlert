# Start Here

## Run the application

1. Install Python 3.11 or newer.
2. Open PowerShell in this folder and run:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python -m streamlit run app.py
   ```

3. Open the local address printed by Streamlit (normally `http://localhost:8501`).
4. Use the sidebar to open the seven app views. The trained model is included, so training is not needed to launch the app.

The Patient Risk Assessment view accepts a single illustrative encounter and returns a model score with local SHAP contributions. Use **Clear Form** to remove the previous result and restore the default form. The score is a research output for the benchmark label, not a clinical risk estimate.

The form does not search for or replay a saved patient row: it transforms the entered values with the saved preprocessing pipeline and sends that feature vector to the trained model. The holdout test records were not used to fit the model, but came from the same 1999–2008 source dataset. This is evidence of performance on held-out records from that source, not validation on new hospitals or current patients. The holdout PR-AUC is 0.1479 against an 8.98% positive prevalence, so prediction quality is limited and correctness for any one entered profile is not guaranteed.

## Reproduce the experiment

The project ZIP includes the UCI source archive and extracted tables, along with the final cohort, trained pipeline, notebooks, metrics, and figures. To rebuild from the extracted source files:

```powershell
python src/data_loader.py
python src/preprocessing.py
python src/feature_engineering.py
python src/eda.py
python src/train.py
python src/evaluate.py
python src/explainability.py
```

The model search uses stratified three-fold cross-validation inside the 80% training partition. An untouched 20% holdout is used for final evaluation. The binary decision threshold comes from training out-of-fold predictions. Results are in `reports/` and the run metadata is in `models/model_metadata.json`.

## Important data note

The supplied `hospital-patient-records-sample.csv` is a separate 25-row synthetic example with no readmission outcome. The application and reported experiment instead use the UCI Diabetes 130-US Hospitals for Years 1999–2008 dataset in the supplied ZIP. Its `<30` field is used as the positive label; the source does not identify planned versus unplanned returns or provide encounter dates to confirm that the first row per patient is chronologically earliest.

