import json
from pathlib import Path
from typing import Dict


def load_cookies(cookie_file: str = "./cookie.json") -> Dict[str, str]:
    """
    指定されたJSONファイルからクッキーを読み込みます。

    Args:
        cookie_file (str): クッキー情報が格納されたJSONファイルのパス。

    Returns:
        Dict[str, str]: 読み込まれたクッキー情報。

    Raises:
        FileNotFoundError: 指定されたファイルが見つからない場合。
        json.JSONDecodeError: JSONファイルの解析に失敗した場合。
    """
    try:
        with open(Path(cookie_file), "r") as file:
            cookies = json.load(file)
        return cookies
    except FileNotFoundError:
        raise
    except json.JSONDecodeError:
        raise
