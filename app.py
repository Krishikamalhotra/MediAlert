"""
MediAlert: Explainable AI-Based Hospital Readmission Prediction System
Main Streamlit Application Entrypoint
"""

import sys
import json
from pathlib import Path
import plotly.io as pio
import streamlit as st

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import APP_TITLE, APP_TAGLINE, APP_VERSION, COLORS

pio.templates.default = "plotly_white"

metadata_path = PROJECT_ROOT / "models" / "model_metadata.json"
model_metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {}
cohort_path = PROJECT_ROOT / "data" / "processed" / "featured_cohort.csv"
cohort_size = int(model_metadata.get("training_samples", 0)) + int(model_metadata.get("test_samples", 0))
champion_label = model_metadata.get("champion_model", "Not trained")
# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title=f"{APP_TITLE} | {APP_TAGLINE}",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Inject Custom CSS
# ---------------------------------------------------------
css_path = PROJECT_ROOT / "assets" / "custom.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Session State & Navigation Setup
# ---------------------------------------------------------
NAV_OPTIONS = [
    "Overview",
    "Patient Risk Assessment",
    "Dataset Explorer",
    "Analytics Dashboard",
    "Model Performance",
    "Explainable AI",
    "Research & About"
]

NAV_ICONS = {
    "Overview": "🏠",
    "Patient Risk Assessment": "👤",
    "Dataset Explorer": "🗄️",
    "Analytics Dashboard": "📊",
    "Model Performance": "⚙️",
    "Explainable AI": "🔬",
    "Research & About": "ℹ️"
}

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Overview"


# ---------------------------------------------------------
# Persistent Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    # Brand Identity Header
    st.markdown(f"""
    <div style="text-align: center; padding: 12px 0 20px 0;">
        <div style="font-size: 2.4rem; line-height: 1; margin-bottom: 6px;">🩺</div>
        <div style="font-family: 'DM Serif Display', Georgia, serif; font-size: 1.8rem; font-weight: 700; color: #FFFFFF; letter-spacing: -0.02em;">
            Medi<span style="color: #DDF1ED; font-style: italic;">Alert</span>
        </div>
        <div style="font-size: 0.72rem; color: #DDF1ED; opacity: 0.85; letter-spacing: 0.05em; text-transform: uppercase; margin-top: 2px;">
            Predictive Intelligence. Proactive Care.
        </div>
    </div>
    <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.15); margin: 0 0 16px 0;">
    """, unsafe_allow_html=True)
    
    # Navigation Radio Selection
    current_idx = NAV_OPTIONS.index(st.session_state["current_page"]) if st.session_state["current_page"] in NAV_OPTIONS else 0
    selected_page = st.radio(
        "Navigation",
        NAV_OPTIONS,
        index=current_idx,
        format_func=lambda x: f"{NAV_ICONS.get(x, '•')}  {x}",
        label_visibility="collapsed"
    )
    
    # Update state if changed by user
    if selected_page != st.session_state["current_page"]:
        st.session_state["current_page"] = selected_page
        st.rerun()
        
    # Sidebar Status & Footer
    st.markdown(f"""
    <div style="width: auto; margin-top: 16px; padding: 12px; background: rgba(0, 0, 0, 0.15); border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="display: flex; align-items: center; gap: 8px; font-size: 0.75rem; color: #DDF1ED;">
            <span style="color: #3D9275; font-size: 0.9rem;">●</span> <span>Model: <b>{champion_label}</b></span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; font-size: 0.75rem; color: #DDF1ED; margin-top: 4px;">
            <span style="color: #3D9275; font-size: 0.9rem;">●</span> <span>Cohort: <b>{cohort_size:,} patients</b></span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# Main Panel View Router
# ---------------------------------------------------------
page = st.session_state["current_page"]

if page == "Overview":
    from pages.overview import render_overview
    render_overview()
elif page == "Patient Risk Assessment":
    from pages.patient_assessment import render_patient_assessment
    render_patient_assessment()
elif page == "Dataset Explorer":
    from pages.dataset_explorer import render_dataset_explorer
    render_dataset_explorer()
elif page == "Analytics Dashboard":
    from pages.analytics import render_analytics
    render_analytics()
elif page == "Model Performance":
    from pages.model_performance import render_model_performance
    render_model_performance()
elif page == "Explainable AI":
    from pages.explainable_ai import render_explainable_ai
    render_explainable_ai()
elif page == "Research & About":
    from pages.about import render_about
    render_about()
