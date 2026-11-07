from __future__ import annotations
if True:
    """
    使用上の注意：
    安易に p,qなどの数値を大きくすると、累乗により非常に大きい数字となり
    扱いきれなくなる可能性があります。
    """
    from random import randint
    from dataclasses import dataclass

    def ランダムに素数選択() -> int:
        raise Exception("処理未作成")

    def 素数ペアを選択() -> tuple[int, int]:
        for _ in range(5):
            p = ランダムに素数選択()
            q = ランダムに素数選択()
            if p != q:
                return p, q
        else:
            raise Exception("Retry out")

    def 互いに素であるか(a: int, b: int) -> bool:
        raise Exception("処理未作成")

    @dataclass
    class 秘密鍵:
        p: int
        q: int
        n: int = None   # p * q 公開鍵と共通
        m: int = None   # (p-1) * (q-1)
        d: int = None   # 秘密の数字

        ### 生成処理 ###
        def mを計算(self) -> None:
            self.m = (self.p - 1) * (self.q - 1)

        def 公開鍵のベース作成(self) -> None:
            self.n = self.p * self.q

        def 秘密の数字を探す(self, 公開鍵_: 公開鍵):
            """
            (公開鍵_.e * d) % self.m = 1
            self.m + 1 = 公開鍵_.e * d
            d = (self.m + 1) / 公開鍵_.e
            """
            for x in range(1, 100):
                f = ( (120*x) + 1 ) / 17
                i = int(f)
                if f == i:
                    self.d = i
                    return
            else:
                raise Exception("Retry out")
        def 秘密の数字をチェック(self, 公開鍵_: 公開鍵):
            if (公開鍵_.e * self.d) % self.m != 1:
                raise Exception("秘密鍵の秘密の数字が適切ではありません。")

        ### 暗号化復号化 ###
        def 暗号化および復号化(self, 変換前数: int) -> int:
            print(f"{変換前数 ** self.d} % {self.n}")
            return (変換前数 ** self.d) % self.n

    @dataclass
    class 公開鍵:
        n: int          # p * q 秘密鍵と共通
        e: int = None   # (p-1)*(q-1)と互いに素

        ### 生成処理 ###
        def 公開数を選択(self, m: int) -> None:
            for _ in range(10):
                e = randint(1, 1000)
                if 互いに素であるか(m, e):
                    self.e = e
            else:
                raise Exception("Retry out")
        def 公開数をチェック(self, m: int) -> None:
            if not 互いに素であるか(m, self.e):
                raise Exception("公開数が秘密鍵の(p-1)*(q-1)と互いに素でありません。")

        ### 暗号化復号化 ###
        def 暗号化および復号化(self, 変換前数: int) -> int:
            print(f"{変換前数 ** self.e} % {self.n}")
            return (変換前数 ** self.e) % self.n

    def 秘密鍵と公開鍵を生成() -> tuple[秘密鍵, 公開鍵]:
        # p, q = 素数ペアを選択()
        p, q = 13, 11
        秘密鍵_ = 秘密鍵(p=p, q=q)
        秘密鍵_.mを計算()
        秘密鍵_.公開鍵のベース作成()

        print(f"{秘密鍵_.__dict__=}")

        公開鍵_ = 公開鍵(秘密鍵_.n)
        公開鍵_.e = 17   # 公開数を手動設定
        # 公開鍵_.公開数をチェック(秘密鍵_.m)

        秘密鍵_.秘密の数字を探す(公開鍵_)

        print(f"{秘密鍵_.__dict__=}\n{公開鍵_.__dict__=}")
        return 秘密鍵_, 公開鍵_

    def 秘密鍵で暗号化し公開鍵で復号化する(元数):
        print("\nstart : 秘密鍵で暗号化し公開鍵で復号化する")
        秘密鍵_, 公開鍵_ = 秘密鍵と公開鍵を生成()

        暗号化数 = 秘密鍵_.暗号化および復号化(元数)

        復号化数 = 公開鍵_.暗号化および復号化(暗号化数)

        print(f"{元数=} : {暗号化数=} : {復号化数=}")
        assert 元数 == 復号化数 , f"{元数=} != {復号化数=}"

    def 公開鍵で暗号化し秘密鍵で復号化する(元数):
        print("\nstart : 公開鍵で暗号化し秘密鍵で復号化する")
        秘密鍵_, 公開鍵_ = 秘密鍵と公開鍵を生成()

        暗号化数 = 公開鍵_.暗号化および復号化(元数)

        復号化数 = 秘密鍵_.暗号化および復号化(暗号化数)

        print(f"{元数=} : {暗号化数=} : {復号化数=}")
        assert 元数 == 復号化数 , f"{元数=} != {復号化数=}"

try:
    秘密鍵で暗号化し公開鍵で復号化する(123)
except Exception as e:
    print(f"エラーが発生しました: {type(e).__name__} - {e}")
try:
    公開鍵で暗号化し秘密鍵で復号化する(123)
except Exception as e:
    print(f"エラーが発生しました: {type(e).__name__} - {e}")
