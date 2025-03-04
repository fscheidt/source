from fastapi import FastAPI, Request
app = FastAPI()

@app.api_route("/", methods=["GET", "POST", "DELETE","PUT","PATCH"])
async def root(request: Request):
    body = await request.body()
    return { 
        "message": "✅ request received",
        "method": request.method,
        "headers": request.headers,
        "body": body
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)
