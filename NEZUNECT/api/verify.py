from typing import Any, Dict, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


class VerifyAPI(BaseAPI):
    def __init__(self, session: Optional[Session] = None):
        super().__init__(session)
        self.headers = Headers.get_json("verify")

    def verify_email(self, email: str, code: str) -> Dict[str, Any]:
        """
        メールアドレスの確認を行います。

        Args:
            email (str): 確認するメールアドレス。
            code (str): 確認コード。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        data = {"email": email, "code": code}

        try:
            response = self._request(
                "PUT",
                Config.Endpoints.EMAIL_VERIFY,
                headers=self.headers,
                data=data,
            )
            return response
        except APIError as e:
            raise APIError(
                f"メールアドレスの確認に失敗しました: {str(e)}",
                status_code=e.status_code,
                response=e.response,
            )
