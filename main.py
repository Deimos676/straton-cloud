from fastapi import FastAPI, Request
from ai_core import process_prompt

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Stratón Cloud Command Node Online"}

@app.post("/query")
async def query_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return {"error": "Prompt is required."}
    
    response = await process_prompt(prompt)
    return {"response": response}
