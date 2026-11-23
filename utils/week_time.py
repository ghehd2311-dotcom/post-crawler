from datetime import datetime


def get_year_folder():
    date = datetime.now()
    year = date.strftime("%Y")
    return year


def get_week_folder(date_str):
    date = datetime.strptime(date_str[:10], "%Y-%m-%d")

    month = date.month

    week = ((date.day - 1) // 7) + 1

    return f"{month}월 {week}주차"
