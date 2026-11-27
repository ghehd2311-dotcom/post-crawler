import re
import os
from pathlib import Path
from datetime import datetime
from utils.week_time import get_week_folder, get_year_folder, get_Date_folder

year = str(get_year_folder())
week = str(get_week_folder(datetime.now().strftime("%Y-%m-%d")))
base_path = r"C:\Users\백호동\Documents\Obsidian Vault\TechBlog"

path = os.path.join(base_path, year, week)

vault = Path(path)
vault.mkdir(parents=True, exist_ok=True)


def safe_filename(title):
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    title = title.strip()
    return title[:150]


def exportToMd(new_posts):
    for post in new_posts:
        file_name = safe_filename(post["title"])
        date = get_Date_folder()
        md_path = vault / f"[{date}]{file_name}.md"

        content = f"""
    # {post['title']}

    링크:
    {post['link']}

    ## AI 요약

    {post['summary']}
    """

        md_path.write_text(content, encoding="utf-8")
    return exportToMd
