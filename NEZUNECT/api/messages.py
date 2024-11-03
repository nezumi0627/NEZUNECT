from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class MessageProfile:
    """メッセージの送信者/受信者のプロフィール情報を表すデータクラス"""

    profile_id: str
    username: str
    nickname: str
    bio: Optional[str]
    icon_url: Optional[str]
    icon_name: Optional[str]
    is_official: bool
    plan_name: str
    created_at: str
    is_following: bool
    is_follower: bool
    is_blocking: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MessageProfile":
        """APIレスポンスからMessageProfileインスタンスを生成"""
        return cls(
            profile_id=data.get("profileId", ""),
            username=data.get("username", ""),
            nickname=data.get("nickname", ""),
            bio=data.get("bio"),
            icon_url=data.get("icon", {}).get("assetUrl"),
            icon_name=data.get("icon", {}).get("assetName"),
            is_official=data.get("official", False),
            plan_name=data.get("planName", ""),
            created_at=data.get("createdAt", ""),
            is_following=data.get("isFollowing", False),
            is_follower=data.get("isFollower", False),
            is_blocking=data.get("isBlocking", False),
        )


@dataclass
class Message:
    """メッセージ情報を表すデータクラス"""

    message_id: str
    text: str
    created_at: str
    read_at: Optional[str]
    assets: List[Dict[str, Any]]
    reactions: List[Dict[str, Any]]
    profile: MessageProfile
    receiver: MessageProfile

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        """APIレスポンスからMessageインスタンスを生成"""
        return cls(
            message_id=data.get("messageId", ""),
            text=data.get("text", ""),
            created_at=data.get("createdAt", ""),
            read_at=data.get("readAt"),
            assets=data.get("assets", []),
            reactions=data.get("reactions", []),
            profile=MessageProfile.from_dict(data.get("profile", {})),
            receiver=MessageProfile.from_dict(data.get("receiver", {})),
        )

    def format_message(self) -> str:
        """メッセージを文字列形式でフォーマット"""
        return (
            f"メッセージID: {self.message_id}\n"
            f"テキスト: {self.text}\n"
            f"作成日時: {self.created_at}\n"
            f"送信者:\n{self._format_profile(self.profile)}\n"
            f"受信者:\n{self._format_profile(self.receiver)}\n"
            f"アセット: {', '.join(str(asset) for asset in self.assets)}\n"
            f"リアクション: {', '.join(str(reaction) for reaction in self.reactions)}"
        )

    @staticmethod
    def _format_profile(profile: MessageProfile) -> str:
        """プロフィール情報を文字列形式でフォーマット"""
        return (
            f"  ユーザー名: {profile.username}\n"
            f"  ニックネーム: {profile.nickname}\n"
            f"  プロフィールID: {profile.profile_id}\n"
            f"  Bio: {profile.bio}"
        )


class MessagesAPI(BaseAPI):
    """メッセージ関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None):
        """
        MessagesAPIクラスの初期化

        Args:
            session (Optional[Session]): 共有セッション。指定がない場合は新規作成。
        """
        super().__init__(session)
        self.headers = Headers.get_plain_text("messages")

    def get_messages(self, receiver_id: str, skip: int = 0) -> Dict[str, Any]:
        """
        特定のユーザーとのメッセージ履歴を取得

        Args:
            receiver_id (str): 相手のプロフィールID
            skip (int): スキップするメッセージ数（デフォルト: 0）

        Returns:
            Dict[str, Any]: 成功時はメッセージリストを含むレスポンス

        Raises:
            APIError: APIリクエストが失敗した場合
        """
        try:
            response = self._request(
                "GET",
                f"{Config.Endpoints.MESSAGES.format(receiver_id=receiver_id)}?skip={skip}",
                headers=self.headers,
            )
            messages = [
                Message.from_dict(msg) for msg in response["data"].get("messages", [])
            ]
            return {"success": True, "data": messages}
        except APIError as e:
            raise APIError(
                f"メッセージの取得に失敗しました: {str(e)}",
                status_code=e.status_code,
                response=e.response,
            )

    def send_message(
        self, receiver_id: str, text: str, assets: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        メッセージを送信

        Args:
            receiver_id (str): 受信者のプロフィールID
            text (str): メッセージ本文
            assets (Optional[List[str]]): 添付アセットのIDリスト

        Returns:
            Dict[str, Any]: 成功時は送信されたメッセージ情報を含むレスポンス

        Raises:
            APIError: APIリクエストが失敗した場合
        """
        headers = Headers.get_plain_text(f"messages/{receiver_id}")
        headers.update(
            {
                "Content-Type": "text/plain;charset=UTF-8",
                "Origin": "https://subnect.com",
                "Referer": "https://subnect.com/messages/user_s0ma",
            }
        )

        data = {
            "text": text,
            "assets": assets or [],
            "receiverId": receiver_id,
        }

        try:
            response = self._request(
                "POST",
                f"{Config.Endpoints.MESSAGES.format(receiver_id=receiver_id)}",
                headers=headers,
                data=data,
            )
            message = Message.from_dict(response["data"]["messageData"])
            return {"success": True, "data": message}
        except APIError as e:
            raise APIError(
                f"メッセージの送信に失敗しました: {str(e)}",
                status_code=e.status_code,
                response=e.response,
            )
