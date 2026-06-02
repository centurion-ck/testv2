$project = "kubeguardian-ai"

New-Item -ItemType Directory -Path $project -Force

# Frontend
New-Item -ItemType Directory -Path "$project/frontend" -Force

New-Item -ItemType File -Path "$project/frontend/index.html" -Force
New-Item -ItemType File -Path "$project/frontend/style.css" -Force
New-Item -ItemType File -Path "$project/frontend/app.js" -Force

# Backend
New-Item -ItemType Directory -Path "$project/backend/app/routes" -Force
New-Item -ItemType Directory -Path "$project/backend/app/services" -Force

New-Item -ItemType File -Path "$project/backend/app/main.py" -Force
New-Item -ItemType File -Path "$project/backend/app/database.py" -Force
New-Item -ItemType File -Path "$project/backend/app/models.py" -Force
New-Item -ItemType File -Path "$project/backend/app/schemas.py" -Force

New-Item -ItemType File -Path "$project/backend/app/routes/health.py" -Force
New-Item -ItemType File -Path "$project/backend/app/routes/predict.py" -Force
New-Item -ItemType File -Path "$project/backend/app/routes/threats.py" -Force
New-Item -ItemType File -Path "$project/backend/app/routes/reports.py" -Force

New-Item -ItemType File -Path "$project/backend/app/services/predictor.py" -Force

New-Item -ItemType File -Path "$project/backend/requirements.txt" -Force
New-Item -ItemType File -Path "$project/backend/Dockerfile" -Force

# ML Service
New-Item -ItemType Directory -Path "$project/ml-service/models" -Force
New-Item -ItemType Directory -Path "$project/ml-service/dataset" -Force

New-Item -ItemType File -Path "$project/ml-service/train.py" -Force
New-Item -ItemType File -Path "$project/ml-service/predict.py" -Force
New-Item -ItemType File -Path "$project/ml-service/requirements.txt" -Force
New-Item -ItemType File -Path "$project/ml-service/Dockerfile" -Force

# Jenkins
New-Item -ItemType Directory -Path "$project/jenkins" -Force
New-Item -ItemType File -Path "$project/jenkins/Jenkinsfile" -Force

# Kubernetes
New-Item -ItemType Directory -Path "$project/k8s/frontend" -Force
New-Item -ItemType Directory -Path "$project/k8s/backend" -Force
New-Item -ItemType Directory -Path "$project/k8s/ml-service" -Force
New-Item -ItemType Directory -Path "$project/k8s/postgres" -Force

New-Item -ItemType File -Path "$project/k8s/namespace.yaml" -Force
New-Item -ItemType File -Path "$project/k8s/configmap.yaml" -Force
New-Item -ItemType File -Path "$project/k8s/secret.yaml" -Force
New-Item -ItemType File -Path "$project/k8s/ingress.yaml" -Force
New-Item -ItemType File -Path "$project/k8s/hpa.yaml" -Force
New-Item -ItemType File -Path "$project/k8s/networkpolicy.yaml" -Force

# Monitoring
New-Item -ItemType Directory -Path "$project/monitoring" -Force

New-Item -ItemType File -Path "$project/monitoring/prometheus-values.yaml" -Force
New-Item -ItemType File -Path "$project/monitoring/grafana-dashboard.json" -Force

# Security
New-Item -ItemType Directory -Path "$project/security" -Force

New-Item -ItemType File -Path "$project/security/falco-rules.yaml" -Force
New-Item -ItemType File -Path "$project/security/trivy-policy.yaml" -Force

# Scripts
New-Item -ItemType Directory -Path "$project/scripts" -Force

New-Item -ItemType File -Path "$project/scripts/deploy.ps1" -Force
New-Item -ItemType File -Path "$project/scripts/rollback.ps1" -Force
New-Item -ItemType File -Path "$project/scripts/cleanup.ps1" -Force

# Root Files
New-Item -ItemType File -Path "$project/docker-compose.yml" -Force
New-Item -ItemType File -Path "$project/README.md" -Force
New-Item -ItemType File -Path "$project/.gitignore" -Force

Write-Host ""
Write-Host "======================================="
Write-Host " KubeGuardian AI Repository Created"
Write-Host "======================================="
Write-Host ""