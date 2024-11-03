from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class ProfileInfo:
    """プロフィール情報を表すデータクラス"""

    username: str
    nickname: str
    bio: Optional[str]
    icon_url: Optional[str]
    header_url: Optional[str]
    is_following: bool
    is_follower: bool
    following_count: int
    followers_count: int
    created_at: datetime
    is_official: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProfileInfo":
        """辞書からProfileInfoインスタンスを生成"""
        return cls(
            username=data.get("username", ""),
            nickname=data.get("nickname", ""),
            bio=data.get("bio"),
            icon_url=data.get("icon", {}).get("assetUrl"),
            header_url=data.get("header", {}).get("assetUrl"),
            is_following=data.get("isFollowing", False),
            is_follower=data.get("isFollower", False),
            following_count=data.get("followingCount", 0),
            followers_count=data.get("followersCount", 0),
            created_at=datetime.fromisoformat(data.get("createdAt", "")),
            is_official=data.get("official", False),
        )


class ProfileAPI(BaseAPI):
    """プロフィール関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__(session)
        self.headers = Headers.get_json("profile")

    def get_profile(self, username: str) -> Dict[str, ProfileInfo]:
        """
        プロフィール情報を取得

        Args:
            username (str): ユーザー名

        Returns:
            Dict[str, ProfileInfo]: プロフィール情報

        Raises:
            APIError: プロフィール情報の取得に失敗した場合
        """
        try:
            response = self._make_request(
                "GET",
                f"{Config.Endpoints.PROFILE}/{username}",
            )
            profile = ProfileInfo.from_dict(response["data"])
            return {"success": True, "data": profile}
        except APIError as error:
            raise APIError(
                f"プロフィール情報の取得に失敗しました: {str(error)}", error.status_code
            )

    def update_profile(
        self,
        *,
        nickname: Optional[str] = None,
        bio: Optional[str] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        プロフィール情報を更新

        Args:
            nickname (Optional[str], optional): 新しいニックネーム
            bio (Optional[str], optional): 新しい自己紹介
            email (Optional[str], optional): 新しいメールアドレス
            username (Optional[str], optional): 新しいユーザー名

        Returns:
            Dict[str, Any]: 更新結果

        Raises:
            APIError: プロフィールの更新に失敗した場合
        """
        try:
            if nickname or bio:
                data = {}
                if nickname:
                    data["nickname"] = nickname
                if bio:
                    data["bio"] = bio
                response = self._make_request(
                    "PUT",
                    Config.Endpoints.PROFILE,
                    data=data,
                )

            if email:
                response = self._make_request(
                    "POST",
                    Config.Endpoints.PROFILE_EMAIL,
                    data={"email": email},
                )

            if username:
                response = self._make_request(
                    "PUT",
                    Config.Endpoints.PROFILE_USERNAME,
                    data={"username": username},
                )

            return response
        except APIError as error:
            raise APIError(
                f"プロフィールの更新に失敗しました: {str(error)}", error.status_code
            )

    def pin_post(self, post_id: str) -> Dict[str, Any]:
        """
        投稿をピン留め

        Args:
            post_id (str): ピン留めする投稿のID

        Returns:
            Dict[str, Any]: ピン留め結果

        Raises:
            APIError: ピン留めに失敗した場合
        """
        try:
            response = self._make_request(
                "POST",
                Config.Endpoints.POST_PIN.format(post_id=post_id),
            )
            return response
        except APIError as error:
            raise APIError(
                f"投稿のピン留めに失敗しました: {str(error)}", error.status_code
            )
