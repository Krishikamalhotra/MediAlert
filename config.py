"""
MediAlert Configuration Module
Centralizes all file paths, styling constants, model hyperparameters, and operational rules.
"""

from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
RESEARCH_DIR = PROJECT_ROOT / "research"
ASSETS_DIR = PROJECT_ROOT / "assets"

# Key Artifact Paths
FINAL_MODEL_PATH = MODELS_DIR / "final_model.pkl"
PREPROCESSOR_PATH = MODELS_DIR / "preprocessor.pkl"
MODEL_METADATA_PATH = MODELS_DIR / "model_metadata.json"
MODEL_COMPARISON_PATH = REPORTS_DIR / "model_comparison.csv"
EVALUATION_METRICS_PATH = REPORTS_DIR / "evaluation_metrics.json"

# Product Branding
APP_TITLE = "MediAlert"
APP_TAGLINE = "Predictive Intelligence. Proactive Care."
APP_VERSION = "1.0.0"

# Design System & Color Palette
COLORS = {
    "primary_bg": "#F5F7FA",
    "secondary_bg": "#FFFFFF",
    "primary_navy": "#15243A",
    "deep_teal": "#176B68",
    "soft_teal": "#DDF1ED",
    "muted_grey": "#788596",
    "border": "#E5EAF0",
    "high_risk": "#D95C5C",
    "moderate_risk": "#D99A42",
    "low_risk": "#3D9275",
}

# Clinical & Modeling Operational Rules
RANDOM_SEED = 42
TARGET_COLUMN = "readmitted_within_30_days"
READMISSION_WINDOW_DAYS = 30

# Risk Stratification Thresholds (Research Baseline - Non-diagnostic)
RISK_THRESHOLDS = {
    "low": (0.0, 0.25),
    "moderate": (0.25, 0.55),
    "high": (0.55, 1.0),
}

# Evaluation Metric Definitions
EVAL_METRICS = [
    "Accuracy",
    "Precision",
    "Recall (Sensitivity)",
    "Specificity",
    "F1-Score",
    "ROC-AUC",
    "PR-AUC",
]

# Models to Train and Compare
MODEL_CANDIDATES = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "XGBoost",
]
