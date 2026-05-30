import tomllib

sample_data = {
    "toml": {
        "記法": "TOMLは、Tom's Obvious, Minimal Languageの略で、構造化されたデータを表現するためのシンプルなマークアップ言語です。",
        "特徴": [
            "人間が読みやすい"
            , "階層構造をサポート"
            , "データ型のサポート（文字列、数値、配列、テーブルなど）"
        ]
    }
}

with open("sample.toml", "wb") as f:
    # Error : tomllib には dump 関数が存在しません。toml ライブラリを使用する必要があります。
    tomllib.dump(sample_data, f)
