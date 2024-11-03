from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class PostAsset:
    """投稿のアセット情報を表すデータクラス"""

    asset_id: str
    asset_url: str
    asset_type: str
    spoiler: bool
    alt_text: Optional[str] = None


@dataclass
class PostProfile:
    """投稿者のプロフィール情報を表すデータクラス"""

    profile_id: str
    username: str
    nickname: str
    bio: Optional[str]
    icon_url: Optional[str]
    is_official: bool
    plan_name: str
    created_at: datetime
    is_following: bool
    is_follower: bool
    is_blocking: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PostProfile":
        """辞書からPostProfileインスタンスを生成"""
        return cls(
            profile_id=data.get("profileId", ""),
            username=data.get("username", ""),
            nickname=data.get("nickname", ""),
            bio=data.get("bio"),
            icon_url=data.get("icon", {}).get("assetUrl"),
            is_official=data.get("official", False),
            plan_name=data.get("planName", ""),
            created_at=datetime.fromisoformat(data.get("createdAt", "")),
            is_following=data.get("isFollowing", False),
            is_follower=data.get("isFollower", False),
            is_blocking=data.get("isBlocking", False),
        )


class PostsAPI(BaseAPI):
    """投稿関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        """
        PostsAPIクラスの初期化

        Args:
            session (Optional[Session]): リクエストセッション
        """
        super().__init__(session)
        self.headers = Headers.get_json("home")

    def create_post(
        self,
        text: str,
        *,
        assets: List[str] = [],
        scope: str = "public",
        scheduled_at: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        投稿を作成する

        Args:
            text (str): 投稿本文
            assets (List[str], optional): アセットIDのリスト
            scope (str, optional): 公開範囲
            scheduled_at (Optional[str], optional): 投稿予定日時（ISO 8601形式）

        Returns:
            Dict[str, Any]: 作成された投稿の情報

        Raises:
            APIError: 投稿の作成に失敗した場合
        """
        data = {
            "text": text,
            "assets": assets,
            "scope": scope,
        }

        if scheduled_at:
            data["scheduledAt"] = scheduled_at

        try:
            response = self._make_request(
                "POST",
                Config.Endpoints.POSTS,
                data=data,
            )
            return self._format_response(response, "post")
        except APIError as error:
            raise APIError(f"投稿の作成に失敗しました: {str(error)}", error.status_code)

    def like_post(self, post_id: str) -> Dict[str, Any]:
        """
        投稿にいいねを付ける

        Args:
            post_id (str): いいねを付ける投稿のID

        Returns:
            Dict[str, Any]: いいねの結果情報

        Raises:
            APIError: いいねの追加に失敗した場合
        """
        try:
            response = self._make_request(
                "POST",
                Config.Endpoints.LIKE_POST.format(post_id=post_id),
            )
            return response
        except APIError as error:
            raise APIError(
                f"いいねの追加に失敗しました: {str(error)}", error.status_code
            )
