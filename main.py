from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="PayAPI",
    description="A learning project for the x402 payment protocol",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "payapi",
    }

@app.get("/premium")
def premium_data():
    return JSONResponse(
        status_code=402,
        content={
                "error": "Payment Required",
                "message": "Payment is required to access this resource."
        },
    )