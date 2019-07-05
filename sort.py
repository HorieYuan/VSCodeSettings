"""用于对VSCode的用户设置settings.json文件内容按照key排序
"""

import os
import json


def main():
    home = os.path.expanduser("~")
    win_path = "AppData/Roaming/Code/User/settings.json"
    linux_path = ".config/Code/User/settings.json"

    path = os.path.join(home, win_path) if os.name == "nt" else os.path.join(
        home, linux_path) if os.name == "posix" else None

    data = open(path, "r", encoding="utf-8").read()
    data = json.loads(data)
    data = json.dumps(data, sort_keys=True, indent=4)
    with open(path, "w", encoding="utf-8") as fw:
        fw.write(data)


if __name__ == "__main__":
    main()
