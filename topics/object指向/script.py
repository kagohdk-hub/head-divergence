"""
object指向の３要素
    カプセル化
    継承
    ポリモーフィズム
"""
# class は データ(以下では サイズ, 色, 鳴き声など) と メソッド(以下では 餌を取る, 卵を産む など) をまとめて持つ
class 鳥:
    def __init__(self, サイズ, 色, 鳴き声):
        self.__サイズ = サイズ
        self.__色 = 色
        self.__鳴き声 = 鳴き声
        self.__名前 = None

    # カプセル化でよくでてくる、setter, getter
    def get_色(self):
        return self.__色
    def set_名前(self, 名前: str):
        self.__名前 = 名前

    def 餌を取る(self):
        ...

    def 卵を産む(self):
        ...
    def 羽ばたく(self):
        ...
    # こういった鳥の共通の特徴を一箇所でかける

bird = 鳥(12, "red", "ガーガー")
# print(bird.__色)
# >>    AttributeError: '鳥' object has no attribute '__色'
# このように、内部に外部から直接さわれない構造を作ることなどが、カプセル化

# それぞれの鳥は受け継ぐだけ >> これが継承
class キツツキ(鳥):
    def 餌を取る(self):
        ...

class ペンギン(鳥):
    def 餌を取る(self):
        ...

    # 空を飛べない というようなマイナスの特徴の表現は難しい

wood_pecker = キツツキ()
penguin = ペンギン()

def func(bird: 鳥):
    # ここで抽象的に、なにかの"鳥"が餌を取るということを表現している
    # これがポリモーフィズム
    bird.餌を取る()

# 以下の二つは全く異なる動きをする
func(wood_pecker)
func(penguin)

# 親クラスのメソッドも使える
wood_pecker.羽ばたく()
