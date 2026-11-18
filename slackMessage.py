import os
import requests
from dotenv import load_dotenv

load_dotenv()


def slack_send_message(text):
    token = os.getenv("BOT_TOKEN")
    ## 메시지 구조 정의
    message = {
        "channel": "post",
        "text": text,
    }

    ## HTTP 헤더 설정
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
    }

    ## 메시지 전송 API 호출
    response = requests.post(
        "https://slack.com/api/chat.postMessage", json=message, headers=headers
    )

    ## 결과 확인
    if response.json().get("ok"):
        print("메시지 전송 성공!")
    else:
        print("에러:", response.json())
