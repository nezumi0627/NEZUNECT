from dataclasses import dataclass
from typing import Any, Dict, Optional

from requests import Session

from ..config import Config
from ..utils.agent import Headers
from ..utils.exceptions import APIError
from .base import BaseAPI


@dataclass
class ThemeSettings:
    """テーマ設定を表すデータクラス"""

    dark_mode: bool
    back_color: Optional[str] = None
    border_color: Optional[str] = None
    accent_color: Optional[str] = None
    font_color: Optional[str] = None


class SettingsAPI(BaseAPI):
    """設定関連のAPI操作を管理するクラス"""

    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__(session)
        self.headers = Headers.get_json("settings")

    def change_dark_mode(self, dark_mode: bool) -> Dict[str, Any]:
        """
        ダークモードの設定を変更

        Args:
            dark_mode (bool): ダークモードを有効にするかどうか

        Returns:
            Dict[str, Any]: 変更結果

        Raises:
            APIError: 設定の変更に失敗した場合
        """
        try:
            response = self._make_request(
                "PUT",
                Config.Endpoints.THEME,
                data={"dark_mode": dark_mode},
            )
            return response
        except APIError as error:
            raise APIError(
                f"ダークモードの変更に失敗しました: {str(error)}", error.status_code
            )

    def change_language(self, language: str) -> Dict[str, Any]:
        """
        言語設定を変更

        Args:
            language (str): 言語コード（"auto"の場合は自動設定）

        Returns:
            Dict[str, Any]: 変更結果

        Raises:
            APIError: 設定の変更に失敗した場合
        """
        try:
            response = self._make_request(
                "PUT",
                Config.Endpoints.LANGUAGE,
                headers=Headers.get_plain_text("settings/account"),
                data={"language": None if language == "auto" else language},
            )
            return response
        except APIError as error:
            raise APIError(
                f"言語設定の変更に失敗しました: {str(error)}", error.status_code
            )

    def change_custom_color(self, color_type: str, color: str) -> Dict[str, Any]:
        """
        カスタムカラー設定を変更

        Args:
            color_type (str): 変更する色の種類
            color (str): 設定する色のHEXコード

        Returns:
            Dict[str, Any]: 変更結果

        Raises:
            APIError: 設定の変更に失敗した場合
        """
        try:
            response = self._make_request(
                "PUT",
                Config.Endpoints.THEME,
                headers=Headers.get_plain_text("settings/theme"),
                data={color_type: color},
            )
            return response
        except APIError as error:
            raise APIError(
                f"カスタムカラーの変更に失敗しました: {str(error)}", error.status_code
            )

    def change_notification_settings(
        self, notification_sound: bool, messages_following_only: bool
    ) -> Dict[str, Any]:
        """
        通知設定を変更

        Args:
            notification_sound (bool): 通知音を有効にするかどうか
            messages_following_only (bool): フォロー中のユーザーからのみメッセージを受信するかどうか

        Returns:
            Dict[str, Any]: 変更結果

        Raises:
            APIError: 設定の変更に失敗した場合
        """
        try:
            sound_response = self._make_request(
                "PUT",
                Config.Endpoints.NOTIFICATION_SOUND,
                headers=Headers.get_plain_text("settings/notification"),
                data={"notification_sound": notification_sound},
            )

            following_response = self._make_request(
                "PUT",
                Config.Endpoints.MESSAGES_FOLLOWING_ONLY,
                headers=Headers.get_plain_text("settings/security"),
                data={"messagesFollowingOnly": messages_following_only},
            )

            return {
                "success": True,
                "data": {
                    "sound_settings": sound_response["data"],
                    "following_settings": following_response["data"],
                },
            }
        except APIError as error:
            raise APIError(
                f"通知設定の変更に失敗しました: {str(error)}", error.status_code
            )
