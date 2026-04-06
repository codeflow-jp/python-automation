import csv
import json
import openpyxl
import sys
import os

# ① 設定ファイルを読み込む
def load_config(config_path="config.json"):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# ② CSVを読み込む
def read_csv(filepath):
    results = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results

# ③ ステータスを判定する
def check_status(value, thresholds):
    for t in thresholds:
        if value >= t["min"]:
            return t["label"]
    return "判定不可"

# ④ Excelに書き出す
def write_excel(data, config, output_path):
    name_col = config["name_column"]
    value_col = config["value_column"]
    thresholds = config["thresholds"]
    sheet_name = config["sheet_name"]

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name

    ws.append([name_col, value_col, "ステータス"])

    for row in data:
        name = row[name_col]
        value = int(row[value_col])
        status = check_status(value, thresholds)
        ws.append([name, value, status])

    wb.save(output_path)
    print("完了：" + output_path + " を作成しました")

# ⑤ 実行
if __name__ == "__main__":
    config = load_config("config.json")

    csv_file = sys.argv[1] if len(sys.argv) > 1 else "sales.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "集計結果.xlsx"

    if not os.path.exists(csv_file):
        print("エラー：" + csv_file + " が見つかりません")
        sys.exit(1)

    data = read_csv(csv_file)
    write_excel(data, config, output_file)