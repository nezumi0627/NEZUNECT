from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class BookmarkFolder:
    """ブックマークフォルダ情報を表すデータクラス"""

    folder_id: str
    name: str
    post_count: int
    created_at: datetime

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BookmarkFolder":
        """辞書からBookmarkFolderインスタンスを生成"""
        return cls(
            folder_id=data.get("folderId", ""),
            name=data.get("name", ""),
            post_count=data.get("postCount", 0),
            created_at=datetime.fromisoformat(data.get("createdAt", "")),
        )


class BookmarksAPI(BaseAPI):
    """ブックマーク関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        """
        BookmarksAPIクラスの初期化

        Args:
            session (Optional[Session]): リクエストセッション
        """
        super().__init__(session)
        self.headers = Headers.get_json("bookmarks")

    def get_bookmarks(self) -> Dict[str, List[BookmarkFolder]]:
        """
        ブックマークフォルダの一覧を取得

        Returns:
            Dict[str, List[BookmarkFolder]]: ブックマークフォルダのリスト

        Raises:
            APIError: フォルダの取得に失敗した場合
        """
        try:
            response = self._make_request(
                "GET",
                Config.Endpoints.BOOKMARKS,
            )
            folders = [
                BookmarkFolder.from_dict(folder)
                for folder in response["data"].get("folders", [])
            ]
            return {"success": True, "data": folders}
        except APIError as error:
            raise APIError(
                f"ブックマークの取得に失敗しました: {str(error)}", error.status_code
            )

    def add_bookmark(self, folder_id: str, post_id: str) -> Dict[str, Any]:
        """
        指定したフォルダに投稿をブックマークとして追加

        Args:
            folder_id (str): ブックマークフォルダのID
            post_id (str): ブックマークする投稿のID

        Returns:
            Dict[str, Any]: 追加結果

        Raises:
            APIError: ブックマークの追加に失敗した場合
        """
        try:
            response = self._make_request(
                "POST",
                Config.Endpoints.BOOKMARK_ADD.format(folder_id=folder_id),
                data={"postId": post_id},
            )
            return response
        except APIError as error:
            raise APIError(
                f"ブックマークの追加に失敗しました: {str(error)}", error.status_code
            )

    def create_bookmark_folder(self, name: str) -> Dict[str, Any]:
        """
        新しいブックマークフォルダを作成

        Args:
            name (str): フォルダ名

        Returns:
            Dict[str, Any]: 作成されたフォルダ情報

        Raises:
            APIError: フォルダの作成に失敗した場合
        """
        try:
            response = self._make_request(
                "POST",
                Config.Endpoints.BOOKMARKS,
                data={"name": name},
            )
            return response
        except APIError as error:
            raise APIError(
                f"ブックマークフォルダの作成に失敗しました: {str(error)}",
                error.status_code,
            )
