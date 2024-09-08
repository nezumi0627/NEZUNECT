from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class VerifyAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("verify")
        self.cookies = load_cookies()

    def verify_email(self, email: str, code: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.EMAIL_VERIFY}"
        data = {"email": email, "code": code}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"メールアドレスの確認に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
