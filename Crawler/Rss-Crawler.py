import feedparser


def crawl_rss(rss_url):
    feed = feedparser.parse(rss_url)

    print(f"=== 피드 제목: {feed.feed.title} ===")

    # 각 포스트(Item) 순회
    for entry in feed.entries:
        title = entry.title  # 글 제목
        link = entry.link  # 글 링크
        published = getattr(entry, "published", "날짜 없음")  # 발행일
        summary = getattr(entry, "summary", "내용 없음")  # 요약 내용

        print(f"제목: {title}")
        print(f"링크: {link}")
        print(f"날짜: {published}")
        print("-" * 30)


# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"
crawl_rss(target_url)
