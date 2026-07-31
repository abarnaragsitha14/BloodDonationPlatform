from fastapi import FastAPI

app = FastAPI(
    title="Blood Donation Network & Emergency Matching Platform",
    version="1.0.0",
    description="REST API for Blood Donation Platform"
)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Blood Donation Network API",
        "data": None
    }