from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from the Voice AI MCP webhook!"}
