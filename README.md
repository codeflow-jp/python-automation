# CSV Auto Aggregator — CSV自動集計ツール

> CSVファイルのデータを条件に基づいて自動判定し、構造化されたExcelレポートを出力するPythonツール。

## できること

| 機能 | 詳細 |
|------|------|
| CSV読み込み | 任意のCSVファイルを自動解析 |
| 条件判定 | config.jsonの閾値に基づきステータスを自動付与 |
| Excel出力 | 判定結果を構造化されたExcelファイルに書き出し |
| 汎用設計 | コード変更不要で異なるCSVデータに対応可能 |

## 動作イメージ

```
CSV読み込み → 条件判定（config.jsonベース） → Excel出力
```

### 入力（sales.csv）

| 名前 | 月収 |
|------|------|
| 山田 | 520000 |
| 鈴木 | 310000 |
| 佐々木 | 210000 |
| 渡辺 | 80000 |

### 出力（集計結果.xlsx）

| 名前 | 月収 | ステータス |
|------|------|------|
| 山田 | 520000 | 目標達成！ |
| 鈴木 | 310000 | 順調です |
| 佐々木 | 210000 | 軌道中 |
| 渡辺 | 80000 | まだこれから |

## 使用技術

| カテゴリ | 技術・ライブラリ |
|------|------|
| 言語 | Python 3.14 |
| Excel出力 | openpyxl |
| 設定管理 | json（標準ライブラリ） |
| CLI対応 | sys / os（標準ライブラリ） |

## セットアップ手順

### 1. リポジトリをクローン

```
git clone https://github.com/codeflow-jp/python-automation.git
cd python-automation
```

### 2. 必要ライブラリをインストール

```
pip install openpyxl
```

### 3. 実行

```
python sales_tool.py
```

### 4. ファイルを指定して実行

```
python sales_tool.py 任意のデータ.csv 任意の出力ファイル.xlsx
```

## カスタマイズ

config.json で判定条件・列名・シート名を自由に変更できます。

```json
{
    "name_column": "名前",
    "value_column": "月収",
    "thresholds": [
        {"label": "目標達成！", "min": 500000},
        {"label": "順調です",   "min": 300000},
        {"label": "軌道中",     "min": 200000},
        {"label": "まだこれから", "min": 0}
    ],
    "sheet_name": "集計結果"
}
```

## 開発で解決した技術課題

| 課題 | 原因 | 解決策 |
|------|------|------|
| 異なるCSVに対応できない | 列名がハードコードされていた | config.jsonで列名を外部管理する設計に変更 |
| 判定条件の変更にコード修正が必要 | 閾値がコード内に直書きされていた | config.jsonのthresholds配列で柔軟に管理 |
| ファイルパスの指定が不便 | 入出力ファイルが固定だった | sys.argvによるコマンドライン引数に対応 |

## ファイル構成

```
python-automation/
├── sales_tool.py      # メインスクリプト
├── config.json        # 判定条件・列名の設定ファイル
├── sales.csv          # 入力データ（サンプル）
├── output_sample.xlsx # 出力サンプル
└── README.md
```

## 対応可能な業務

- 売上・成績データの自動集計
- 社員・顧客データの条件別振り分け
- 任意のCSVデータの一括処理・Excel出力

## ライセンス

MIT License