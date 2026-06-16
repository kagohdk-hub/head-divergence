"""事例
日本三国    空城の計    を題材とする。
    せいいのおおがの目線
"""
if True:
    # standard lib
    from pathlib import Path
    import yaml
    import time
    from typing import Union
    from copy import deepcopy as dc
    from functools import partial
    # import lib
    # handmaid lib

    class IO:
        def __init__(self, path: Path) -> None:
            self.path = path

        def text_load(self, mode: str = "r", encoding: str = "utf-8") -> str:
            with open(self.path, mode=mode, encoding=encoding) as f:
                return f.read()

        def text_dump(self, data: str, mode="w") -> None:
            with open(  self.path
                        , mode=mode, encoding="utf-8") as f:
                return f.write(data)

        def yaml_load(self) -> Union[dict, list]:
            with open(self.path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)

        def yaml_dump(self, data: Union[dict, list]) -> None:
            with open(  self.path
                        , mode="w", encoding="utf-8") as f:
                return yaml.dump(
                    data
                    , f
                    , encoding="utf-8"
                    , allow_unicode=True
                    , sort_keys=False
                )

    SEC = 3
    def division_point_output(io_: IO, liststr: list[str]) -> list[str]:
        time.sleep(SEC)
        io_.text_dump("\n".join(liststr))
        return dc(liststr)

    def main():
        # TODO  これではただ、アニメーションのために列挙しているだけ。
        #       処理の共通かなどがなされて初めて意味が出る。

        io_ = IO("output.md")
        o = partial(division_point_output, io_)

        strlist_0 = []
        strlist_0.append("龍門が１人で座っている。")
        def senario_01(strlist):
            strlist_01 = o(strlist)
            strlist_01.append("龍門が１人であるので、このまま進軍する。")
            strlist_01.append("!! 伏兵がいる可能性がある。")
            o(strlist_01)
        senario_01(strlist_0)
        strlist_02 = o(strlist_0)
        strlist_02.append("伏兵がいる可能性がある。")

        def senario_02n(strlist, 調査できるか: bool):
            if 調査できるか is True:
                def senario_021(strlist_, 伏兵がいるか):
                    strlist_021 = o(strlist_)
                    strlist_021.append("周囲を調査する。")

                    if 伏兵がいるか is True:
                        strlist_0211 = o(strlist_021)
                        strlist_0211.append("伏兵がいれば、撤退する。")
                        o(strlist_0211)
                    else:
                        strlist_0212 = o(strlist_021)
                        strlist_0212.append("伏兵がいなければ、進軍する。")
                        o(strlist_0212)

                for 伏兵がいるか in [True, False]:
                    senario_021(strlist, 伏兵がいるか)
            else:
                def senario_022(strlist_):
                    strlist_022 = o(strlist_)
                    strlist_022.append("!! 周囲は暗闇で調査できない。")
                    strlist_022.append("伏兵の有無は判断できない。")
                    strlist_0221 = o(strlist_022)
                    strlist_0221.append("慎重に進軍する。")
                    strlist_0221.append("矢が確実にあたり、かつ、撤退もできる位置で停止する。")
                    strlist_0221.append("矢を構える。")

                    def senario_0221n(strlist__, 龍門が動じるか: bool):
                        if 龍門が動じるか is True:
                            strlist_02211 = o(strlist__)
                            strlist_02211.append("龍門は動じるはずだ。")
                            strlist_02211.append("動じるということは、本当は伏兵がおらず、伏兵を案じての撤退を期待していたということ。")
                            strlist_02211.append("そのまま進軍する。")
                            o(strlist_02211)
                            strlist_02211.append("!! 龍門は動じない。")
                            o(strlist_02211)
                        else:
                            strlist_02212 = o(strlist__)
                            strlist_02212.append("龍門が動じないならば、それは伏兵がいて、踏み込んでくるのを待っているからだ。")
                            strlist_02212.append("撤退する。")
                            o(strlist_02212)
                            strlist_02212.append("!! 伏兵がいる確証なく撤退したため、味方に腰抜けと思われ士気が乱れた。")
                            o(strlist_02212)
                    for 龍門が動じるか in [True, False]:
                        senario_0221n(strlist_0221, 龍門が動じるか)
                senario_022(strlist)

        for 調査できるか in [True, False]:
            senario_02n(strlist_02, 調査できるか)

    if __name__ == "__main__":
        main()
