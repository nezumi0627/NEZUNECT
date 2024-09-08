from typing import Any, Dict

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class ProfileAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("profile")
        self.cookies = load_cookies()

    def change_profile_name(self, nickname: str) -> Dict[str, Any]:
        """
        プロフィールのニックネームを変更します。

        Args:
            nickname (str): 新しいニックネーム。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.ENDPOINTS['PROFILE']}"
        data = {"nickname": nickname}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"プロフィール名の変更に失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def change_profile_bio(self, bio: str) -> Dict[str, Any]:
        """
        プロフィールの自己紹介を変更します。

        Args:
            bio (str): 新しい自己紹介。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.Endpoints.PROFILE}"
        data = {"bio": bio}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"自己紹介の変更に失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def change_profile_email(self, email: str) -> Dict[str, Any]:
        """
        プロフィールのメールアドレスを変更します。

        Args:
            email (str): 新しいメールアドレス。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.Endpoints.PROFILE_EMAIL}"
        data = {"email": email}

        try:
            response = requests.post(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"メールアドレスの変更に失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def change_profile_id(self, new_username: str) -> Dict[str, Any]:
        """
        プロフィールのユーザーIDを変更します。

        Args:
            new_username (str): 新しいユーザーID。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.Endpoints.PROFILE_USERNAME}"
        data = {"username": new_username}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ユーザーIDの変更に失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def change_profile_name_bio(self, nickname: str, bio: str) -> Dict[str, Any]:
        """
        プロフィールのニックネームと自己紹介を同時に変更します。

        Args:
            nickname (str): 新しいニックネーム。
            bio (str): 新しい自己紹介。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.Endpoints.PROFILE}"
        data = {"nickname": nickname, "bio": bio}

        try:
            response = requests.put(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"ニックネームと自己紹介の変更に失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def post_profile_pin(self, post_id: str) -> Dict[str, Any]:
        """
        プロフィールに投稿をピン留めします。

        Args:
            post_id (str): ピン留めする投稿のID。

        Returns:
            Dict[str, Any]: APIレスポンス。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        url = f"{self.base_url}{Config.Endpoints.POST_PIN.format(post_id=post_id)}"

        try:
            response = requests.post(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"投稿のピン留めに失敗しました: {str(e)}",
                status_code=response.status_code,
            )

    def change_and_verify_email(
        self, new_email: str, verification_code: str
    ) -> Dict[str, Any]:
        """
        メールアドレスを変更し、その後確認コードを送信して認証を完了します。

        Args:
            new_email (str): 新しいメールアドレス。
            verification_code (str): 確認コード。

        Returns:
            Dict[str, Any]: プロセス全体の結果。

        Raises:
            APIError: APIリクエストが失敗した場合。
        """
        try:
            change_result = self.change_profile_email(new_email)
            if not change_result["success"]:
                return {"success": False, "data": {"details": change_result}}

            verify_result = self.verify_email(new_email, verification_code)
            if not verify_result["success"]:
                return {"success": False, "data": {"details": verify_result}}
            return {
                "success": True,
                "data": {
                    "details": {
                        "change_result": change_result,
                        "verify_result": verify_result,
                    }
                },
            }
        except APIError as e:
            return {
                "success": False,
                "data": {"error": str(e), "status_code": e.status_code},
            }

    def get_profile(self, username: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.PROFILE}/{username}"

        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            profile_data = {
                "username": result.get("username"),
                "nickname": result.get("nickname"),
                "bio": result.get("bio"),
                "icon": result.get("icon", {}).get("assetUrl"),
                "header": result.get("header", {}).get("assetUrl"),
                "isFollowing": result.get("isFollowing"),
                "isFollower": result.get("isFollower"),
                "followingCount": result.get("followingCount"),
                "followersCount": result.get("followersCount"),
                "createdAt": result.get("createdAt"),
                "official": result.get("official"),
            }
            return {"success": True, "data": profile_data}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"プロフィール情報の取得に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
