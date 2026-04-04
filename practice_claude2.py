# ① ファイルに書き込む
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("副業目標：月30万円\n")
    f.write("現在のスキル：Python学習中\n")
    f.write("開始月：2026年4月\n")

print("ファイルを作成しました")

# ② ファイルを読み込む
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 1行ずつ読み込んでループ処理
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("→ " + line.strip())