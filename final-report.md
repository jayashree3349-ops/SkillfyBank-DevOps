# SkillfyBank DevOps Project — Final Report

## 1. Project Overview
Deployed the SkillfyBank application using Docker Swarm and Kubernetes on an AWS EC2 Ubuntu instance.

## 2. Kubernetes Deployment
- Deployed account, transaction, and notification services.
- Verified three registered Kubernetes nodes in Ready state.
- Verified application pods were Running and ready.
- Configured persistent storage and Horizontal Pod Autoscaling.

## 3. Docker Swarm
- Configured Swarm services and overlay networking.
- Captured service and rolling-update evidence.

## 4. Istio Service Mesh
- Configured transaction traffic routing with 90% v1 and 10% v2 weights.
- Configured notification beta-header routing to v2.
- Configured retry behavior for transaction requests.
- Verified ingress requests returned HTTP 200.
- Note: Configured traffic weights were inspected, but live version-level traffic distribution was not conclusively measured.

## 5. Centralized Logging
- Deployed Elasticsearch, Fluentd, and Kibana.
- Verified logging components were Running.
- Captured Elasticsearch index and Fluentd evidence.

## 6. Evidence
The accompanying `final-evidence.tar.gz` contains Kubernetes, Istio, logging, storage, autoscaling, and service status evidence.

## 7. Conclusion
The application infrastructure and supporting observability components were deployed and validated. The attached evidence archive supports the reported configuration and health checks.
