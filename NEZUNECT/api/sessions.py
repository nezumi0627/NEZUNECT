from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class SessionsAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("sessions")
        self.cookies = load_cookies()

    def get_sessions(self, skip: int = 0) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.SESSIONS}?skip={skip}"

        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("sessions", [])}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"セッション情報の取得に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
