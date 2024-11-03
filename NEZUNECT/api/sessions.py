from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class SessionInfo:
    """セッション情報を表すデータクラス"""

    session_id: str
    current: bool
    ip: str
    device: str
    browser: str
    country: str
    region: str
    city: str
    latitude: str
    longitude: str
    created_at: datetime

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SessionInfo":
        """辞書からSessionInfoインスタンスを生成"""
        return cls(
            session_id=data.get("sessionId", ""),
            current=data.get("current", False),
            ip=data.get("ip", ""),
            device=data.get("device", ""),
            browser=data.get("browser", ""),
            country=data.get("country", ""),
            region=data.get("region", ""),
            city=data.get("city", ""),
            latitude=data.get("latitude", ""),
            longitude=data.get("longitude", ""),
            created_at=datetime.fromisoformat(data.get("createdAt", "")),
        )


class SessionsAPI(BaseAPI):
    """セッション関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__(session)
        self.headers = Headers.get_json("sessions")

    def get_sessions(self, skip: int = 0) -> Dict[str, List[SessionInfo]]:
        """
        セッション情報を取得

        Args:
            skip (int, optional): スキップするセッション数。デフォルトは0。

        Returns:
            Dict[str, List[SessionInfo]]: セッション情報のリスト

        Raises:
            APIError: セッション情報の取得に失敗した場合
        """
        try:
            response = self._make_request(
                "GET",
                Config.Endpoints.SESSIONS,
                params={"skip": skip},
            )
            sessions = [
                SessionInfo.from_dict(session)
                for session in response["data"].get("sessions", [])
            ]
            return {"success": True, "data": sessions}
        except APIError as error:
            raise APIError(
                f"セッション情報の取得に失敗しました: {str(error)}", error.status_code
            )
