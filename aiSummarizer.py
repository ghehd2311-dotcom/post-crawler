# ai_summarizer.py
import os
from dotenv import load_dotenv

from google import genai
from google.genai import types
from google.genai.errors import APIError

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")


def genaiClient():
    try:
        # client = genai.Client(api_key=key)

        # 1. 클라이언트 생성 시 503, 429 등에 대한 자동 재시도 옵션 설정
        client = genai.Client(
            api_key=key,
            http_options=types.HttpOptions(
                retry_options=types.HttpRetryOptions(
                    attempts=5,  # 최초 1회 + 최대 4회 재시도
                    initial_delay=2.0,  # 첫 재시도 전 대기 시간 (초)
                    max_delay=30.0,  # 최대 대기 시간 (초)
                    exp_base=2.0,  # 대기 시간 증가 배수 (2초 -> 4초 -> 8초 -> 16초...)
                    http_status_codes=[429, 500, 502, 503, 504],
                )
            ),
        )

        print("Client 생성 성공!")
        return client
    except Exception as e:
        print("발생한 실제 에러:", type(e).__name__, e)


# 예시: OpenAI나 Gemini API 등을 활용한 요약 함수
def summarize_text(client, data):
    """
    크롤러로부터 제목과 본문 텍스트를 받아 요약본을 반환하는 함수
    """
    if client == None:
        print("client가 없음. 재연결 필요")
        return ""

    prompt = f"""
        다음 데이터를 3000자 이내로 한국어로 요약해.
        아래 규칙에 맞춰 Markdown 형식으로 답해:
        - 주요 제목은 # 또는 ## 사용
        - 코드나 명령어는 ``` 코드블록 사용
        - 핵심 키워드는 **볼드체** 처리

        [요약할 데이터]
        {data}
        """
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite", contents=[prompt, data]
        )
        return response.text
    except APIError as e:
        # 5번 모두 재시도했으나 여전히 503이거나, 400(잘못된 요청) 등 재시도 불가 에러인 경우
        if e.code == 503:
            print(f"구글 서버 과부하가 지속되어 요청에 실패했습니다: {e.message}")
        else:
            print(f"API 오류가 발생했습니다 (코드 {e.code}): {e.message}")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")
