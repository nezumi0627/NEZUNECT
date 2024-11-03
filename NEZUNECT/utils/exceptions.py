from typing import Dict, Optional


class APIError(Exception):
    """APIリクエストに関連するエラーを表す例外クラス。"""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response: Optional[Dict] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

    def __str__(self) -> str:
        error_msg = self.message
        if self.status_code:
            error_msg += f" (Status: {self.status_code})"
        if self.response:
            error_msg += f"\nResponse: {self.response}"
        return error_msg
