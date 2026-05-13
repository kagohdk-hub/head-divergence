from __future__ import annotations
if True:
    """
    topics/フォルダは以下のフォルダからランダムに３つ選択し、
    内容を全て pickup-topic/下にコピーする。

    pickup-topic/ 下は、処理開始時にクリーンアップする。
    """

    # standard
    import os
    import shutil
    from pathlib import Path
    from random import shuffle
    # installed
    # custom

    # 拡張性のための記載
    def _get_parent_dir():
        """
        カレントディレクトリ、親ディレクトリの情報取得
        本pythonコード自体をどこかのフォルダ内に配置したい場合、必要になる。
        """
        current_dir = os.getcwd()
        parent_dir = os.path.join(current_dir, os.pardir)

    def _get_path_list(path: str, pattern: str = "**/*") -> list[str]:
        # 普通に、import glob   glob.glob(pattern)としてもOK
        # return glob(pattern)
        pathlist = Path(path).glob(pattern)
        return [str(path) for path in list(pathlist)]

    def _delete_pickup_files():
        for folder_path in _get_path_list("pickup-topic", "*"):
            shutil.rmtree(folder_path)

    def _copy_pickup_files(folder_path):
        target_folder_path = os.path.join("pickup-topic", os.path.basename(folder_path))
        shutil.copytree(folder_path, target_folder_path)

    def main():
        _delete_pickup_files()
        pathlist = _get_path_list("topics/", "*")
        shuffle(pathlist)
        for pick_folder_path in pathlist[:3]:
            _copy_pickup_files(pick_folder_path)
            print(pick_folder_path)

    if __name__ == "__main__":
        main()
