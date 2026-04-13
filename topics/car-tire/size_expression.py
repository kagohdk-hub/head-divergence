from enum import Enum

例 = "205/65R 15 94V"

class 速度記号_(Enum):
    Q = "160km"
    S = "180km"
    H = "210km"
    V = "240km"

タイヤの幅_mm = 205
偏平率_percent = 65 # 断面高さ / 断面幅 * 100
ラジアル構造 = "R"
リム径_inch = 15
ロードインデックス = 94
速度記号 = 速度記号_.Q.name

表記 = f"{タイヤの幅_mm}/{偏平率_percent}{ラジアル構造} {リム径_inch} {ロードインデックス}{速度記号}"
