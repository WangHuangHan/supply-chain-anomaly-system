# Supply Chain Anomaly Detection System

An end-to-end Machine Learning system for detecting supply chain anomalies using SAP MRP data.

This project demonstrates how ML models move beyond experimentation into production-oriented systems including APIs, dashboards, monitoring, and business decision logic.

---

## 🎯 Problem Statement

Supply chain risks often emerge through abnormal patterns across:

- Demand changes
- Inventory fluctuations
- Supplier lead time variations

Traditional rule-based monitoring fails to capture multidimensional anomalies.

This system combines statistical methods and machine learning to identify risks early and notify supply chain stakeholders.

---

## 🏗 Architecture Overview
SAP / MRP Data
↓
Ingestion Layer
↓
Feature Engineering
↓
Statistical Detection + ML Detection
↓
Evaluation Layer
↓
Business Risk Rules
↓
Monitoring
↓
Dashboard & API

---
## 📂 Project Structure
supply-chain-anomaly-system/
├── ingestion/ # SAP data loader
├── processing/ # feature engineering
├── models/ # anomaly detection models
├── evaluation/ # model comparison
├── business_logic/ # domain decisions
├── monitoring/ # drift & performance tracking
├── api/ # FastAPI serving
├── dashboard/ # Streamlit visualization
└── main.py # pipeline entrypoint

---
## ⚙️ Pipeline Execution

Run full workflow:

```bash
python main.py
```
This executes:
1. Data ingestion
2. Feature engineering
3. Statistical anomaly detection
4. ML anomaly detection
5. Evaluation comparison
6. Risk decision rules
7. Monitoring tracking

---
## 📊 Dashboard
Launch Streamlit dashboard:
```bash
streamlit run dashboard/app.py
```
Provides:
- Time-series anomaly visualization
- ML vs statistical comparison
- Operational monitoring view

---
## 🚀 API Service
Start FastAPI server:
```bash
uvicorn api.main:app --reload
``` 
Used by downstream systems for real-time anomaly scoring.

---
## 🧠 Key ML Concepts
- Time-series feature engineering
- Isolation Forest anomaly detection
- Statistical baseline comparison
- Business-rule integration
- Model monitoring & drift detection

---
## 📈 Roadmap
✅ Implemented
- Feature engineering pipeline
- Statistical anomaly detection
- Isolation Forest model
- Evaluation framework
- Streamlit dashboard
- FastAPI inference service
🚧 In Progress
- Airflow orchestration
- Automated alert service
- Email/Slack notifications
- Container deployment (Docker)

---
## 🧠 Key Engineering Ideas
This project focuses on bridging the gap between:
```bash
Data Science → ML Engineering → Production Systems
```
Key learnings:
- Models are only 20% of ML systems
- Monitoring is as important as accuracy
- Business interpretability matters
- Statistical baselines remain essential

---
## ▶️ Quick Start
Install dependencies:
```bash
pip install -r requirements.txt
```
Run dashboard:
```bash
streamlit run dashboard/app.py
```
Run API:
```bash
uvicorn api.main:app --reload
```

---
## 👤 Author
Wang Huang Han - Machine Learning Engineer focused on bridging Data Science and real-world supply chain applications.