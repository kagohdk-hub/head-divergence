"""mermaidで出力できないかを検討する"""
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
        liststr_display = [
            "```mermaid"
            , "graph TB"
        ] + liststr + [
            "```"
        ]
        time.sleep(SEC)
        io_.text_dump("\n".join(liststr_display))
        return dc(liststr)

    def main():
        io_ = IO("output.md")
        o = partial(division_point_output, io_)

        liststr_0 = []
        liststr_0.append("e01[龍門が１人で座っている。]")
        liststr_0.append("e02[伏兵がいる可能性がある。]")
        liststr_0.append("e01 ---> e02")
        o(liststr_0)
        liststr_0.append("---> e11[周囲を調査する]")
        o(liststr_0)
        liststr_0.append("---> e12[！！！暗闇で調査ができない！！！]")
        o(liststr_0)
        liststr_0.append("e21[伏兵の有無は判断できない。]")
        liststr_0.append("e02 ---> e21")
        o(liststr_0)
        liststr_0.append("---> e22[慎重に進軍する。]")
        liststr_0.append("---> e23[矢が確実にあたり、かつ、撤退もできる位置で停止する。]")
        liststr_0.append("---> e24[矢を構える。]")

        liststr_0.append("---> e311[龍門は動じるはずだ。]")
        liststr_0.append("---> e312[動じるということは、本当は伏兵がおらず、伏兵を案じての撤退を期待していたということ。]")
        liststr_0.append("---> e313[そのまま進軍する。]")
        o(liststr_0)
        liststr_0.append("---> e314[！！！龍門は動じない。！！！]")
        liststr_0.append("e311[誤：龍門は動じるはずだ。]")
        o(liststr_0)
        liststr_0.append("e24 ---> e321[龍門が動じない]")
        liststr_0.append("---> e322[それは伏兵がいて、踏み込んでくるのを待っているからだ。]")
        liststr_0.append("---> e323[撤退する。]")
        o(liststr_0)
        liststr_0.append("---> e324[！！！伏兵がいる確証なく撤退したため、味方に腰抜けと思われ士気が乱れた。！！！]")
        o(liststr_0)

    if __name__ == "__main__":
        main()
