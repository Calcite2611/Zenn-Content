#!/usr/bin/env python3
import subprocess
from datetime import datetime

def main():
    # 日付の選択
    use_today = input("今日の日付を使いますか？ (y/n): ").strip().lower()
    if use_today == 'y':
        date_str = datetime.today().strftime("%Y-%m-%d")
    else:
        date_str = input("日付を YYYY-MM-DD 形式で入力してください: ").strip()

    # 記事識別子の入力
    short_id = input("記事の識別子（例: thm）を入力してください: ").strip()

    # slug の生成
    slug = f"{date_str}-{short_id}"

    # Zenn CLI を呼び出して記事作成
    subprocess.run(["npx", "zenn", "new:article", "--slug", slug])

if __name__ == "__main__":
    main()