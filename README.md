# Predictive Reliability Engine 🚀

A DevOps/SRE project that demonstrates:

- Kubernetes-based application deployment
- Prometheus metrics collection
- Grafana dashboards
- Predictive failure estimation based on memory leak patterns
- End-to-end observability pipeline

## Components

- **pre-app**: Python app exposing Prometheus metrics
- **pre-engine**: Predictive engine querying Prometheus
- **infra/kubernetes**: Kubernetes manifests
- **infra/terraform**: (Planned) AWS EKS infrastructure
- **ci**: (Planned) GitHub Actions CI/CD

## Current Status

✅ Local Kubernetes (kind)  
✅ Prometheus + Grafana  
✅ Metrics + prediction logic  
🚧 AWS EKS + Terraform (Next phase)

## Architecture

App → Prometheus → Grafana → Predictive Engine

