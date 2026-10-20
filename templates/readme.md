# Heart API Helm Chart

This Helm chart deploys the Heart Disease FastAPI service on Kubernetes.

## Prerequisites

- Kubernetes cluster (Minikube, AKS, GKE, etc.)
- Helm v3+
- Docker image pushed to a registry

## Structure

- `Chart.yaml` — chart metadata
- `values.yaml` — default configuration
- `templates/deployment.yaml` — app Deployment
- `templates/service.yaml` — Service (NodePort)
- `templates/ingress.yaml` — optional Ingress
- `templates/hpa.yaml` — Horizontal Pod Autoscaler
- Prometheus annotations on the Deployment for scraping metrics

## Installation

```bash
helm install heart-api helm/heart-api-chart
