from fastapi import FastAPI

app = FastAPI(
    title="EphemeralLab API",
    description="Self-service development environment provisioning platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to EphemeralLab",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }