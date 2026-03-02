"""
Main Pipeline Entrypoint

Runs full Supply Chain Anomaly Detection workflow.

Usage:
    python main.py
"""

from datetime import datetime

# ingestion
from ingestion.sap_loader import load_sap_data

# processing
from processing.feature_engineering import build_features

# models
from models.statistical_detector import run_statistical_detection
from models.isolation_forest_detector import run_ml_detection

# evaluation
from evaluation.ml_vs_statistical_comparison import compare_results

# business logic
from business_logic.risk_rules import apply_risk_rules
from business_logic.action_engine import decide_actions

# monitoring
from monitoring.logger import get_logger
from monitoring.performance_tracker import track_anomaly_rate
from monitoring.drift_detector import detect_drift


logger = get_logger()


def step(title: str):
    logger.info(f"\n========== {title} ==========")


def run_pipeline():

    logger.info(f"Pipeline started at {datetime.now()}")

    # --------------------------------------------------
    step("STEP 1 — Load SAP / MRP Data")
    # --------------------------------------------------
    raw_df = load_sap_data()

    logger.info(f"Loaded records: {len(raw_df)}")

    # --------------------------------------------------
    step("STEP 2 — Feature Engineering")
    # --------------------------------------------------
    feature_df = build_features(raw_df)

    # --------------------------------------------------
    step("STEP 3 — Statistical Detection")
    # --------------------------------------------------
    stat_df = run_statistical_detection(feature_df)

    # --------------------------------------------------
    step("STEP 4 — ML Detection")
    # --------------------------------------------------
    ml_df = run_ml_detection(feature_df)

    # --------------------------------------------------
    step("STEP 5 — Evaluation (ML vs Statistical)")
    # --------------------------------------------------
    summary = compare_results(ml_df, stat_df)

    logger.info(f"Evaluation summary: {summary}")

    # --------------------------------------------------
    step("STEP 6 — Business Risk Rules")
    # --------------------------------------------------
    risk_df = apply_risk_rules(ml_df)

    actions = decide_actions(risk_df)

    logger.info(f"Actions generated: {len(actions)}")

    # --------------------------------------------------
    step("STEP 7 — Monitoring")
    # --------------------------------------------------
    track_anomaly_rate(ml_df)
    detect_drift(feature_df)

    logger.info("Pipeline completed successfully ✅")


if __name__ == "__main__":
    run_pipeline()