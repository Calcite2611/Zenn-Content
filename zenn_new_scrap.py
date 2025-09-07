#!/usr/bin/env python3
# zenn_scrap_new.py

import os
from datetime import datetime
import argparse

# Scrap フォルダのパス（Zenn-content/Scrap の下に作成）
SCRAP_DIR = os.path.join(os.getcwd(), "Scrap")

# Markdown テンプレート
TEMPLATE = """# Day {day_number} - {date}

### タイトル
{{今日の学習内容やテーマを簡潔に書く}}

### TryHackMe Room / Lab
- Room名 / Lab名: {{例: Linux Fundamentals}}
- URL: {{任意で貼る}}

### 学習内容
- {{学習したことの要約を箇条書きで}}
- {{コマンドや手順のポイント}}
- {{気づきや注意点}}

### 結果 / 成果
- {{どこまでできたか、解決した問題など}}
- {{スキル向上や理解の進捗など}}

### 振り返り / 感想
- {{今日の学習の感想や次回への課題}}
"""

def get_next_day_number(scrap_dir):
    """Scrapフォルダ内の既存ファイルから次のDay番号を決定"""
    if not os.path.exists(scrap_dir):
        return 1
    max_day = 0
    for fname in os.listdir(scrap_dir):
        if fname.startswith("day-") and fname.endswith(".md"):
            try:
                with open(os.path.join(scrap_dir, fname), "r") as f:
                    first_line = f.readline()
                    if first_line.startswith("# Day "):
                        day_num = int(first_line.split()[2])
                        if day_num > max_day:
                            max_day = day_num
            except:
                continue
    return max_day + 1

def main():
    parser = argparse.ArgumentParser(description="Zenn Scrap 用 Markdown ファイル生成")
    parser.add_argument("--date", type=str, help="任意の日付 YYYY-MM-DD (省略時は今日)")
    args = parser.parse_args()

    # 日付設定
    if args.date:
        try:
            date_obj = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print("日付形式が不正です。YYYY-MM-DD の形式で指定してください。")
            return
    else:
        date_obj = datetime.today()

    date_str = date_obj.strftime("%Y-%m-%d")

    # Scrap ディレクトリ作成
    os.makedirs(SCRAP_DIR, exist_ok=True)

    # Day番号決定
    day_number = get_next_day_number(SCRAP_DIR)

    # Markdown 内容生成
    content = TEMPLATE.format(day_number=day_number, date=date_str)

    # ファイル名
    filename = f"day-{date_str}.md"
    filepath = os.path.join(SCRAP_DIR, filename)

    # 書き込み
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Scrap Markdown を生成しました: {filepath}")

if __name__ == "__main__":
    main()