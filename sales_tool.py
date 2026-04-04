import csv
import openpyxl

# ① CSVを読み込む
def read_csv(filename):
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results

# ② ステータスを判定する
def check_status(income):
    if income >= 300000:
        return "目標達成！"
    elif income >= 100000:
        return "順調です"
    elif income >= 30000:
        return "副業軌道中"
    else:
        return "まだこれから"

# ③ Excelに書き出す
def write_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "集計結果"

    ws["A1"] = "名前"
    ws["B1"] = "月収"
    ws["C1"] = "ステータス"

    for row in data:
        name = row["名前"]
        income = int(row["月収"])
        status = check_status(income)
        ws.append([name, income, status])

    wb.save(filename)
    print("完了：" + filename + " を作成しました")

# ④ 実行
sales = read_csv("practice_claude/sales.csv")
write_excel(sales, "practice_claude/集計結果.xlsx")