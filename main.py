import rssCrawler
import aiSummarizer
import exportToMd as exp

import streamlit as st

import pandas as pd

# 테스트용 RSS URL (예시)
target_url = "https://www.techblogposts.com/rss.xml"

context = rssCrawler.crawl_rss(target_url)
# data = pd.DataFrame(context)

"""
    ai 순차적으로 호출 (일단 3개만)해서
    리스트에 안에 딕셔너리에 summary 추가
"""
for post in context[0:3]:  # 일단 3개만
    summary = aiSummarizer.summarize_text(post["item"])
    post["summary"] = summary

"""
    context변수를 pandas 데이터프레임으로 감싸서
    1. 디비에 저장
    2. ai 요약 전에 디비에 저장 되있는지 검사해서 없을때만 디비에 저장
    3. 저장 후에 .md 파일로 내보내기
"""
df = pd.DataFrame(context)
print(df)
st.dataframe(df)
st.header("마크다운")
st.markdown(df["summary"])
