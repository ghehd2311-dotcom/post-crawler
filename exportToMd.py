from pathlib import Path
import re

vault = Path(r"C:\Users\백호동\Documents\Obsidian Vault\TechBlog")
vault.mkdir(exist_ok=True)


def safe_filename(title):
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    title = title.strip()
    return title[:150]


def exportToMd(new_posts):
    for post in new_posts:
        file_name = safe_filename(post["title"])

        md_path = vault / f"{file_name}.md"

        content = f"""
    # {post['title']}

    링크:
    {post['link']}

    ## AI 요약

    {post['summary']}
    """

        md_path.write_text(content, encoding="utf-8")
    return exportToMd
