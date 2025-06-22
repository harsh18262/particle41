from fastapi import FastAPI, Request
import datetime

app = FastAPI()

@app.get("/")
async def get_current_time_and_ip(request: Request):
    
    timestamp = datetime.datetime.now().isoformat()
    ip = request.client.host
    return {"timestamp": timestamp, "ip": ip}
