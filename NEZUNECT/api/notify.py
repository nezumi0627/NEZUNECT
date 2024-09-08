from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class NotifyAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("notifications")
        self.cookies = load_cookies()

    def get_notifications(self, skip: int = 0) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.NOTIFICATIONS}?skip={skip}"

        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("notifications", [])}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"通知の取得に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
