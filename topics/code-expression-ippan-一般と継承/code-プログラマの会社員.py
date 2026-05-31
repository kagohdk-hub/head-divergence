from __future__ import annotations
if True:
    """
    一般的な＊＊、というのは、継承元の親クラスのことだと思った。

    本コードの目的はあくまで、現実を単純化して表すことなので、こんな感じでいい
    """
    # 属性クラス
    class 社会人:
        def __init__(self, name: str):
            self.name = name
        def 挨拶(self):
            print(f"こんにちは、{self.name}です。")

    class 一般的な会社員(社会人):
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
            社会人.__init__(self, name)
        def 勤務データ提出(self):
            print(f"勤務データを提出しました。: {self.name}")

    class 一般的なプログラマ:
        def __init__(self, language: str, name: str):
            self.language = language
            self.name = name
        def コードを書く(self):
            print(f"コードを書きました。: {self.name} - {self.language}")

    class 優秀なプログラマ(一般的なプログラマ):
        def __init__(self, language: str, name: str):
            一般的なプログラマ.__init__(self, language, name)
        def コードレビューをする(self):
            print(f"コードレビューをしました。: {self.name} - {self.language}")

    # 個別クラス
    class 山田(一般的な会社員, 一般的なプログラマ):
        def __init__(self, name: str = "やまだ", age: int = 30, language: str = "python"):
            一般的な会社員.__init__(self, name, age)
            一般的なプログラマ.__init__(self, language, name)
        
        def 自社独自の機能の開発(self):
            print(f"自社独自の機能を開発しました。: {self.name}")
    class 佐々木(一般的な会社員, 優秀なプログラマ):
        def __init__(self, name: str = "ささき", age: int = 35, language: str = "java"):
            一般的な会社員.__init__(self, name, age)
            優秀なプログラマ.__init__(self, language, name)
        
        def 自社独自の機能の開発(self):
            print(f"自社独自の機能を開発しました。: {self.name}")

    # 実行イメージ
    yamada = 山田()
    sasaki = 佐々木()
    yamada.コードを書く()
    sasaki.コードを書く()
    sasaki.コードレビューをする()

    # 判定
    try:
        yamada.挨拶()
    except AttributeError:
        print(f"挨拶ができないなんて、{yamada.name}は社会人失格だ")
