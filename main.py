import rssCrawler
import aiSummarizer
import exportToMd as ex
import pandas as pd

import dbConnection

# 데이터 베이스 연결
engine = dbConnection.DbConn()
# genai client 연결
client = aiSummarizer.genaiClient()

# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"

context = rssCrawler.crawl_rss(target_url)

# 디비에 link로 글 존재 유무 확인
existing_df = pd.read_sql("SELECT link FROM post", engine)

existing_links = set(existing_df["link"])

new_posts = []
for post in context:
    if post["link"] not in existing_links:
        new_posts.append(post)

for post in new_posts:
    summary = aiSummarizer.summarize_text(client, post["item"])
    post["summary"] = summary

df = pd.DataFrame(new_posts)


# 1. 디비에 저장
df.to_sql(
    name="post",  # 생성될 테이블 이름
    con=engine,  # DB 연결 엔진
    if_exists="append",  # 'replace': 기존 테이블 덮어쓰기 / 'append': 기존 테이블에 이어서 추가
    index=False,  # 데이터프레임의 행 번호(0, 1, 2...)는 컬럼으로 넣지 않음
)
ex.exportToMd(new_posts)
