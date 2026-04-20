# 🚀 End-to-End MLOps Pipeline for Loan Prediction

## 📌 Overview
This project implements a production-ready MLOps pipeline for a Loan Prediction system. It covers the complete lifecycle of a machine learning model—from data versioning and training to deployment, monitoring, and automated retraining.
The system is designed to be scalable, reproducible, and cloud-ready using modern MLOps tools.

## 🧠 Key Features
- 📦 **Data Versioning** using DVC  
- 🔁 **CI/CD Pipeline** using GitHub Actions  
- 📊 **Experiment Tracking** using MLflow  
- 🚀 **Model Deployment** using FastAPI + Docker + Kubernetes (EKS)  
- 📡 **Monitoring** using Prometheus & Grafana  
- 🔄 **Continuous Training** triggered on new data  
- 📉 **Data Drift Detection** using Streamlit  


## ⚙️ Tech Stack
- **Backend**: FastAPI  
- **ML**: Scikit-learn  
- **Experiment Tracking**: MLflow  
- **Data Versioning**: DVC  
- **Containerization**: Docker  
- **Orchestration**: Kubernetes (EKS)  
- **Cloud**: AWS (S3, ECR, EKS)  
- **Monitoring**: Prometheus + Grafana  
- **Drift Detection**: Streamlit  


## 🚀 How to Run Locally

# Install dependencies
pip install -r requirements.txt

# Run FastAPI
uvicorn main:app --reload --port 8005