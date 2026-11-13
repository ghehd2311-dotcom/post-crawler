# ai_summarizer.py
import os
from dotenv import load_dotenv

from google import genai

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")


def genaiClient(key):
    try:
        client = genai.Client(api_key=key)
        print("Client 생성 성공!")
        return client
    except Exception as e:
        print("발생한 실제 에러:", type(e).__name__, e)


# 예시: OpenAI나 Gemini API 등을 활용한 요약 함수
def summarize_text(data):
    """
    크롤러로부터 제목과 본문 텍스트를 받아 요약본을 반환하는 함수
    """
    # prompt = "이 글을 3000자 이내로 요약해,다음 규칙에 맞춰 Markdown 형식으로 답해주세요:- 주요 제목은 # 또는 ## 사용- 코드나 명령어는 ``` 코드블록 사용- 핵심 키워드는 **볼드체** 처리 "
    # formatted_data = data.to_string(index=False)
    client = genaiClient(key)
    if client == None:
        pass
    # 2. 지시사항과 변환된 데이터를 하나의 문자열로 결합
    prompt = f"""
        다음 데이터를 3000자 이내로 요약해 주세요.
        아래 규칙에 맞춰 Markdown 형식으로 답해주세요:
        - 주요 제목은 # 또는 ## 사용
        - 코드나 명령어는 ``` 코드블록 사용
        - 핵심 키워드는 **볼드체** 처리

        [요약할 데이터]
        {data}
        """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite", contents=[prompt, data]
    )

    return response.text
