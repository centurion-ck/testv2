from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import k8s
from app.routes.health import router as health_router
from app.routes.predict import router as predict_router
from app.routes.scan import router as scan_router

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

@app.get("/")
def root():
    return {
        "message": "KubeGuardian AI Running"
    }