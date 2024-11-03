from abc import ABC
from typing import Any, Dict, Optional

import requests
from requests import Response, Session

from ..config import Config
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class BaseAPI(ABC):
    """APIリクエストの基底クラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        """
        BaseAPIクラスの初期化

        Args:
            session (Optional[Session]): リクエストセッション。デフォルトはNone。
        """
        self.base_url: str = Config.BASE_URL
        self.session: Session = session or Session()
        self.cookies: Dict[str, str] = load_cookies()
        self.headers: Dict[str, str] = {}

    def _make_request(
        self,
        method: str,
        endpoint: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        APIリクエストを実行する共通メソッド

        Args:
            method (str): HTTPメソッド
            endpoint (str): APIエンドポイント
            headers (Optional[Dict[str, str]], optional): リクエストヘッダー
            data (Optional[Dict[str, Any]], optional): リクエストデータ
            params (Optional[Dict[str, Any]], optional): クエリパラメータ
            **kwargs: 追加のリクエストオプション

        Returns:
            Dict[str, Any]: APIレスポンス

        Raises:
            APIError: APIリクエストが失敗した場合
        """
        try:
            response: Response = self.session.request(
                method=method,
                url=f"{self.base_url}{endpoint}",
                headers=headers or self.headers,
                cookies=self.cookies,
                json=data,
                params=params,
                **kwargs,
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as error:
            self._handle_request_error(error)

    def _handle_request_error(
        self, error: requests.exceptions.RequestException
    ) -> None:
        """
        リクエストエラーを処理する

        Args:
            error (requests.exceptions.RequestException): 発生したエラー

        Raises:
            APIError: 整形されたAPIエラー
        """
        status_code = error.response.status_code if hasattr(error, "response") else None
        response_data = error.response.json() if hasattr(error, "response") else None
        raise APIError(
            message=f"APIリクエストに失敗しました: {str(error)}",
            status_code=status_code,
            response=response_data,
        )

    def _format_response(
        self, response: Dict[str, Any], key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        APIレスポンスを整形する

        Args:
            response (Dict[str, Any]): 生のAPIレスポンス
            key (Optional[str], optional): 抽出するデータのキー

        Returns:
            Dict[str, Any]: 整形されたレスポンス
        """
        if key and key in response.get("data", {}):
            return {"success": True, "data": response["data"][key]}
        return response
