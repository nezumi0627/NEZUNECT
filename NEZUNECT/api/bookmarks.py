from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class BookmarksAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("bookmarks")
        self.cookies = load_cookies()

    def get_bookmarks(self) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.BOOKMARKS}"

        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("folders", [])}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ブックマークの取得に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def add_bookmark(self, folder_id: str, post_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.BOOKMARK_ADD.format(folder_id=folder_id)}"
        data = {"postId": post_id}

        try:
            response = requests.post(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ブックマークの追加に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def create_bookmark_folder(self, name: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.BOOKMARKS}"
        data = {"name": name}

        try:
            response = requests.post(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ブックマークフォルダの作成に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
