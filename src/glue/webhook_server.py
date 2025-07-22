import logging
import os
from fastapi import FastAPI, Request, HTTPException
from .openhands_client import forward_to_openhands

logging.basicConfig(level=logging.INFO)
app = FastAPI()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "change-me")

@app.post("/webhook")
async def webhook(request: Request):
    secret = request.headers.get("X-Webhook-Secret")
    if secret != WEBHOOK_SECRET:
        logging.warning("Unauthorized webhook call")
        raise HTTPException(status_code=401, detail="Unauthorized")
    payload = await request.json()
    logging.info("Webhook payload: %s", payload)
    try:
        forward_to_openhands(payload)
    except Exception as e:
        logging.error("Error forwarding to OpenHands: %s", e)
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
