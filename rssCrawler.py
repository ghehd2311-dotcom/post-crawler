import feedparser
import requests
import trafilatura


def requestRss(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(f"RSS 요청 중 오류 발생: {e}")
        return ""


def webTextProcessor(url):
    # downloaded = trafilatura.fetch_url(url)
    # 보일러플레이트(광고, 네비게이션 등) 제거 및 본문 추출
    extracted_text = trafilatura.extract(
        url,
        output_format="txt",  # 순수 텍스트 형식 지정 (기본값이기도 함)
        include_comments=False,
        include_tables=True,
        include_links=False,
        with_metadata=False,
    )
    return extracted_text


def normalize_text(text: str) -> str:
    """연속된 공백이나 불필요한 줄바꿈을 압축하여 토큰 낭비를 방지합니다."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def crawl_rss(rss_url):
    feed = feedparser.parse(rss_url)
    items = []
    for entry in feed.entries:
        title = entry.title  # 글 제목
        link = entry.link  # 글 링크
        # published = getattr(entry, "published", "날짜 없음")  # 발행일

        if link == "":
            continue  # 링크가 없는 경우 건너뜀

        html = requestRss(link)  # 링크 요청
        text = webTextProcessor(html)

        if text is None:
            print(f"본문 추출 실패: {link}")
            continue

        clean_text = normalize_text(text)
        # df = pd.DataFrame([clean_text])
        # print(clean_text)  # 추출된 본문 일부 출력
        # print(df)  # 추출된 본문 일부 출력
        res = {"title": title, "item": clean_text}
        items.append(res)

    return items  # 첫 번째 글의 본문만 반환 (테스트용)
