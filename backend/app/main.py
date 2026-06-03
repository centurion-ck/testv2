from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import k8s
from app.routes.health import router as health_router
from app.routes.predict import router as predict_router
from app.routes.scan import router as scan_router
from app.routes.remediation import router as remediation_router
from app.routes.cluster import router as cluster_router
from app.routes.metrics import router as metrics_router
from app.routes.recommendation import router as recommendation_router
from app.routes.copilot import router as copilot_router


app = FastAPI(
    title="KubeGuardian AI",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(predict_router)
app.include_router(k8s.router)
app.include_router(k8s.router)
app.include_router(scan_router)
app.include_router(remediation_router)
app.include_router(cluster_router)
app.include_router(metrics_router)
app.include_router(recommendation_router)
app.include_router(copilot_router)

@app.get("/")
def root():
    return {
        "message": "KubeGuardian AI Running"
    }