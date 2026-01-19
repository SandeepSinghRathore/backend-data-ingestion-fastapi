from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Data Ingestion"])

@router.get("/databases")
def list_databases():
    return {
        "message": "Database listing endpoint (placeholder)"
    }

@router.post("/ingest")
def ingest_data():
    return {
        "message": "Data ingestion triggered (placeholder)"
    }
