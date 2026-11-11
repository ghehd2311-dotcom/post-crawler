import rssCrawler
import aiSummarizer

import pandas as pd

# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"

context = rssCrawler.crawl_rss(target_url)
data = pd.DataFrame(context)
print(data)
print(data["title"])

# summary = aiSummarizer.summarize_text("제목", context)
# print(summary)
"""
    ai 호출 하고 .md파일로 저장 하는 로직 만들기
"""
