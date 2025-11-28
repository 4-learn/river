from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import json

load_dotenv()

app = FastAPI()

# CORS 設定（允許前端呼叫）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Model
class WheelRequest(BaseModel):
    text: str
    position: list[int]


# Response Models
class LEDPosition(BaseModel):
    row: int
    col: int


class WheelResponse(BaseModel):
    led_position: LEDPosition
    color: str
    sentiment: str
    text: str


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/wheel", response_model=WheelResponse)
async def wheel_endpoint(request: WheelRequest):
    # Debug: 印出收到的 request 值
    print("=" * 50)
    print("收到 /wheel 請求:")
    print(f"  text: {request.text}")
    print(f"  position: {request.position}")
    print(f"  position[0]: {request.position[0]}")
    print(f"  position[1]: {request.position[1]}")
    print("=" * 50)

    # 回傳 fake data
    return {
        "led_position": {
            "row": 2,
            "col": 4
        },
        "color": "#FF0000",
        "sentiment": "positive",
        "text": request.text
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9005)
