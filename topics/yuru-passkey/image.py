from __future__ import annotations
if True:
    from random import randint
    from dataclasses import dataclass

    @dataclass
    class UserInfo:
        userid: str
        public_key: str = None
        is_active: bool = False

    class Server:
        def __init__(self, domain: str):
            self.domain: str = domain
            self.user_bank: list[UserInfo]

        def 認証リクエスト受信(self, user_: User):
            self.チャレンジ(user_)

        def チャレンジ(self, user_: User):
            チャレンジ文字列 = str(randint(100, 999))
            チャレンジ暗号化結果 = user_.チャレンジ暗号化(チャレンジ文字列)
            チャレンジ復号結果 = self.チャレンジ復号(チャレンジ暗号化結果)

            if チャレンジ文字列 == チャレンジ復号結果:
                for user_info in self.user_bank:
                    user_info: UserInfo
                    if user_info.userid == User.userid:
                        user_info.is_active = True

        def チャレンジ復号(self):
            ...
        ...

    class User:
        def 認証リクエスト(self, server_: Server):
            server_.認証リクエスト受信(self)

        def チャレンジ暗号化(self, チャレンジ文字列):
            ...

    def main():
        user1 = User()
        server1 = Server("https://server1/")

        user1.認証リクエスト(server=server1)
