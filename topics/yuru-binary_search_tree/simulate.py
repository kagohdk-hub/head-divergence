from __future__ import annotations
if True:
    from dataclasses import dataclass
    from random import randint
    from functools import partial

    class PrintLogger:  # ロジックを極力邪魔しないように、ログ出し部分は切り出し、ロジック内には１行で出したい。
        @classmethod
        def print1(cls, element: BinarySearchTreeElement, index: int, is_find: bool):
            if is_find:
                cls.print_elem_info(element, index)
        def print_upper(element: BinarySearchTreeElement, is_find: bool):
            if is_find:
                print(f"{' '*element.value}      ＼")
        def print_lower(element: BinarySearchTreeElement, is_find: bool):
            if is_find:
                print(f"{' '*element.value}    ／")
        def print_list(bst: BinarySearchTree):
            line1 = line2 = line3 = line4 = ""
            for index, elem in enumerate(bst.element_list):
                line1 += f"{index:>3}"
                line2 += f"{elem.value:>3}"
                line3 += f"{elem.upper_index if elem.upper_index else '__':>3}"
                line4 += f"{elem.lower_index if elem.lower_index else '__':>3}"
            print(line1)
            print(line2)
            print(line3)
            print(line4)
        def print_elem_info(bste: BinarySearchTreeElement, index: int):
            print(f"{' '*bste.value}:({index}):{bste.value}[{bste.lower_index},{bste.upper_index}]")
    pl = PrintLogger

    @dataclass
    class BinarySearchTreeElement:
        value: int
        lower_index: int = None
        upper_index: int = None

    class BinarySearchTree:
        def __init__(self):
            self.element_list: list[BinarySearchTree] = []
            self.next_index: int = 0

        def insert(self, value: int):
            self.next_index = len(self.element_list)

            if self.next_index:
                edge_index, edge_element = self.recursive_find(value)
                if edge_element.value <= value:
                    self.element_list[edge_index].upper_index = self.next_index
                else:
                    self.element_list[edge_index].lower_index = self.next_index

            self.element_list.append(BinarySearchTreeElement(value))

        def recursive_find(self, value: int
                            , index: int = 0
                            , nest_level: int = 0
                            , is_find: bool = False
                            ) -> tuple[int, BinarySearchTreeElement]:
            if nest_level >= 100:
                raise Exception("ERROR : NEST LEVEL is OVER.")
            nest_level += 1

            element: BinarySearchTreeElement = self.element_list[index]
            pl.print1(element, index, is_find)
            if is_find and element.value == value:
                return index, element

            recursive_find_partial = partial(
                self.recursive_find
                , value=value, nest_level=nest_level, is_find=is_find)
            if element.value <= value:
                if element.upper_index is None:
                    return index, element
                else:
                    pl.print_upper(element, is_find)
                    edge_index, edge_element = recursive_find_partial(index=element.upper_index)
            else:
                if element.lower_index is None:
                    return index, element
                else:
                    pl.print_lower(element, is_find)
                    edge_index, edge_element = recursive_find_partial(index=element.lower_index)

            return edge_index, edge_element

    def main():
        # 初期設定
        bst = BinarySearchTree()
        datalist = [randint(0, 100) for _ in range(30)]
        target_value = randint(0, 100)

        # 二分探索木 作成
        for data in datalist:
            bst.insert(data)

        print("==="*30)
        print(f"{target_value=}")
        # 二分探索木 探索
        res_index, res_elem = bst.recursive_find(target_value, is_find=True)

        # 結果
        print("---"*30)
        pl.print_elem_info(res_elem, res_index)
        # 作成結果表示
        pl.print_list(bst)

    if __name__ == "__main__":
        main()
