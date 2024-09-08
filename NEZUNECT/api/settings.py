from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class SettingsAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("settings")
        self.cookies = load_cookies()

    def change_dark_mode(self, dark_mode: bool) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.THEME}"
        data = {"dark_mode": dark_mode}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ダークモードの変更に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def change_language(self, language: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.LANGUAGE}"
        headers = Headers.get_plain_text("settings/account")
        language_code = None if language == "auto" else language
        data = {"language": language_code}

        try:
            response = requests.put(
                url, headers=headers, cookies=load_cookies(), json=data
            )
            response.raise_for_status()
            result = response.json()
            if result.get("message") == "Language Setting updated successfully.":
                return {"success": True, "response": result}
            else:
                return {"success": False, "response": result}
        except requests.exceptions.HTTPError as e:
            print(f"HTTPエラー: {e}")
            print(f"レスポンス内容: {response.text}")
            return {"success": False, "error": str(e), "response": response.text}
        except requests.exceptions.RequestException as e:
            print(f"リクエストエラー: {e}")
            return {"success": False, "error": str(e)}

    def change_custom_color(self, color_type: str, color: str) -> Dict[str, Any]:
        """
        Subnect APIを使用してカスタムカラー設定を変更します。

        Args:
            color_type (str): 変更する色の種類（"backColor", "borderColor", "accentColor", "fontColor"のいずれか）。
            color (str): 設定する色のHEXコード（例: "e6e6e6"）。

        Returns:
            Dict[str, Any]: APIからのレスポンス。
        """
        url = f"{self.base_url}{Config.Endpoints.THEME}"

        headers = Headers.get_plain_text("settings/theme")

        data = {color_type: color}

        try:
            response = requests.put(
                url, headers=headers, cookies=load_cookies(), json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "response": result}
        except requests.exceptions.HTTPError as e:
            print(f"HTTPエラー: {e}")
            print(f"レスポンス内容: {response.text}")
            return {"success": False, "error": str(e), "response": response.text}
        except requests.exceptions.RequestException as e:
            print(f"リクエストエラー: {e}")
            return {"success": False, "error": str(e)}

    def change_notification_sound(self, notification_sound: bool) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.NOTIFICATION_SOUND}"
        headers = Headers.get_plain_text("settings/notification")
        data = {"notification_sound": notification_sound}

        try:
            response = requests.put(
                url, headers=headers, cookies=load_cookies(), json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "response": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"通知音の変更に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
