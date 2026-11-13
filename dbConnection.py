# postgreSql
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine

load_dotenv()


def DbConn():
    pwd = os.getenv("DATABASE_PASSWORD")
    # 형식: postgresql+psycopg2://사용자명:비밀번호@호스트주소:포트/DB이름
    try:
        db_url = f"postgresql+psycopg2://postgres:{pwd}@localhost:5432/Crawler"
        engine = create_engine(db_url)
        print("db connection success")
        print("--" * 40)
        return engine
    except:
        print("db connection fail")
        print("--" * 40)


# print(engine)
# df.to_sql(
#     name="user_scores",  # 생성될 테이블 이름
#     con=engine,  # DB 연결 엔진
#     if_exists="replace",  # 'replace': 기존 테이블 덮어쓰기 / 'append': 기존 테이블에 이어서 추가
#     index=False,  # 데이터프레임의 행 번호(0, 1, 2...)는 컬럼으로 넣지 않음
# )
