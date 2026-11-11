# ai_summarizer.py
import os
from dotenv import load_dotenv

load_dotenv()


# 예시: OpenAI나 Gemini API 등을 활용한 요약 함수
def summarize_text(title, content_text):
    """
    크롤러로부터 제목과 본문 텍스트를 받아 요약본을 반환하는 함수
    """
    if not content_text.strip():
        return "본문 내용이 비어있어 요약할 수 없습니다."

    # 텍스트 길이를 제한하여 토큰 낭비 방지 (글자 수 기준 3000자 내외 등)
    truncated_content = content_text[:3000]

    print(f"\n[AI 요약 중] '{title}' 분석 중...")

    # 임시 프롬프트 설정 (실제 사용 시 OpenAI, Anthropic, LangChain 등 API 연동 코드가 들어갑니다)
    # response = client.chat.completions.create(...)

    key = os.getenv("GEMINI_KEY")
    print(key)

    # 모형 동작 예시를 위한 임시 반환문
    summary = f"({title} 요약 결과) 본문 요약 테스트 데이터입니다. 텍스트 총 길이: {len(truncated_content)}자."

    return summary
