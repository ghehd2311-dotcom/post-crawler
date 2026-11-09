import feedparser
import requests
from bs4 import BeautifulSoup


def request_rss(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(f"RSS 요청 중 오류 발생: {e}")
        return ""


def crawl_rss(rss_url):
    feed = feedparser.parse(rss_url)

    print(f"=== 피드 제목: {feed.feed.title} ===")

    # 각 포스트(Item) 순회
    for entry in feed.entries:
        title = entry.title  # 글 제목
        link = entry.link  # 글 링크
        published = getattr(entry, "published", "날짜 없음")  # 발행일

        print(f"제목: {title}")
        print(f"링크: {link}")
        print(f"날짜: {published}")

        if link != "":
            html = request_rss(link)  # 링크 요청
            if type(html) == str:  # 타입가드 str인 경우에만
                soup = BeautifulSoup(html, "html.parser")
                print(soup)
        print("-" * 30)


# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"
crawl_rss(target_url)
