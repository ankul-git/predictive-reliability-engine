# Predictive Reliability Engine

A production-grade DevOps platform that predicts application failures before they occur using real-time metrics analysis and statistical forecasting.

## Key Features
- **Predictive Analytics**: Forecasts OOM events 30-60 minutes in advance
- **Auto-scaling Ready**: HPA integration based on predictive thresholds
- **Zero-Trust Security**: OIDC-based CI/CD with no static credentials
- **Production Infrastructure**: EKS + Terraform + GitOps workflow

## Tech Stack
AWS EKS | Terraform | Kubernetes | Docker | Prometheus | Grafana | Python | GitHub Actions

## Live Dashboard
<img width="1352" height="878" alt="Screenshot 2025-12-28 at 2 41 23 PM" src="https://github.com/user-attachments/assets/75ab228d-372f-4ee9-ac6e-ba5459e18831" />


## Architecture
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub Actions (CI/CD)                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ OIDC Auth    │───▶│ Terraform    │───▶│ Deploy App   │      │
│  │ (AWS STS)    │    │ Apply (EKS)  │    │ to K8s       │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AWS EKS Cluster                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    Application Layer                    │    │
│  │  ┌──────────────────┐      ┌──────────────────┐       │    │
│  │  │ Memory Leak App  │──────│ Custom Metrics   │       │    │
│  │  │ (Python)         │      │ /metrics endpoint│       │    │
│  │  └──────────────────┘      └──────────────────┘       │    │
│  └────────────────────────────────────────────────────────┘    │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Monitoring & Alerting Layer               │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │    │
│  │  │ Prometheus   │─▶│ Grafana      │  │ AlertManager│ │    │
│  │  │ (Scraping)   │  │ (Dashboard)  │  │ (Routing)   │ │    │
│  │  └──────────────┘  └──────────────┘  └─────────────┘ │    │
│  └────────────────────────────────────────────────────────┘    │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │            Predictive Reliability Engine               │    │
│  │  ┌──────────────────────────────────────────────┐     │    │
│  │  │ Python Service                               │     │    │
│  │  │ - Queries Prometheus PromQL                  │     │    │
│  │  │ - Calculates time-to-OOM based on trends     │     │    │
│  │  │ - Triggers preemptive scaling/alerts         │     │    │
│  │  └──────────────────────────────────────────────┘     │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘

