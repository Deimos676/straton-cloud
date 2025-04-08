from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from ai_core import process_prompt

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stratón Cloud Command Node Online"}

@app.post("/query")
async def query(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")

        if not prompt:
            return JSONResponse(status_code=400, content={"error": "Missing prompt"})

        response = process_prompt(prompt)
        return {"response": response}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
