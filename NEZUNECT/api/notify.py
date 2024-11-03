from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class Notification:
    """通知情報を表すデータクラス"""

    notification_id: str
    type: str
    text: str
    created_at: datetime
    read: bool
    profile: Dict[str, Any]
    post: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Notification":
        """辞書からNotificationインスタンスを生成"""
        return cls(
            notification_id=data.get("notificationId", ""),
            type=data.get("type", ""),
            text=data.get("text", ""),
            created_at=datetime.fromisoformat(data.get("createdAt", "")),
            read=data.get("read", False),
            profile=data.get("profile", {}),
            post=data.get("post"),
        )


class NotifyAPI(BaseAPI):
    """通知関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        """
        NotifyAPIクラスの初期化

        Args:
            session (Optional[Session]): リクエストセッション
        """
        super().__init__(session)
        self.headers = Headers.get_json("notifications")

    def get_notifications(self, skip: int = 0) -> Dict[str, List[Notification]]:
        """
        通知一覧を取得

        Args:
            skip (int, optional): スキップする通知数。デフォルトは0。

        Returns:
            Dict[str, List[Notification]]: 通知のリスト

        Raises:
            APIError: 通知の取得に失敗した場合
        """
        try:
            response = self._make_request(
                "GET",
                f"{Config.Endpoints.NOTIFICATIONS}",
                params={"skip": skip},
            )
            notifications = [
                Notification.from_dict(notif)
                for notif in response["data"].get("notifications", [])
            ]
            return {"success": True, "data": notifications}
        except APIError as error:
            raise APIError(f"通知の取得に失敗しました: {str(error)}", error.status_code)
