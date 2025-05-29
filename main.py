from fastapi import FastAPI, Request, HTTPException
import logging

# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# https://cf3a-211-168-191-21.ngrok-free.app/robot/status
# https://cf3a-211-168-191-21.ngrok-free.app/robot/moving


# https://ecb5-211-168-191-21.ngrok-free.app/el/arrival
# https://cf3a-211-168-191-21.ngrok-free.app/el/moving
# https://cf3a-211-168-191-21.ngrok-free.app/el/error


@app.post("/el/arrival")
async def elevator_arrival_event(request: Request):
    print("엘리베이터 도착 이벤트 수신")
    logger.info("엘리베이터 도착 이벤트 수신")
    payload = await request.json()
    print(payload)
    logger.info(f"Received payload: {payload}")


@app.post("/el/moving")
async def elevator_moving_event(request:Request):
    payload = await request.json()
    logger.info(f"Received payload: {payload}")

@app.post("/el/error")
async def elevator_error_event(request:Request):
    payload = await request.json()
    logger.info(f"Received payload: {payload}")

@app.post("/robot/status")
async def robot_status_event(request:Request):
    payload = await request.json()
    logger.info(f"Received payload: {payload}")


@app.post("/robot/moving")
async def robot_moving_event(request:Request):
    payload = await request.json()
    logger.info(f"Received payload: {payload}")



# 테스트를 위한 간단한 GET 엔드포인트
@app.get("/")
async def root():
    return {"message": "Hello from Webhook Listener!"}

"""
pip install fastapi uvicorn
uvicorn main:app --reload

ngrok 활용: 로컬에서 실행 중인 서버를 외부에서 접근할 수 있도록 해주는 도구입니다. 
ngrok http 8000 명령어를 실행하면 https://<random_id>.ngrok-free.app 형태의 URL을 얻을 수 있고, 이 URL을 API 제공 서비스의 웹훅 설정에 등록하여 실제 puevent를 받아볼 수 있습니다.


"""