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
    import sys
    from pathlib import Path
    from random import shuffle
    # installed
    # custom

    TOPICS_DIR = Path("topics")
    PICKUP_DIR = Path("pickup-topic")
    MODE_RANDOM_PICK = "random_pick"
    MODE_SAVE = "save"

    # 拡張性のための記載
    def _get_parent_dir():
        """
        カレントディレクトリ、親ディレクトリの情報取得
        本pythonコード自体をどこかのフォルダ内に配置したい場合、必要になる。
        """
        current_dir = os.getcwd()
        parent_dir = os.path.join(current_dir, os.pardir)

    def _get_path_list(path: str|Path, pattern: str = "**/*") -> list[Path]:
        # 普通に、import glob   glob.glob(pattern)としてもOK
        # return glob(pattern)
        pathlist = Path(path).glob(pattern)
        return list(pathlist)

    def _clear_pickup_directory() -> None:
        for item in PICKUP_DIR.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    def _copy_pickup_files(folder_path: str|Path) -> None:
        target_folder_path = os.path.join(PICKUP_DIR, os.path.basename(folder_path))
        shutil.copytree(folder_path, target_folder_path)

    def _copy_directory(src: Path, dst: Path) -> None:
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    def _random_pick() -> None:
        _clear_pickup_directory()
        pathlist = _get_path_list(TOPICS_DIR, "*")
        shuffle(pathlist)
        for pick_folder_path in pathlist[:3]:
            _copy_pickup_files(pick_folder_path)
            print(pick_folder_path)

    def _save() -> None:
        if not PICKUP_DIR.exists():
            raise FileNotFoundError(f"pickup-topic directory not found: {PICKUP_DIR}")

        for pickup_dir in _get_path_list(PICKUP_DIR, "*"):
            target_dir = TOPICS_DIR / pickup_dir.name
            _copy_directory(pickup_dir, target_dir)
            print(f"saved: {pickup_dir.name}")

    def _usage() -> str:
        return (
            "Usage: python random_pick.py <mode>\n"
            f"Modes: {MODE_RANDOM_PICK}, {MODE_SAVE}\n"
            "Examples:\n"
            f"  python random_pick.py {MODE_RANDOM_PICK}\n"
            f"  python random_pick.py {MODE_SAVE}\n"
        )

    def main() -> None:
        if len(sys.argv) != 2:
            print(_usage())
            return

        mode = sys.argv[1]
        if mode == MODE_RANDOM_PICK:
            _random_pick()
        elif mode == MODE_SAVE:
            _save()
        else:
            print(f"Unknown mode: {mode}")
            print(_usage())

    if __name__ == "__main__":
        main()
