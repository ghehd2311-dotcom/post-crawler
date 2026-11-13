import rssCrawler
import aiSummarizer

import pandas as pd

import dbConnection

# 데이터 베이스 연결
engine = dbConnection.DbConn()
# genai client 연결
client = aiSummarizer.genaiClient()

# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"

context = rssCrawler.crawl_rss(target_url)

"""
    ai 순차적으로 호출해서
    context 리스트에 안에 딕셔너리에 summary 추가
"""
for post in context[0:2]:
    summary = aiSummarizer.summarize_text(client, post["item"])
    post["summary"] = summary
"""
    context변수를 pandas 데이터프레임으로 감싸서
    
    2. ai 요약 전에 디비에 저장 되있는지 검사해서 없을때만 디비에 저장
    3. 저장 후에 .md 파일로 내보내기
"""
df = pd.DataFrame(context)

# 1. 디비에 저장
df.to_sql(
    name="post",  # 생성될 테이블 이름
    con=engine,  # DB 연결 엔진
    if_exists="replace",  # 'replace': 기존 테이블 덮어쓰기 / 'append': 기존 테이블에 이어서 추가
    index=False,  # 데이터프레임의 행 번호(0, 1, 2...)는 컬럼으로 넣지 않음
)

df.to_markdown(r"C:\Users\백호동\Documents\Obsidian Vault", index=False)
