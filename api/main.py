import os
import shutil
from fastapi import FastAPI, File, HTTPException, UploadFile
from ml.engine import StrainAnalysisEngine
 
app = FastAPI(title="CardioVision API", version="0.1.0")
ml_engine = StrainAnalysisEngine()

TEMP_DIR = "temp_uploads"
os.makedirs(TEMP_DIR, exist_ok = True)

@app.get("/health")
def health_check():
    # adding endpoint for Google Cloud Run
    return {"status": "ok", "service": "CardioVision API"} 

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    # to count GLS and download cardiogram

    if not file.filename.endswith(('.mp4', '.dcm', '.avi')):
        raise HTTPException(status_code=400, detail="mp4, dcm, avi formats only")

    file_path = os.path.join(TEMP_DIR, file.filename)

    try: 
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while saving: {str(e)}")
    finally:
        file.file.close()
            
    try:
        analysis_result = ml_engine.process_video(file_path)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    return {"filename": file.filename, "result": analysis_result}